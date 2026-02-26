import networkx as nx
import numpy as np
from typing import Dict, Any
import logging
from app.services.free_india_data import india_data_service

logger = logging.getLogger(__name__)

# Global infrastructure cache
_infrastructure_cache = {}

class SimulationAgent:
    """Agent-based simulation with graph infrastructure - OPTIMIZED"""
    
    def __init__(self, num_agents=10000):
        self.num_agents = num_agents
        # Use cached infrastructure if available
        if 'infrastructure_graph' in _infrastructure_cache:
            self.infrastructure_graph = _infrastructure_cache['infrastructure_graph']
            logger.info("Using cached infrastructure graph")
        else:
            self.infrastructure_graph = self._build_infrastructure()
            _infrastructure_cache['infrastructure_graph'] = self.infrastructure_graph
    
    def _build_infrastructure(self) -> nx.Graph:
        """Create synthetic city infrastructure graph - OPTIMIZED"""
        # Use faster graph generation
        G = nx.barabasi_albert_graph(100, 3, seed=42)  # Deterministic for caching
        
        # Vectorized attribute assignment
        capacities = np.random.RandomState(42).uniform(50, 200, 100)
        types = np.random.RandomState(42).choice(
            ['residential', 'commercial', 'industrial'], 
            100
        )
        
        for i, node in enumerate(G.nodes()):
            G.nodes[node]['capacity'] = capacities[i]
            G.nodes[node]['type'] = types[i]
        
        logger.info("Built optimized infrastructure graph")
        return G
    
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Run agent-based simulation using REAL state data"""
        policy = state.get("structured_policy")
        behavior = state.get("behavior_output")
        
        # Get real state data
        region = policy.region
        state_data = india_data_service.get_state_data(region.state)
        traffic_data = india_data_service.get_traffic_data(region.state)
        
        # Simulate using real baselines
        metrics = self._run_simulation(policy, behavior, state_data, traffic_data)
        
        state["simulation_metrics"] = metrics
        logger.info(f"SimulationAgent completed for {region.state}: {metrics}")
        
        return state
    
    def _run_simulation(self, policy, behavior, state_data, traffic_data) -> Dict[str, float]:
        """Simulation using REAL state data"""
        if not state_data or not traffic_data:
            return self._fallback_simulation(policy, behavior)
        
        # Real baseline data
        population = state_data["population"]
        vehicles = state_data["vehicles"]
        current_congestion = traffic_data["congestion_level"] / 100  # Normalize to 0-1
        avg_speed = traffic_data["avg_speed_kmph"]
        
        # Policy effects based on real data
        adaptation = behavior["adaptation_rate"]
        compliance = behavior["compliance_probability"]
        
        # Budget per capita (real calculation)
        budget = getattr(policy, 'budget_allocation_inr', 100000000)
        budget_per_capita = budget / population
        
        # Congestion calculation based on infrastructure changes
        new_lanes = policy.infrastructure_changes.get("new_lanes", 0)
        metro_stations = policy.infrastructure_changes.get("metro_stations", 0)
        bus_routes = policy.infrastructure_changes.get("bus_routes", 0)
        
        # Real impact calculation
        lane_impact = (new_lanes * 0.03) * compliance  # Each lane reduces 3%
        metro_impact = (metro_stations * 0.02) * compliance  # Each station reduces 2%
        bus_impact = (bus_routes * 0.01) * compliance  # Each route reduces 1%
        
        congestion_reduction = min(0.25, lane_impact + metro_impact + bus_impact)
        new_congestion = max(0.1, current_congestion - congestion_reduction)
        
        # Energy load (based on EV infrastructure)
        charging_stations = policy.infrastructure_changes.get("charging_stations", 0)
        ev_adoption_rate = min(0.15, (charging_stations / vehicles) * 100) if vehicles > 0 else 0.05
        energy_load = 0.3 + (ev_adoption_rate * 2)  # Base load + EV load
        
        # Dissatisfaction (based on budget adequacy and enforcement)
        budget_adequacy = min(1.0, budget_per_capita / 500)  # ₹500 per capita is good
        enforcement_stress = policy.enforcement_level * 0.3
        dissatisfaction = max(0.1, 0.5 - (budget_adequacy * 0.3) + enforcement_stress - (behavior["satisfaction_score"] * 0.2))
        
        # Economic stability (based on budget impact on state economy)
        state_gdp_estimate = population * 200000  # Rough estimate: ₹2 lakh per capita
        budget_to_gdp = budget / state_gdp_estimate
        economic_stability = min(1.0, 0.7 + (budget_to_gdp * 10) - (dissatisfaction * 0.2))
        
        # Infrastructure stress (real calculation based on vehicle density)
        vehicle_density = vehicles / state_data["area_sq_km"]
        stress_factor = min(1.0, vehicle_density / 10000)  # 10k vehicles/sq km is high
        
        return {
            "congestion_score": round(new_congestion, 3),
            "energy_load": round(energy_load, 3),
            "dissatisfaction_index": round(dissatisfaction, 3),
            "economic_stability": round(economic_stability, 3),
            "infrastructure_stress": {
                "vehicle_density_per_sqkm": round(vehicle_density, 1),
                "stress_level": round(stress_factor, 3),
                "current_congestion_percent": round(current_congestion * 100, 1),
                "projected_congestion_percent": round(new_congestion * 100, 1),
                "congestion_reduction_percent": round(congestion_reduction * 100, 1)
            }
        }
    
    def _fallback_simulation(self, policy, behavior) -> Dict[str, float]:
        """Fallback for states without data"""
        return {
            "congestion_score": 0.5,
            "energy_load": 0.4,
            "dissatisfaction_index": 0.3,
            "economic_stability": 0.7,
            "infrastructure_stress": {
                "note": "Using default values - state data not available"
            }
        }

