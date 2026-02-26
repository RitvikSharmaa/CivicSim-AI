from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from bson import ObjectId

class PolicyInput(BaseModel):
    raw_text: str = Field(..., description="Natural language policy description")
    user_id: Optional[str] = None

class StructuredPolicy(BaseModel):
    policy_type: str
    target_population: str
    budget_allocation: float
    implementation_timeline: int  # days
    enforcement_level: float  # 0-1
    incentive_structure: Dict[str, float]
    infrastructure_changes: Dict[str, Any]
    
class PolicyDocument(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    raw_text: str
    structured_parameters: StructuredPolicy
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
