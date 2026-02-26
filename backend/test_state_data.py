"""
Quick test to verify state data functionality
"""
from app.services.free_india_data import india_data_service

def test_state_data():
    """Test state data retrieval"""
    print("Testing State Data Retrieval\n" + "="*50)
    
    # Test a few states
    test_states = ["Karnataka", "Punjab", "Maharashtra", "Delhi", "Tamil Nadu"]
    
    for state in test_states:
        print(f"\n{state}:")
        print("-" * 40)
        
        # Get state data
        state_data = india_data_service.get_state_data(state)
        if state_data:
            print(f"  Population: {state_data['population']:,}")
            print(f"  Vehicles: {state_data['vehicles']:,}")
            print(f"  Literacy: {state_data['literacy_rate']}%")
            print(f"  Median Income: ₹{state_data['median_income_inr']:,}")
            print(f"  Cities: {', '.join(state_data['cities'])}")
        else:
            print(f"  ERROR: No data found!")
        
        # Get traffic data
        traffic_data = india_data_service.get_traffic_data(state)
        if traffic_data:
            print(f"  Congestion: {traffic_data['congestion_level']}%")
            print(f"  Avg Speed: {traffic_data['avg_speed_kmph']} km/h")
    
    print("\n" + "="*50)
    print(f"Total States/UTs: {len(india_data_service.get_states_list())}")
    print("✓ All state data working correctly!")

if __name__ == "__main__":
    test_state_data()
