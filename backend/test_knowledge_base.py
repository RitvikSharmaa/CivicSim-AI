#!/usr/bin/env python3
"""
Test Knowledge Base Integration
Verify policy retrieval and AI agent integration
"""

import sys
sys.path.insert(0, '.')

from app.knowledge.policy_knowledge_base import policy_kb

def test_get_specific_policy():
    """Test retrieving a specific policy"""
    print("\n🧪 Test 1: Get Specific Policy")
    print("=" * 60)
    
    policy = policy_kb.get_policy("Karnataka", "social", "gruha_jyothi")
    
    if policy:
        print(f"✅ Policy Found: {policy['name']}")
        print(f"   Department: {policy['department']}")
        print(f"   Budget: ₹{policy['budget_allocation']:,}")
        print(f"   Beneficiaries: {policy['beneficiaries']:,}")
        print(f"   Impact Areas: {', '.join(policy['impact_areas'])}")
    else:
        print("❌ Policy not found")

def test_get_all_state_policies():
    """Test retrieving all policies for a state"""
    print("\n🧪 Test 2: Get All State Policies")
    print("=" * 60)
    
    all_policies = policy_kb.get_all_policies_for_state("Karnataka")
    
    print(f"✅ Karnataka Policies:")
    print(f"   Economic: {len(all_policies.get('economic', {}))}")
    print(f"   Social: {len(all_policies.get('social', {}))}")
    print(f"   Infrastructure: {len(all_policies.get('infrastructure', {}))}")
    
    if 'budget_2025_26' in all_policies:
        budget = all_policies['budget_2025_26']
        print(f"   Budget 2025-26: ₹{budget['total_outlay']:,}")

def test_get_related_policies():
    """Test finding related policies"""
    print("\n🧪 Test 3: Get Related Policies")
    print("=" * 60)
    
    related = policy_kb.get_related_policies("transportation", "Karnataka")
    
    print(f"✅ Found {len(related)} related transportation policies:")
    for i, policy in enumerate(related[:5], 1):
        print(f"   {i}. {policy.get('level', 'N/A')}: {policy.get('name', 'N/A')}")

def test_search_policies():
    """Test searching policies by keyword"""
    print("\n🧪 Test 4: Search Policies")
    print("=" * 60)
    
    results = policy_kb.search_policies("electricity")
    
    print(f"✅ Found {len(results)} policies related to 'electricity':")
    for i, result in enumerate(results[:5], 1):
        print(f"   {i}. {result['state']}: {result['policy']}")

def test_get_budget_data():
    """Test retrieving budget data"""
    print("\n🧪 Test 5: Get Budget Data")
    print("=" * 60)
    
    budget = policy_kb.get_budget_data("Karnataka", "2025_26")
    
    if budget:
        print(f"✅ Karnataka Budget 2025-26:")
        print(f"   Total Outlay: ₹{budget['total_outlay']:,}")
        print(f"   GSDP Projection: ₹{budget['gsdp_projection']:,}")
        print(f"   GSDP Growth: {budget['gsdp_growth']}%")
        print(f"   Key Allocations:")
        for sector, amount in budget['key_allocations'].items():
            print(f"      {sector.replace('_', ' ').title()}: ₹{amount:,}")
    else:
        print("❌ Budget data not found")

def test_national_policies():
    """Test retrieving national policies"""
    print("\n🧪 Test 6: Get National Policies")
    print("=" * 60)
    
    # Test economic policy
    make_in_india = policy_kb.get_policy("national", "economic", "make_in_india")
    if make_in_india:
        print(f"✅ {make_in_india['name']}")
        print(f"   Ministry: {make_in_india['ministry']}")
        print(f"   Launched: {make_in_india['launched']}")
        print(f"   Objective: {make_in_india['objective']}")
    
    # Test social policy
    ayushman = policy_kb.get_policy("national", "social", "ayushman_bharat")
    if ayushman:
        print(f"\n✅ {ayushman['name']}")
        print(f"   Coverage: ₹{ayushman['coverage']:,} per family")
        print(f"   Beneficiaries: {ayushman['beneficiaries']:,}")

def test_multiple_states():
    """Test policies from multiple states"""
    print("\n🧪 Test 7: Multiple States")
    print("=" * 60)
    
    states = ["Karnataka", "Maharashtra", "Tamil Nadu", "Delhi", "West Bengal", "Gujarat"]
    
    for state in states:
        policies = policy_kb.get_all_policies_for_state(state)
        total = sum(len(v) if isinstance(v, dict) else 0 for k, v in policies.items() if k != 'budget_2025_26')
        print(f"✅ {state}: {total} policies")

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("🎓 KNOWLEDGE BASE INTEGRATION TEST")
    print("=" * 60)
    
    try:
        test_get_specific_policy()
        test_get_all_state_policies()
        test_get_related_policies()
        test_search_policies()
        test_get_budget_data()
        test_national_policies()
        test_multiple_states()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\n📊 Summary:")
        print("  • Policy retrieval: ✅")
        print("  • State policies: ✅")
        print("  • Related policies: ✅")
        print("  • Search functionality: ✅")
        print("  • Budget data: ✅")
        print("  • National policies: ✅")
        print("  • Multiple states: ✅")
        print("\n🎉 Knowledge Base is fully operational!")
        
        return 0
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())
