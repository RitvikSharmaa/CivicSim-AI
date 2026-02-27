"""Test token tracking in simulation responses"""
import asyncio
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.simulation_engine import SimulationEngine
from app.config import get_settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_token_tracking():
    """Test that token usage is tracked and returned"""
    
    print("=" * 80)
    print("TESTING TOKEN TRACKING IN SIMULATION")
    print("=" * 80)
    print()
    
    # Test policy
    policy_text = "Increase metro rail budget by ₹5000 crore to reduce traffic congestion"
    region = {"state": "Karnataka"}
    
    print(f"Policy: {policy_text}")
    print(f"Region: {region['state']}")
    print()
    
    # Run simulation
    engine = SimulationEngine()
    
    print("Running simulation...")
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
        print(f"Input Tokens:  {token_usage.get('input_tokens', 0)}")
        print(f"Output Tokens: {token_usage.get('output_tokens', 0)}")
        print(f"Total Tokens:  {token_usage.get('total_tokens', 0)}")
        print()
        
        # Check settings
        settings = get_settings()
        if settings.demo_mode:
            print("ℹ️  Note: Running in DEMO_MODE - tokens will be 0")
            print("   Set DEMO_MODE=false in .env to use real LLM and track tokens")
        else:
            print("✅ Running in PRODUCTION mode with real LLM")
            if token_usage.get('total_tokens', 0) > 0:
                print("✅ Tokens successfully tracked from OpenRouter API!")
            else:
                print("⚠️  Tokens are 0 - check OpenRouter API key and response")
    else:
        print("❌ Token usage NOT found in response!")
        print("   This should not happen - check implementation")
    
    print()
    print("=" * 80)
    print("TEST COMPLETE")
    print("=" * 80)
    
    return result

if __name__ == "__main__":
    asyncio.run(test_token_tracking())
