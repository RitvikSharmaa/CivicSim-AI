"""Test token tracking with real LLM (DEMO_MODE=false)"""
import asyncio
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Override DEMO_MODE for this test
os.environ["DEMO_MODE"] = "false"

from app.services.simulation_engine import SimulationEngine
from app.config import get_settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_token_tracking_production():
    """Test that token usage is tracked with real LLM"""
    
    print("=" * 80)
    print("TESTING TOKEN TRACKING WITH REAL LLM (PRODUCTION MODE)")
    print("=" * 80)
    print()
    
    # Verify settings
    settings = get_settings()
    print(f"DEMO_MODE: {settings.demo_mode}")
    print(f"OpenRouter Model: {settings.openrouter_model}")
    print(f"API Key: {settings.openrouter_api_key[:20]}...")
    print()
    
    # Test policy
    policy_text = "Increase metro rail budget by ₹5000 crore to reduce traffic congestion"
    region = {"state": "Karnataka"}
    
    print(f"Policy: {policy_text}")
    print(f"Region: {region['state']}")
    print()
    
    # Run simulation
    engine = SimulationEngine()
    
    print("Running simulation with REAL LLM...")
    print("(This will make an actual API call to OpenRouter)")
    print()
    
    try:
        result = await engine.run_simulation(
            policy_input=policy_text,
            enable_optimization=True,
            region=region
        )
        
        print()
        print("=" * 80)
        print("RESULTS")
        print("=" * 80)
        print()
        
        # Check if token_usage exists
        if "token_usage" in result:
            token_usage = result["token_usage"]
            print("✅ Token usage tracking WORKING!")
            print()
            print(f"📊 Input Tokens:  {token_usage.get('input_tokens', 0)}")
            print(f"📊 Output Tokens: {token_usage.get('output_tokens', 0)}")
            print(f"📊 Total Tokens:  {token_usage.get('total_tokens', 0)}")
            print()
            
            if token_usage.get('total_tokens', 0) > 0:
                print("✅ SUCCESS! Tokens successfully tracked from OpenRouter API!")
                print()
                print("Token breakdown:")
                print(f"  - System prompt + user input: {token_usage.get('input_tokens', 0)} tokens")
                print(f"  - LLM response: {token_usage.get('output_tokens', 0)} tokens")
                print(f"  - Total cost: {token_usage.get('total_tokens', 0)} tokens")
            else:
                print("⚠️  Tokens are 0 - LLM might have failed, check logs above")
        else:
            print("❌ Token usage NOT found in response!")
        
        print()
        print("=" * 80)
        print("TEST COMPLETE")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_token_tracking_production())
