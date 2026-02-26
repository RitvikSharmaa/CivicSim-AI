from fastapi import APIRouter, HTTPException, Depends
from app.models.policy_schema import PolicyInput, PolicyDocument
from app.db import get_database
from bson import ObjectId
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/policy", tags=["policy"])

@router.post("/", response_model=dict)
async def create_policy(
    policy_input: PolicyInput,
    db = Depends(get_database)
):
    """Create and store a new policy"""
    try:
        from app.agents.policy_agent import PolicyAgent
        
        agent = PolicyAgent()
        state = {"policy_input": policy_input.raw_text}
        result = await agent.process(state)
        
        # Store in MongoDB
        policy_doc = {
            "raw_text": policy_input.raw_text,
            "structured_parameters": result["structured_policy"].dict(),
            "created_at": datetime.utcnow(),
            "user_id": policy_input.user_id
        }
        
        result = await db.policies.insert_one(policy_doc)
        policy_id = str(result.inserted_id)
        
        logger.info(f"Policy created: {policy_id}")
        
        return {
            "policy_id": policy_id,
            "structured_policy": policy_doc["structured_parameters"]
        }
    
    except Exception as e:
        logger.error(f"Error creating policy: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{policy_id}")
async def get_policy(
    policy_id: str,
    db = Depends(get_database)
):
    """Retrieve a policy by ID"""
    try:
        policy = await db.policies.find_one({"_id": ObjectId(policy_id)})
        
        if not policy:
            raise HTTPException(status_code=404, detail="Policy not found")
        
        policy["_id"] = str(policy["_id"])
        return policy
    
    except Exception as e:
        logger.error(f"Error retrieving policy: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
