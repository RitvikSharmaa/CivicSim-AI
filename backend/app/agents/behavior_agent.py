import torch
import torch.nn as nn
import numpy as np
from typing import Dict, Any
import logging
import os
import pickle
from app.services.free_india_data import india_data_service

logger = logging.getLogger(__name__)

# Global model cache to avoid reloading
_model_cache = {}
_scaler_cache = {}

class BehaviorLSTM(nn.Module):
    """Lightweight LSTM for citizen behavior prediction - OPTIMIZED"""
    def __init__(self, input_size=10, hidden_size=32, output_size=4):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out[:, -1, :])
        return self.sigmoid(output)

class BehaviorAgent:
    """Predicts citizen behavioral adaptation using LSTM - OPTIMIZED"""
    
    def __init__(self):
        # Use cached model if available
        if 'behavior_model' in _model_cache:
            self.model = _model_cache['behavior_model']
            self.scaler = _scaler_cache.get('behavior_scaler')
        else:
            self.model = BehaviorLSTM()
            self._load_trained_model()
            self.model.eval()
            # Cache for future use
            _model_cache['behavior_model'] = self.model
            _scaler_cache['behavior_scaler'] = self.scaler
    
    def _load_trained_model(self):
        """Load trained model if available - OPTIMIZED"""
        model_path = "backend/app/ml/models/india_behavior_lstm.pth"
        scaler_path = "backend/app/ml/models/behavior_scaler.pkl"
        
        if os.path.exists(model_path):
            try:
                # Load with map_location for CPU optimization
                self.model.load_state_dict(
                    torch.load(model_path, map_location=torch.device('cpu'))
                )
                logger.info("Loaded trained Indian behavior model (CACHED)")
            except Exception as e:
                logger.warning(f"Could not load model: {e}")
        
        if os.path.exists(scaler_path):
            try:
                with open(scaler_path, 'rb') as f:
                    self.scaler = pickle.load(f)
            except Exception as e:
                logger.warning(f"Could not load scaler: {e}")
                self.scaler = None
        else:
            self.scaler = None
    
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Predict behavioral responses using REAL state context"""
        policy = state.get("structured_policy")
        
        # Get real state data for context
        region = policy.region
        state_data = india_data_service.get_state_data(region.state)
        
        # Convert policy to feature vector
        features = self._policy_to_features(policy, state_data)
        
        # Run LSTM prediction
        with torch.no_grad():
            input_tensor = torch.FloatTensor(features).unsqueeze(0).unsqueeze(0)
            predictions = self.model(input_tensor).squeeze().numpy()
        
        # Adjust predictions based on real state characteristics
        if state_data:
            literacy_factor = state_data["literacy_rate"] / 100
            income_factor = min(1.0, state_data["median_income_inr"] / 50000)
            urban_factor = state_data["urban_percentage"] / 100
            
            # Higher literacy/income/urbanization = better adaptation
            predictions[0] *= (0.7 + 0.3 * literacy_factor)  # adaptation_rate
            predictions[1] *= (0.7 + 0.3 * income_factor)    # compliance
            predictions[2] *= (0.7 + 0.3 * urban_factor)     # satisfaction
        
        behavior_output = {
            "adaptation_rate": float(np.clip(predictions[0], 0.1, 0.95)),
            "compliance_probability": float(np.clip(predictions[1], 0.1, 0.95)),
            "satisfaction_score": float(np.clip(predictions[2], 0.1, 0.95)),
            "economic_impact_personal": float(np.clip(predictions[3], 0.0, 1.0))
        }
        
        state["behavior_output"] = behavior_output
        logger.info(f"BehaviorAgent predicted for {region.state}: {behavior_output}")
        
        return state
    
    def _policy_to_features(self, policy, state_data=None) -> np.ndarray:
        """Convert policy parameters to feature vector with real state context"""
        # Handle both old and new schema
        budget = getattr(policy, 'budget_allocation_inr', None) or getattr(policy, 'budget_allocation', 1000000)
        timeline = getattr(policy, 'implementation_timeline_days', None) or getattr(policy, 'implementation_timeline', 90)
        
        # Base features
        features = [
            budget / 1e6,  # Budget in millions
            timeline / 365,  # Timeline in years
            policy.enforcement_level,
            policy.incentive_structure.get("tax_reduction", 0) if isinstance(policy.incentive_structure.get("tax_reduction", 0), (int, float)) else policy.incentive_structure.get("tax_reduction_percent", 0) / 100,
            policy.incentive_structure.get("subsidy", 0) if isinstance(policy.incentive_structure.get("subsidy", 0), (int, float)) else policy.incentive_structure.get("subsidy_inr", 0) / 1000,
            policy.infrastructure_changes.get("new_lanes", 0),
            policy.infrastructure_changes.get("charging_stations", 0) / 100,
        ]
        
        # Add real state context if available
        if state_data:
            features.extend([
                state_data["literacy_rate"] / 100,
                state_data["median_income_inr"] / 50000,
                state_data["urban_percentage"] / 100
            ])
        else:
            features.extend([0.7, 0.7, 0.7])  # Default values
        
        return np.array(features)
