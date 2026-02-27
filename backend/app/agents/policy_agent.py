import json
from typing import Dict, Any, List
from app.models.india_schema import IndianStructuredPolicy, IndianRegion
from app.services.free_india_data import india_data_service
from app.knowledge.policy_knowledge_base import policy_kb
from app.config import get_settings
import logging
import httpx
import re

logger = logging.getLogger(__name__)
settings = get_settings()

class PolicyAgent:
    """Extracts structured policy parameters from natural language - Indian context"""
    
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Convert natural language policy to structured format"""
        raw_text = state.get("policy_input", "")
        
        # Get region from state, or use default
        region_dict = state.get("region")
        if region_dict:
            region = IndianRegion(state=region_dict["state"])
        else:
            region = IndianRegion(state="Maharashtra")
        
        # Initialize token tracking
        token_usage = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
        
        if settings.demo_mode:
            # Demo mode: deterministic extraction with Indian context
            structured = self._demo_extraction_india(raw_text, region)
        else:
            # Production: use OpenRouter LLM
            structured, token_usage = await self._llm_extraction(raw_text, region)
        
        state["structured_policy"] = structured
        state["token_usage"] = token_usage
        
        # Get related policies from knowledge base
        related_policies = self._get_related_policies(structured.policy_type, region.state)
        state["related_policies"] = related_policies
        
        # Get state-specific context
        state_policies = policy_kb.get_all_policies_for_state(region.state)
        state["state_policy_context"] = state_policies
        
        # Log agent activity
        await self._log_activity(raw_text, structured)
        
        return state
    
    def _get_related_policies(self, policy_type: str, state: str) -> List[Dict]:
        """Get related policies from knowledge base"""
        try:
            # Search for related policies
            related = policy_kb.get_related_policies(policy_type, state)
            
            # Also search by keywords
            keywords = {
                "transportation": ["transport", "traffic", "metro", "bus", "road"],
                "electric_mobility": ["electric", "ev", "charging", "vehicle"],
                "environmental": ["environment", "pollution", "green", "clean"],
                "housing": ["housing", "affordable", "rent", "shelter"],
                "economic": ["economic", "industry", "business", "investment"],
                "tax": ["tax", "gst", "duty", "levy"],
                "subsidy": ["subsidy", "support", "assistance", "benefit"]
            }
            
            search_terms = keywords.get(policy_type, [policy_type])
            for term in search_terms:
                related.extend(policy_kb.search_policies(term))
            
            # Remove duplicates
            seen = set()
            unique_related = []
            for policy in related:
                policy_id = f"{policy.get('state', '')}_{policy.get('policy', '')}"
                if policy_id not in seen:
                    seen.add(policy_id)
                    unique_related.append(policy)
            
            return unique_related[:10]  # Return top 10 related policies
        except Exception as e:
            logger.error(f"Error getting related policies: {e}")
            return []
    
    def _demo_extraction_india(self, text: str, region: IndianRegion) -> IndianStructuredPolicy:
        """Fast deterministic extraction for demo - Indian context"""
        
        # Extract budget in INR
        budget_inr = self._extract_budget_inr(text)
        
        # Determine policy type
        policy_type = self._determine_policy_type(text)
        
        # Get real state data
        state_data = india_data_service.get_state_data(region.state)
        
        return IndianStructuredPolicy.from_inr(
            budget_inr=budget_inr,
            policy_type=policy_type,
            target_population=f"{region.state} residents",
            implementation_timeline_days=90,
            enforcement_level=0.7,
            incentive_structure={
                "tax_reduction_percent": 15.0,
                "subsidy_inr": 5000.0,
                "toll_discount_percent": 50.0
            },
            infrastructure_changes={
                "new_lanes": 2,
                "charging_stations": 50,
                "bus_routes": 10,
                "metro_stations": 3
            },
            region=region
        )
    
    def _extract_budget_inr(self, text: str) -> float:
        """Extract budget from text in INR"""
        text_lower = text.lower()
        
        # Look for crore
        crore_match = re.search(r'(\d+(?:\.\d+)?)\s*crore', text_lower)
        if crore_match:
            return float(crore_match.group(1)) * 10000000
        
        # Look for lakh
        lakh_match = re.search(r'(\d+(?:\.\d+)?)\s*lakh', text_lower)
        if lakh_match:
            return float(lakh_match.group(1)) * 100000
        
        # Look for rupees/inr
        rupee_match = re.search(r'₹?\s*(\d+(?:,\d+)*(?:\.\d+)?)', text)
        if rupee_match:
            amount_str = rupee_match.group(1).replace(',', '')
            return float(amount_str)
        
        # Default: 10 crore
        return 100000000
    
    def _determine_policy_type(self, text: str) -> str:
        """Determine policy type from text"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['transport', 'traffic', 'congestion', 'road', 'metro', 'bus']):
            return "transportation"
        elif any(word in text_lower for word in ['electric', 'ev', 'vehicle', 'charging']):
            return "electric_mobility"
        elif any(word in text_lower for word in ['environment', 'pollution', 'air quality', 'green']):
            return "environmental"
        elif any(word in text_lower for word in ['housing', 'affordable', 'rent']):
            return "housing"
        else:
            return "economic"
    
    async def _llm_extraction(self, text: str, region: IndianRegion) -> tuple[IndianStructuredPolicy, Dict[str, int]]:
        """Use OpenRouter LLM for extraction - returns (policy, token_usage)"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {settings.openrouter_api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": settings.openrouter_model,
                        "messages": [
                            {
                                "role": "system",
                                "content": f"Extract policy parameters for {region.state}, India. Return JSON with: policy_type, budget_allocation_inr (in ₹), implementation_timeline_days, enforcement_level, incentive_structure, infrastructure_changes. Use Indian Rupees (₹) for all amounts."
                            },
                            {
                                "role": "user",
                                "content": text
                            }
                        ]
                    },
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    result = response.json()
                    content = result["choices"][0]["message"]["content"]
                    policy_data = json.loads(content)
                    policy_data["region"] = region
                    
                    # Extract token usage from response
                    usage = result.get("usage", {})
                    token_usage = {
                        "input_tokens": usage.get("prompt_tokens", 0),
                        "output_tokens": usage.get("completion_tokens", 0),
                        "total_tokens": usage.get("total_tokens", 0)
                    }
                    
                    return IndianStructuredPolicy.from_inr(**policy_data), token_usage
                else:
                    logger.warning(f"LLM API failed, falling back to demo mode")
                    return self._demo_extraction_india(text, region), {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
        except Exception as e:
            logger.error(f"LLM extraction error: {e}, falling back to demo mode")
            return self._demo_extraction_india(text, region), {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
    
    async def _log_activity(self, input_data: str, output_data: IndianStructuredPolicy):
        """Log agent activity to MongoDB"""
        logger.info(f"PolicyAgent processed for {output_data.region.state}: {input_data[:50]}...")
