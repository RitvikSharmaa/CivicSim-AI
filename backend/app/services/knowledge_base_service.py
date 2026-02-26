"""
MongoDB-based Knowledge Base Service
Provides efficient storage, retrieval, and search for policy documents
"""

from motor.motor_asyncio import AsyncIOMotorClient
from typing import Dict, List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class KnowledgeBaseService:
    """
    MongoDB-based knowledge base with:
    - Text search indexing
    - Efficient querying
    - Document chunking
    - Semantic search ready
    """
    
    def __init__(self, db_client: AsyncIOMotorClient, db_name: str):
        self.client = db_client
        self.db = self.client[db_name]
        self.policies_collection = self.db["policies"]
        self.schemes_collection = self.db["schemes"]
        self.economic_data_collection = self.db["economic_data"]
        
    async def initialize_indexes(self):
        """Create indexes for efficient querying"""
        try:
            # Text search index on policies
            await self.policies_collection.create_index([
                ("name", "text"),
                ("objective", "text"),
                ("description", "text"),
                ("impact_areas", "text")
            ], name="policy_text_search")
            
            # Compound indexes for filtering
            await self.policies_collection.create_index([
                ("state", 1),
                ("category", 1)
            ], name="state_category_idx")
            
            await self.policies_collection.create_index([
                ("level", 1),
                ("category", 1)
            ], name="level_category_idx")
            
            # Index for budget queries
            await self.policies_collection.create_index([
                ("budget_allocation", -1)
            ], name="budget_idx")
            
            logger.info("Knowledge base indexes created successfully")
        except Exception as e:
            logger.error(f"Error creating indexes: {e}")
    
    async def insert_policy(self, policy_data: Dict) -> str:
        """Insert a single policy document"""
        try:
            policy_data["created_at"] = datetime.utcnow()
            policy_data["updated_at"] = datetime.utcnow()
            
            result = await self.policies_collection.insert_one(policy_data)
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error inserting policy: {e}")
            return None
    
    async def bulk_insert_policies(self, policies: List[Dict]) -> int:
        """Bulk insert multiple policies"""
        try:
            for policy in policies:
                policy["created_at"] = datetime.utcnow()
                policy["updated_at"] = datetime.utcnow()
            
            result = await self.policies_collection.insert_many(policies)
            return len(result.inserted_ids)
        except Exception as e:
            logger.error(f"Error bulk inserting policies: {e}")
            return 0
    
    async def get_policy(self, state: str, category: str, policy_name: str) -> Optional[Dict]:
        """Get a specific policy"""
        try:
            query = {
                "state": state,
                "category": category,
                "policy_key": policy_name
            }
            
            policy = await self.policies_collection.find_one(query)
            if policy:
                policy["_id"] = str(policy["_id"])
            return policy
        except Exception as e:
            logger.error(f"Error getting policy: {e}")
            return None
    
    async def get_state_policies(self, state: str) -> List[Dict]:
        """Get all policies for a state"""
        try:
            cursor = self.policies_collection.find({"state": state})
            policies = await cursor.to_list(length=None)
            
            for policy in policies:
                policy["_id"] = str(policy["_id"])
            
            return policies
        except Exception as e:
            logger.error(f"Error getting state policies: {e}")
            return []
    
    async def get_national_policies(self, category: str) -> List[Dict]:
        """Get national policies by category"""
        try:
            cursor = self.policies_collection.find({
                "level": "national",
                "category": category
            })
            policies = await cursor.to_list(length=None)
            
            for policy in policies:
                policy["_id"] = str(policy["_id"])
            
            return policies
        except Exception as e:
            logger.error(f"Error getting national policies: {e}")
            return []
    
    async def search_policies(self, query: str, limit: int = 50) -> List[Dict]:
        """Full-text search across all policies"""
        try:
            # MongoDB text search
            cursor = self.policies_collection.find(
                {"$text": {"$search": query}},
                {"score": {"$meta": "textScore"}}
            ).sort([("score", {"$meta": "textScore"})]).limit(limit)
            
            policies = await cursor.to_list(length=limit)
            
            for policy in policies:
                policy["_id"] = str(policy["_id"])
            
            return policies
        except Exception as e:
            logger.error(f"Error searching policies: {e}")
            return []
    
    async def get_related_policies(self, policy_type: str, state: Optional[str] = None, limit: int = 10) -> List[Dict]:
        """Get related policies by type"""
        try:
            query = {
                "$or": [
                    {"policy_type": {"$regex": policy_type, "$options": "i"}},
                    {"category": {"$regex": policy_type, "$options": "i"}},
                    {"impact_areas": {"$regex": policy_type, "$options": "i"}}
                ]
            }
            
            if state:
                query["$or"].append({"state": state})
            
            cursor = self.policies_collection.find(query).limit(limit)
            policies = await cursor.to_list(length=limit)
            
            for policy in policies:
                policy["_id"] = str(policy["_id"])
            
            return policies
        except Exception as e:
            logger.error(f"Error getting related policies: {e}")
            return []
    
    async def get_all_states(self) -> List[str]:
        """Get list of all states with policies"""
        try:
            states = await self.policies_collection.distinct("state")
            # Remove 'national' if present
            return [s for s in states if s != "national"]
        except Exception as e:
            logger.error(f"Error getting states: {e}")
            return []
    
    async def get_state_summary(self, state: str) -> Dict:
        """Get summary statistics for a state"""
        try:
            pipeline = [
                {"$match": {"state": state}},
                {"$group": {
                    "_id": "$category",
                    "count": {"$sum": 1},
                    "total_budget": {"$sum": "$budget_allocation"}
                }}
            ]
            
            cursor = self.policies_collection.aggregate(pipeline)
            results = await cursor.to_list(length=None)
            
            summary = {
                "state": state,
                "categories": {},
                "total_policies": 0,
                "total_budget": 0
            }
            
            for result in results:
                category = result["_id"]
                summary["categories"][category] = {
                    "count": result["count"],
                    "budget": result.get("total_budget", 0)
                }
                summary["total_policies"] += result["count"]
                summary["total_budget"] += result.get("total_budget", 0)
            
            return summary
        except Exception as e:
            logger.error(f"Error getting state summary: {e}")
            return {}
    
    async def get_budget_data(self, state: str, year: str = "2025_26") -> Optional[Dict]:
        """Get budget data for a state"""
        try:
            budget = await self.policies_collection.find_one({
                "state": state,
                "document_type": "budget",
                "year": year
            })
            
            if budget:
                budget["_id"] = str(budget["_id"])
            
            return budget
        except Exception as e:
            logger.error(f"Error getting budget data: {e}")
            return None
    
    async def get_top_policies_by_budget(self, limit: int = 10) -> List[Dict]:
        """Get policies with highest budget allocations"""
        try:
            cursor = self.policies_collection.find(
                {"budget_allocation": {"$exists": True, "$ne": None}}
            ).sort("budget_allocation", -1).limit(limit)
            
            policies = await cursor.to_list(length=limit)
            
            for policy in policies:
                policy["_id"] = str(policy["_id"])
            
            return policies
        except Exception as e:
            logger.error(f"Error getting top policies: {e}")
            return []
    
    async def get_policies_by_impact_area(self, impact_area: str) -> List[Dict]:
        """Get policies by impact area"""
        try:
            cursor = self.policies_collection.find({
                "impact_areas": {"$regex": impact_area, "$options": "i"}
            })
            
            policies = await cursor.to_list(length=None)
            
            for policy in policies:
                policy["_id"] = str(policy["_id"])
            
            return policies
        except Exception as e:
            logger.error(f"Error getting policies by impact area: {e}")
            return []
    
    async def update_policy(self, state: str, category: str, policy_key: str, update_data: Dict) -> bool:
        """Update a policy document"""
        try:
            update_data["updated_at"] = datetime.utcnow()
            
            result = await self.policies_collection.update_one(
                {
                    "state": state,
                    "category": category,
                    "policy_key": policy_key
                },
                {"$set": update_data}
            )
            
            return result.modified_count > 0
        except Exception as e:
            logger.error(f"Error updating policy: {e}")
            return False
    
    async def delete_policy(self, state: str, category: str, policy_key: str) -> bool:
        """Delete a policy document"""
        try:
            result = await self.policies_collection.delete_one({
                "state": state,
                "category": category,
                "policy_key": policy_key
            })
            
            return result.deleted_count > 0
        except Exception as e:
            logger.error(f"Error deleting policy: {e}")
            return False
    
    async def get_statistics(self) -> Dict:
        """Get overall knowledge base statistics"""
        try:
            total_policies = await self.policies_collection.count_documents({})
            total_states = len(await self.get_all_states())
            
            # Get policies by level
            national_count = await self.policies_collection.count_documents({"level": "national"})
            state_count = total_policies - national_count
            
            # Get total budget
            pipeline = [
                {"$group": {
                    "_id": None,
                    "total_budget": {"$sum": "$budget_allocation"}
                }}
            ]
            cursor = self.policies_collection.aggregate(pipeline)
            results = await cursor.to_list(length=1)
            total_budget = results[0]["total_budget"] if results else 0
            
            return {
                "total_policies": total_policies,
                "total_states": total_states,
                "national_policies": national_count,
                "state_policies": state_count,
                "total_budget_allocation": total_budget,
                "last_updated": datetime.utcnow().isoformat()
            }
        except Exception as e:
            logger.error(f"Error getting statistics: {e}")
            return {}

# Global instance
kb_service: Optional[KnowledgeBaseService] = None

async def get_kb_service() -> KnowledgeBaseService:
    """Get knowledge base service instance"""
    return kb_service

async def initialize_kb_service(db_client: AsyncIOMotorClient, db_name: str):
    """Initialize knowledge base service"""
    global kb_service
    kb_service = KnowledgeBaseService(db_client, db_name)
    await kb_service.initialize_indexes()
    logger.info("Knowledge base service initialized")
