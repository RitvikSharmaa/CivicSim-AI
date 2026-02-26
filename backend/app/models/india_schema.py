from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class IndianRegion(BaseModel):
    """Indian region specification - STATE LEVEL ONLY"""
    country: str = "India"
    state: str = Field(..., description="State/UT name (e.g., Maharashtra, Karnataka, Delhi)")
    
class IndianPolicyInput(BaseModel):
    """Policy input for Indian context"""
    raw_text: str = Field(..., description="Natural language policy description")
    region: IndianRegion
    user_id: Optional[str] = None
    
class IndianStructuredPolicy(BaseModel):
    """Structured policy with Indian context"""
    policy_type: str
    target_population: str
    budget_allocation_inr: float = Field(..., description="Budget in Indian Rupees (₹)")
    budget_in_lakhs: float = Field(..., description="Budget in Lakhs")
    budget_in_crores: float = Field(..., description="Budget in Crores")
    implementation_timeline_days: int
    enforcement_level: float  # 0-1
    incentive_structure: Dict[str, float]
    infrastructure_changes: Dict[str, Any]
    region: IndianRegion
    
    @classmethod
    def from_inr(cls, budget_inr: float, **kwargs):
        """Create policy with automatic lakh/crore conversion"""
        return cls(
            budget_allocation_inr=budget_inr,
            budget_in_lakhs=budget_inr / 100000,
            budget_in_crores=budget_inr / 10000000,
            **kwargs
        )

class IndianSimulationMetrics(BaseModel):
    """Simulation metrics for Indian context"""
    congestion_score: float
    congestion_reduction_percent: float
    energy_load: float
    dissatisfaction_index: float
    economic_stability: float
    infrastructure_stress: Dict[str, float]
    
    # India-specific metrics
    fuel_saved_liters_daily: int
    co2_reduction_tons_yearly: int
    affected_population: int
    vehicles_affected: int
    time_saved_minutes_per_trip: float
    
class IndianImpactPredictions(BaseModel):
    """Impact predictions with Indian metrics"""
    congestion_score: float
    inflation_rate_percent: float
    dissatisfaction_index: float
    energy_stress: float
    
    # India-specific
    fuel_price_impact_inr: float
    public_transport_usage_increase_percent: float
    air_quality_improvement_percent: float
    economic_benefit_crores: float
    
class IndianPolicyDocument(BaseModel):
    """Policy document for Indian government"""
    id: Optional[str] = Field(None, alias="_id")
    raw_text: str
    structured_parameters: IndianStructuredPolicy
    region: IndianRegion
    created_at: datetime = Field(default_factory=datetime.utcnow)
    created_by: Optional[str] = None
    status: str = "draft"  # draft, approved, implemented
    
    class Config:
        populate_by_name = True
