from typing import Dict, Any, TypedDict
from langgraph.graph import StateGraph, END
from app.agents.policy_agent import PolicyAgent
from app.agents.behavior_agent import BehaviorAgent
from app.agents.simulation_agent import SimulationAgent
from app.agents.impact_agent import ImpactAgent
from app.agents.optimization_agent import OptimizationAgent
from app.agents.explainability_agent import ExplainabilityAgent
import logging

logger = logging.getLogger(__name__)

class SimulationState(TypedDict):
    policy_input: str
    structured_policy: Any
    behavior_output: Dict
    simulation_metrics: Dict
    impact_predictions: Dict
    optimization_result: Dict
    explanation: Dict
    enable_optimization: bool
    region: Dict
    token_usage: Dict

class SimulationEngine:
    """LangGraph-based orchestration of all agents"""
    
    def __init__(self):
        self.policy_agent = PolicyAgent()
        self.behavior_agent = BehaviorAgent()
        self.simulation_agent = SimulationAgent()
        self.impact_agent = ImpactAgent()
        self.optimization_agent = OptimizationAgent()
        self.explainability_agent = ExplainabilityAgent()
        
        self.graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """Build LangGraph workflow"""
        workflow = StateGraph(SimulationState)
        
        # Add nodes
        workflow.add_node("policy", self.policy_agent.process)
        workflow.add_node("behavior", self.behavior_agent.process)
        workflow.add_node("simulation", self.simulation_agent.process)
        workflow.add_node("impact", self.impact_agent.process)
        workflow.add_node("optimization", self.optimization_agent.process)
        workflow.add_node("explainability", self.explainability_agent.process)
        
        # Define edges
        workflow.set_entry_point("policy")
        workflow.add_edge("policy", "behavior")
        workflow.add_edge("behavior", "simulation")
        workflow.add_edge("simulation", "impact")
        
        # Conditional routing for optimization
        workflow.add_conditional_edges(
            "impact",
            self._should_optimize,
            {
                "optimize": "optimization",
                "skip": "explainability"
            }
        )
        
        workflow.add_edge("optimization", "explainability")
        workflow.add_edge("explainability", END)
        
        return workflow.compile()
    
    def _should_optimize(self, state: SimulationState) -> str:
        """Decide whether to run optimization"""
        return "optimize" if state.get("enable_optimization", True) else "skip"
    
    async def run_simulation(
        self, 
        policy_input: str, 
        enable_optimization: bool = True,
        region: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """Execute full simulation pipeline"""
        region_info = f"{region['state']}" if region else "default region"
        logger.info(f"Starting simulation for {region_info}: {policy_input[:50]}...")
        
        initial_state = {
            "policy_input": policy_input,
            "enable_optimization": enable_optimization,
            "region": region
        }
        
        # Run graph
        final_state = await self.graph.ainvoke(initial_state)
        
        logger.info(f"Simulation completed successfully for {region_info}")
        
        return final_state
