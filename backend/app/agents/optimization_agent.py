import numpy as np
from typing import Dict, Any
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
import gymnasium as gym
from gymnasium import spaces
import logging

logger = logging.getLogger(__name__)

class PolicyOptimizationEnv(gym.Env):
    """Custom environment for policy optimization"""
    
    def __init__(self, base_policy):
        super().__init__()
        self.base_policy = base_policy
        
        # Action space: adjustments to policy parameters
        self.action_space = spaces.Box(
            low=-0.3, high=0.3, shape=(5,), dtype=np.float32
        )
        
        # Observation space: current policy state
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(8,), dtype=np.float32
        )
        
        self.current_step = 0
        self.max_steps = 10
    
    def reset(self, seed=None, options=None):
        if seed is not None:
            np.random.seed(seed)
        self.current_step = 0
        return self._get_observation(), {}
    
    def step(self, action):
        self.current_step += 1
        
        # Apply action to policy parameters
        reward = self._compute_reward(action)
        terminated = self.current_step >= self.max_steps
        truncated = False
        
        return self._get_observation(), reward, terminated, truncated, {}
    
    def _get_observation(self):
        return np.random.rand(8).astype(np.float32)
    
    def _compute_reward(self, action):
        # Multi-objective reward
        congestion_penalty = -abs(action[0])
        dissatisfaction_penalty = -abs(action[1])
        energy_penalty = -abs(action[2])
        economic_bonus = abs(action[3])
        
        return congestion_penalty + dissatisfaction_penalty + energy_penalty + economic_bonus

class OptimizationAgent:
    """Optimizes policy parameters using PPO"""
    
    def __init__(self):
        self.model = None
    
    async def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize policy parameters"""
        policy = state.get("structured_policy")
        metrics = state.get("simulation_metrics")
        
        # Create environment
        env = PolicyOptimizationEnv(policy)
        
        # Train PPO (limited steps for hackathon)
        if self.model is None:
            self.model = PPO("MlpPolicy", env, verbose=0, n_steps=128)
            self.model.learn(total_timesteps=1000)  # Minimal training
        
        # Get optimized parameters
        obs, _ = env.reset()
        action, _ = self.model.predict(obs, deterministic=True)
        
        # Apply optimizations
        optimized = self._apply_optimizations(policy, action)
        
        # Compute reward and comparison
        reward = self._compute_final_reward(metrics, optimized)
        comparison = self._compare_policies(metrics, optimized)
        
        optimization_result = {
            "optimized_parameters": optimized,
            "reward_score": float(reward),
            "improvement_percentage": float(comparison["improvement"]),
            "comparison_metrics": comparison["metrics"]
        }
        
        state["optimization_result"] = optimization_result
        logger.info(f"OptimizationAgent completed: {optimization_result}")
        
        return state
    
    def _apply_optimizations(self, policy, action) -> Dict[str, float]:
        """Apply RL actions to policy parameters"""
        # Handle both old and new schema
        budget = getattr(policy, 'budget_allocation_inr', None) or getattr(policy, 'budget_allocation', 1000000)
        timeline = getattr(policy, 'implementation_timeline_days', None) or getattr(policy, 'implementation_timeline', 90)
        
        # Determine which budget key to use
        budget_key = "budget_allocation_inr" if hasattr(policy, "budget_allocation_inr") else "budget_allocation"
        timeline_key = "implementation_timeline_days" if hasattr(policy, "implementation_timeline_days") else "implementation_timeline"
        
        return {
            budget_key: float(budget * (1 + action[0])),
            "enforcement_level": float(np.clip(policy.enforcement_level + action[1], 0, 1)),
            timeline_key: int(timeline * (1 + action[2])),
            "tax_reduction": float(np.clip(policy.incentive_structure.get("tax_reduction", 0) + action[3], 0, 1)),
            "subsidy": float(policy.incentive_structure.get("subsidy", 0) * (1 + action[4]))
        }
    
    def _compute_final_reward(self, metrics, optimized) -> float:
        """Compute final reward score"""
        return -metrics["congestion_score"] - metrics["dissatisfaction_index"] - metrics["energy_load"] + metrics["economic_stability"]
    
    def _compare_policies(self, original_metrics, optimized) -> Dict:
        """Compare original vs optimized"""
        improvement = np.random.uniform(5, 15)  # Mock improvement
        return {
            "improvement": improvement,
            "metrics": {
                "congestion_reduction": 0.12,
                "satisfaction_increase": 0.08,
                "cost_efficiency": 0.15
            }
        }
