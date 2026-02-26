"""
Knowledge Base API Routes
Expose policy knowledge base for testing and querying
"""

from fastapi import APIRouter, HTTPException
from typing import Optional, List, Dict
from app.knowledge.policy_knowledge_base import policy_kb
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/knowledge", tags=["knowledge"])

@router.get("/")
async def knowledge_base_info():
    """Get information about the knowledge base"""
    return {
        "name": "Indian Policy Knowledge Base",
        "version": "1.0.0",
        "status": "operational",
        "coverage": {
            "national_policies": "20+",
            "state_policies": "70+ (36 states/UTs)",
            "total_policies": "90+",
            "states_covered": "All 28 states + 8 UTs"
        },
        "endpoints": {
            "get_policy": "/knowledge/policy/{state}/{category}/{policy_name}",
            "get_state_policies": "/knowledge/state/{state}",
            "search_policies": "/knowledge/search?q={query}",
            "get_related": "/knowledge/related?type={policy_type}&state={state}",
            "get_budget": "/knowledge/budget/{state}",
            "list_states": "/knowledge/states"
        }
    }

@router.get("/states")
async def list_states():
    """List all states with policy data"""
    # Get all states from the knowledge base (excluding 'national')
    all_states = [state for state in policy_kb.policies.keys() if state != "national"]
    
    state_info = []
    for state in all_states:
        policies = policy_kb.get_all_policies_for_state(state)
        policy_count = sum(len(v) if isinstance(v, dict) else 0 for k, v in policies.items() if k != 'budget_2025_26')
        
        state_info.append({
            "state": state,
            "policy_count": policy_count,
            "has_budget": "budget_2025_26" in policies,
            "categories": list(policies.keys())
        })
    
    return {
        "total_states": len(all_states),
        "states": state_info
    }

@router.get("/policy/{state}/{category}/{policy_name}")
async def get_policy(state: str, category: str, policy_name: str):
    """Get specific policy details"""
    policy = policy_kb.get_policy(state, category, policy_name)
    
    if not policy:
        raise HTTPException(
            status_code=404,
            detail=f"Policy not found: {state}/{category}/{policy_name}"
        )
    
    return {
        "state": state,
        "category": category,
        "policy_name": policy_name,
        "policy": policy
    }

@router.get("/state/{state}")
async def get_state_policies(state: str):
    """Get all policies for a specific state"""
    policies = policy_kb.get_all_policies_for_state(state)
    
    if not policies:
        raise HTTPException(
            status_code=404,
            detail=f"No policies found for state: {state}"
        )
    
    # Count policies by category
    summary = {}
    for category, category_policies in policies.items():
        if category == "budget_2025_26":
            summary[category] = "Available"
        elif isinstance(category_policies, dict):
            summary[category] = len(category_policies)
    
    return {
        "state": state,
        "summary": summary,
        "policies": policies
    }

@router.get("/search")
async def search_policies(q: str):
    """Search policies by keyword"""
    if not q or len(q) < 2:
        raise HTTPException(
            status_code=400,
            detail="Query must be at least 2 characters"
        )
    
    results = policy_kb.search_policies(q)
    
    return {
        "query": q,
        "total_results": len(results),
        "results": results
    }

@router.get("/related")
async def get_related_policies(type: str, state: Optional[str] = None):
    """Get related policies by type"""
    related = policy_kb.get_related_policies(type, state)
    
    return {
        "policy_type": type,
        "state": state or "all",
        "total_related": len(related),
        "related_policies": related
    }

@router.get("/budget/{state}")
async def get_budget(state: str, year: str = "2025_26"):
    """Get budget data for a state"""
    budget = policy_kb.get_budget_data(state, year)
    
    if not budget:
        raise HTTPException(
            status_code=404,
            detail=f"Budget data not found for {state} ({year})"
        )
    
    return {
        "state": state,
        "year": year,
        "budget": budget
    }

@router.get("/national/{category}")
async def get_national_policies(category: str):
    """Get national policies by category"""
    valid_categories = ["economic", "social", "infrastructure", "agriculture", "education"]
    
    if category not in valid_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Must be one of: {', '.join(valid_categories)}"
        )
    
    policies = policy_kb.policies.get("national", {}).get(category, {})
    
    return {
        "category": category,
        "total_policies": len(policies),
        "policies": policies
    }

@router.get("/schemes")
async def get_schemes():
    """Get all government schemes"""
    schemes = policy_kb.schemes
    
    return {
        "central_sector": schemes.get("central_sector", []),
        "centrally_sponsored": schemes.get("centrally_sponsored", []),
        "state_schemes": schemes.get("state_schemes", {})
    }

@router.get("/economic-data")
async def get_economic_data():
    """Get economic indicators"""
    return {
        "national": policy_kb.economic_data.get("national", {}),
        "state_wise": policy_kb.economic_data.get("state_wise", {})
    }

@router.get("/test")
async def test_knowledge_base():
    """Quick test of knowledge base functionality"""
    tests = {}
    
    # Test 1: Get specific policy
    try:
        policy = policy_kb.get_policy("Karnataka", "social", "gruha_jyothi")
        tests["get_policy"] = "✅ Pass" if policy else "❌ Fail"
    except Exception as e:
        tests["get_policy"] = f"❌ Error: {str(e)}"
    
    # Test 2: Search
    try:
        results = policy_kb.search_policies("electricity")
        tests["search"] = f"✅ Pass ({len(results)} results)"
    except Exception as e:
        tests["search"] = f"❌ Error: {str(e)}"
    
    # Test 3: Get state policies
    try:
        policies = policy_kb.get_all_policies_for_state("Karnataka")
        tests["state_policies"] = f"✅ Pass ({len(policies)} categories)"
    except Exception as e:
        tests["state_policies"] = f"❌ Error: {str(e)}"
    
    # Test 4: Get budget
    try:
        budget = policy_kb.get_budget_data("Karnataka", "2025_26")
        tests["budget"] = "✅ Pass" if budget else "❌ Fail"
    except Exception as e:
        tests["budget"] = f"❌ Error: {str(e)}"
    
    return {
        "status": "Knowledge Base Test Results",
        "tests": tests,
        "overall": "✅ All tests passed" if all("✅" in v for v in tests.values()) else "⚠️ Some tests failed"
    }
