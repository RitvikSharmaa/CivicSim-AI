from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime

class BehaviorOutput(BaseModel):
    adaptation_rate: float
    compliance_probability: float
    satisfaction_score: float
    economic_impact_personal: float

class SimulationMetrics(BaseModel):
    congestion_score: float
    energy_load: float
    dissatisfaction_index: float
    economic_stability: float
    infrastructure_stress: Dict[str, float]

class ImpactPredictions(BaseModel):
    congestion_score: float
    inflation_rate: float
    dissatisfaction_index: float
    energy_stress: float
    confidence_intervals: Dict[str, List[float]]

class OptimizedPolicy(BaseModel):
    optimized_parameters: Dict[str, float]
    reward_score: float
    improvement_percentage: float
    comparison_metrics: Dict[str, float]

class ExplanationReport(BaseModel):
    shap_values: Dict[str, float]
    feature_importance: Dict[str, float]
    narrative_summary: str
    recommendations: List[str]

class SimulationDocument(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    policy_id: str
    metrics: SimulationMetrics
    impact_predictions: ImpactPredictions
    optimization_result: Optional[OptimizedPolicy] = None
    explanation: Optional[ExplanationReport] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
