import numpy as np
from typing import Dict, List
import random

class SyntheticDataGenerator:
    """Generate synthetic datasets for demo mode"""
    
    @staticmethod
    def generate_citizen_profiles(n: int = 10000) -> np.ndarray:
        """Generate synthetic citizen behavioral profiles"""
        profiles = np.random.rand(n, 10)
        
        # Add realistic distributions
        profiles[:, 0] = np.random.beta(2, 5, n)  # Income distribution
        profiles[:, 1] = np.random.normal(0.5, 0.15, n)  # Compliance tendency
        profiles[:, 2] = np.random.gamma(2, 2, n) / 10  # Risk aversion
        profiles[:, 3] = np.random.uniform(0, 1, n)  # Location preference
        
        return np.clip(profiles, 0, 1)
    
    @staticmethod
    def generate_infrastructure_data() -> Dict[str, List]:
        """Generate synthetic infrastructure network data"""
        nodes = []
        edges = []
        
        for i in range(100):
            nodes.append({
                "id": i,
                "type": random.choice(["residential", "commercial", "industrial"]),
                "capacity": random.uniform(50, 200),
                "current_load": random.uniform(20, 150),
                "coordinates": [random.uniform(-180, 180), random.uniform(-90, 90)]
            })
        
        # Generate edges (connections)
        for i in range(300):
            source = random.randint(0, 99)
            target = random.randint(0, 99)
            if source != target:
                edges.append({
                    "source": source,
                    "target": target,
                    "weight": random.uniform(0.1, 1.0)
                })
        
        return {"nodes": nodes, "edges": edges}
    
    @staticmethod
    def generate_historical_policies(n: int = 50) -> List[Dict]:
        """Generate historical policy data for training"""
        policies = []
        
        policy_types = ["transportation", "economic", "environmental", "social"]
        
        for i in range(n):
            policy = {
                "id": i,
                "type": random.choice(policy_types),
                "budget": random.uniform(100000, 5000000),
                "duration": random.randint(30, 365),
                "enforcement": random.uniform(0.3, 1.0),
                "outcomes": {
                    "congestion": random.uniform(0.2, 0.8),
                    "satisfaction": random.uniform(0.3, 0.9),
                    "economic_impact": random.uniform(-0.1, 0.3)
                }
            }
            policies.append(policy)
        
        return policies
    
    @staticmethod
    def generate_time_series_data(days: int = 90) -> Dict[str, List]:
        """Generate time series simulation data"""
        timestamps = list(range(days))
        
        # Generate realistic trends
        base_congestion = 0.5
        congestion = [base_congestion + 0.1 * np.sin(t / 7) + np.random.normal(0, 0.05) 
                     for t in timestamps]
        
        base_satisfaction = 0.7
        satisfaction = [base_satisfaction - 0.05 * np.sin(t / 14) + np.random.normal(0, 0.03)
                       for t in timestamps]
        
        return {
            "timestamps": timestamps,
            "congestion": [max(0, min(1, c)) for c in congestion],
            "satisfaction": [max(0, min(1, s)) for s in satisfaction],
            "energy_load": [random.uniform(0.4, 0.8) for _ in timestamps],
            "economic_index": [random.uniform(0.5, 0.9) for _ in timestamps]
        }
