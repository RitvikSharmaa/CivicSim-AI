"""
Quick test script for the simulation engine
Run: python test_simulation.py
"""

import asyncio
from app.services.simulation_engine import SimulationEngine

async def test_simulation():
    print("🧪 Testing CivicSim AI Simulation Engine\n")
    
    engine = SimulationEngine()
    
    test_policy = """
    Implement a congestion pricing policy in the downtown area.
    Charge $5 during peak hours (7-9 AM, 5-7 PM).
    Use revenue to fund public transportation improvements.
    Provide 50% discount for low-income residents.
    """
    
    print(f"📝 Policy Input:\n{test_policy}\n")
    print("⚙️  Running simulation...\n")
    
    result = await engine.run_simulation(
        policy_input=test_policy,
        enable_optimization=True
    )
    
    print("✅ Simulation Complete!\n")
    print("=" * 60)
    
    # Display results
    print("\n📊 SIMULATION METRICS:")
    metrics = result.get("simulation_metrics", {})
    print(f"  Congestion Score: {metrics.get('congestion_score', 0):.3f}")
    print(f"  Energy Load: {metrics.get('energy_load', 0):.3f}")
    print(f"  Dissatisfaction: {metrics.get('dissatisfaction_index', 0):.3f}")
    print(f"  Economic Stability: {metrics.get('economic_stability', 0):.3f}")
    
    print("\n🎯 IMPACT PREDICTIONS:")
    predictions = result.get("impact_predictions", {})
    print(f"  Congestion: {predictions.get('congestion_score', 0):.3f}")
    print(f"  Inflation Rate: {predictions.get('inflation_rate', 0):.3f}")
    print(f"  Dissatisfaction: {predictions.get('dissatisfaction_index', 0):.3f}")
    print(f"  Energy Stress: {predictions.get('energy_stress', 0):.3f}")
    
    if result.get("optimization_result"):
        print("\n🔧 OPTIMIZATION RESULTS:")
        opt = result["optimization_result"]
        print(f"  Reward Score: {opt.get('reward_score', 0):.3f}")
        print(f"  Improvement: +{opt.get('improvement_percentage', 0):.1f}%")
    
    if result.get("explanation"):
        print("\n💡 TOP RECOMMENDATIONS:")
        recs = result["explanation"].get("recommendations", [])
        for i, rec in enumerate(recs[:3], 1):
            print(f"  {i}. {rec}")
    
    print("\n" + "=" * 60)
    print("✨ Test completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_simulation())
