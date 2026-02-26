"""
Comprehensive test for Indian simulation
"""
import asyncio
import httpx
import json

async def test_indian_simulation():
    print("🧪 Testing CivicSim AI - India Edition\n")
    print("=" * 60)
    
    # Test data
    test_cases = [
        {
            "name": "Bengaluru Congestion Pricing",
            "policy_text": "Implement ₹50 congestion charge in Bengaluru during peak hours (8-10 AM, 6-8 PM)",
            "region": {"state": "Karnataka", "city": "Bengaluru"}
        },
        {
            "name": "Mumbai Metro Expansion",
            "policy_text": "Expand Mumbai Metro with ₹500 crore budget, add 3 new lines",
            "region": {"state": "Maharashtra", "city": "Mumbai"}
        },
        {
            "name": "Delhi Odd-Even Scheme",
            "policy_text": "Implement odd-even vehicle scheme in Delhi with ₹100 crore enforcement budget",
            "region": {"state": "Delhi", "city": "New Delhi"}
        }
    ]
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n📝 Test Case {i}: {test_case['name']}")
            print(f"Policy: {test_case['policy_text']}")
            print(f"Region: {test_case['region']['city']}, {test_case['region']['state']}")
            print("-" * 60)
            
            try:
                # Run simulation
                response = await client.post(
                    "http://localhost:8000/india/simulate",
                    json={
                        "policy_text": test_case["policy_text"],
                        "region": test_case["region"],
                        "enable_optimization": True
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    print("✅ Simulation Successful!")
                    print(f"Simulation ID: {result.get('simulation_id')}")
                    
                    # Display results
                    if 'results' in result:
                        results = result['results']
                        
                        # Simulation metrics
                        if 'simulation_metrics' in results:
                            metrics = results['simulation_metrics']
                            print("\n📊 Simulation Metrics:")
                            print(f"  Congestion Score: {metrics.get('congestion_score', 0):.3f}")
                            print(f"  Energy Load: {metrics.get('energy_load', 0):.3f}")
                            print(f"  Dissatisfaction: {metrics.get('dissatisfaction_index', 0):.3f}")
                            print(f"  Economic Stability: {metrics.get('economic_stability', 0):.3f}")
                        
                        # Impact predictions
                        if 'impact_predictions' in results:
                            impact = results['impact_predictions']
                            print("\n🎯 Impact Predictions:")
                            print(f"  Congestion: {impact.get('congestion_score', 0):.3f}")
                            print(f"  Inflation Rate: {impact.get('inflation_rate', 0):.3f}")
                            print(f"  Dissatisfaction: {impact.get('dissatisfaction_index', 0):.3f}")
                            print(f"  Energy Stress: {impact.get('energy_stress', 0):.3f}")
                        
                        # Real India impact
                        if 'real_india_impact' in result:
                            real_impact = result['real_india_impact']
                            print("\n🇮🇳 Real India Impact (Based on actual data):")
                            print(f"  Congestion Reduction: {real_impact.get('congestion_reduction_percent', 0):.2f}%")
                            print(f"  New Congestion Level: {real_impact.get('new_congestion_level', 0):.2f}%")
                            print(f"  Affected Population: {real_impact.get('affected_population', 0):,}")
                            print(f"  Vehicles Affected: {real_impact.get('vehicles_affected', 0):,}")
                            print(f"  Time Saved: {real_impact.get('estimated_time_saved_minutes', 0):.1f} min/trip")
                            print(f"  Fuel Saved: {real_impact.get('fuel_saved_liters_daily', 0):,} L/day")
                            print(f"  CO2 Reduction: {real_impact.get('co2_reduction_tons_yearly', 0):,} tons/year")
                        
                        # Optimization
                        if 'optimization_result' in results:
                            opt = results['optimization_result']
                            print("\n🔧 Optimization Results:")
                            print(f"  Reward Score: {opt.get('reward_score', 0):.3f}")
                            print(f"  Improvement: +{opt.get('improvement_percentage', 0):.1f}%")
                        
                        # Recommendations
                        if 'explanation' in results and 'recommendations' in results['explanation']:
                            recs = results['explanation']['recommendations']
                            print("\n💡 Top Recommendations:")
                            for j, rec in enumerate(recs[:3], 1):
                                print(f"  {j}. {rec}")
                    
                    print(f"\n✅ Test Case {i} PASSED")
                else:
                    print(f"❌ Test Case {i} FAILED: Status {response.status_code}")
                    print(response.text)
            
            except Exception as e:
                print(f"❌ Test Case {i} FAILED: {str(e)}")
            
            print("=" * 60)
    
    print("\n🎉 All tests completed!")

if __name__ == "__main__":
    asyncio.run(test_indian_simulation())
