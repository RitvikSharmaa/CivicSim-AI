# 🧪 Manual Testing Guide - Knowledge Base

## 🌐 Access URLs

### Main Application
- **Frontend**: http://localhost:3001 (or http://localhost:3000)
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Knowledge Base API**: http://localhost:8000/knowledge

---

## 📋 Quick Test - Start Here!

### 1. Test Knowledge Base Status
**URL**: http://localhost:8000/knowledge

**What to expect**:
```json
{
  "name": "Indian Policy Knowledge Base",
  "version": "1.0.0",
  "status": "operational",
  "coverage": {
    "national_policies": "20+",
    "state_policies": "40+ (6 states)",
    "total_policies": "60+",
    "states_covered": ["Karnataka", "Maharashtra", "Tamil Nadu", "Delhi", "West Bengal", "Gujarat"]
  }
}
```

### 2. Quick Test All Features
**URL**: http://localhost:8000/knowledge/test

**What to expect**:
```json
{
  "status": "Knowledge Base Test Results",
  "tests": {
    "get_policy": "✅ Pass",
    "search": "✅ Pass (2 results)",
    "state_policies": "✅ Pass (7 categories)",
    "budget": "✅ Pass"
  },
  "overall": "✅ All tests passed"
}
```

---

## 🎯 Detailed Testing

### Test 1: List All States with Policies
**URL**: http://localhost:8000/knowledge/states

**What you'll see**:
- List of 6 states
- Policy count for each state
- Budget availability
- Policy categories

**Example Response**:
```json
{
  "total_states": 6,
  "states": [
    {
      "state": "Karnataka",
      "policy_count": 6,
      "has_budget": true,
      "categories": ["economic", "social", "infrastructure", "budget_2025_26"]
    },
    ...
  ]
}
```

---

### Test 2: Get Karnataka's Gruha Jyothi Scheme
**URL**: http://localhost:8000/knowledge/policy/Karnataka/social/gruha_jyothi

**What you'll see**:
```json
{
  "state": "Karnataka",
  "category": "social",
  "policy_name": "gruha_jyothi",
  "policy": {
    "name": "Gruha Jyothi (Free Electricity)",
    "department": "Energy Department",
    "launched": "2023-06-01",
    "objective": "Provide 200 units free electricity to households",
    "beneficiaries": 15000000,
    "budget_allocation": 120000000000,
    "impact_areas": ["Household savings", "Energy access", "Quality of life"]
  }
}
```

**Key Points**:
- ✅ Budget: ₹12,000 crore (120000000000)
- ✅ Beneficiaries: 1.5 crore households
- ✅ Real government scheme data

---

### Test 3: Get All Karnataka Policies
**URL**: http://localhost:8000/knowledge/state/Karnataka

**What you'll see**:
- Economic policies (2)
- Social policies (3) - Gruha Jyothi, Gruha Lakshmi, Anna Bhagya
- Infrastructure policies (1)
- Budget 2025-26 data

**Example Response**:
```json
{
  "state": "Karnataka",
  "summary": {
    "economic": 2,
    "social": 3,
    "infrastructure": 1,
    "budget_2025_26": "Available"
  },
  "policies": {
    "economic": {...},
    "social": {...},
    "infrastructure": {...},
    "budget_2025_26": {...}
  }
}
```

---

### Test 4: Search for "Electricity" Policies
**URL**: http://localhost:8000/knowledge/search?q=electricity

**What you'll see**:
```json
{
  "query": "electricity",
  "total_results": 2,
  "results": [
    {
      "state": "Karnataka",
      "category": "social",
      "policy": "gruha_jyothi",
      "data": {...}
    },
    {
      "state": "Delhi",
      "category": "social",
      "policy": "delhi_free_electricity",
      "data": {...}
    }
  ]
}
```

**Try other searches**:
- `?q=metro` - Find metro projects
- `q=women` - Find women welfare schemes
- `?q=education` - Find education policies
- `?q=health` - Find healthcare schemes

---

### Test 5: Get Related Transportation Policies
**URL**: http://localhost:8000/knowledge/related?type=transportation&state=Karnataka

**What you'll see**:
- Related transportation policies
- National and state level
- Infrastructure projects

---

### Test 6: Get Karnataka Budget 2025-26
**URL**: http://localhost:8000/knowledge/budget/Karnataka

**What you'll see**:
```json
{
  "state": "Karnataka",
  "year": "2025_26",
  "budget": {
    "total_outlay": 408647000000,
    "gsdp_projection": 3070103000000,
    "gsdp_growth": 7.0,
    "key_allocations": {
      "guarantee_schemes": 560000000000,
      "infrastructure": 800000000000,
      "education": 450000000000,
      "health": 350000000000,
      "agriculture": 250000000000
    }
  }
}
```

**Key Points**:
- ✅ Total Budget: ₹4.09 lakh crore
- ✅ GSDP: ₹30.70 lakh crore
- ✅ Growth: 7%
- ✅ Real budget data from Karnataka Budget 2025-26

---

### Test 7: Get National Economic Policies
**URL**: http://localhost:8000/knowledge/national/economic

**What you'll see**:
```json
{
  "category": "economic",
  "total_policies": 3,
  "policies": {
    "make_in_india": {...},
    "atmanirbhar_bharat": {...},
    "digital_india": {...}
  }
}
```

**Try other categories**:
- `/national/social` - Social welfare policies
- `/national/infrastructure` - Infrastructure projects
- `/national/agriculture` - Agriculture schemes
- `/national/education` - Education policies

---

### Test 8: Get All Government Schemes
**URL**: http://localhost:8000/knowledge/schemes

**What you'll see**:
```json
{
  "central_sector": [
    "PM-KISAN",
    "Ayushman Bharat",
    "PM Jan Dhan Yojana",
    "Digital India",
    "Make in India",
    ...
  ],
  "centrally_sponsored": [
    "MGNREGA",
    "National Health Mission",
    "Samagra Shiksha",
    ...
  ],
  "state_schemes": {
    "Karnataka": ["Gruha Jyothi", "Gruha Lakshmi", ...],
    "Maharashtra": [...],
    ...
  }
}
```

---

### Test 9: Get Economic Indicators
**URL**: http://localhost:8000/knowledge/economic-data

**What you'll see**:
```json
{
  "national": {
    "gdp_growth": 7.3,
    "inflation_rate": 5.2,
    "unemployment_rate": 7.8,
    "fiscal_deficit": 5.9,
    "current_account_deficit": 1.2
  },
  "state_wise": {
    "Karnataka": {
      "gsdp": 3070103000000,
      "gsdp_growth": 7.0,
      "per_capita_income": 364000,
      "unemployment_rate": 2.9
    },
    ...
  }
}
```

---

## 🎨 Test in Browser

### Option 1: Use API Documentation (Easiest)
1. Open: http://localhost:8000/docs
2. Scroll to "knowledge" section
3. Click on any endpoint
4. Click "Try it out"
5. Fill parameters (if needed)
6. Click "Execute"
7. See response below

### Option 2: Direct Browser URLs
Just paste these URLs in your browser:

**Quick Tests**:
- http://localhost:8000/knowledge
- http://localhost:8000/knowledge/test
- http://localhost:8000/knowledge/states

**Get Policies**:
- http://localhost:8000/knowledge/state/Karnataka
- http://localhost:8000/knowledge/state/Maharashtra
- http://localhost:8000/knowledge/state/Delhi

**Search**:
- http://localhost:8000/knowledge/search?q=electricity
- http://localhost:8000/knowledge/search?q=metro
- http://localhost:8000/knowledge/search?q=women

**Budget Data**:
- http://localhost:8000/knowledge/budget/Karnataka
- http://localhost:8000/knowledge/budget/Maharashtra

**National Policies**:
- http://localhost:8000/knowledge/national/economic
- http://localhost:8000/knowledge/national/social
- http://localhost:8000/knowledge/national/infrastructure

**Schemes & Data**:
- http://localhost:8000/knowledge/schemes
- http://localhost:8000/knowledge/economic-data

---

## 🧪 Test with Simulation

### Test Knowledge Base Integration in Simulation

1. **Open Frontend**: http://localhost:3001

2. **Launch Simulator**: Click "Start Simulation"

3. **Select State**: Choose "Karnataka"

4. **Enter Policy**: 
   ```
   Increase metro rail budget by ₹5000 crore to reduce traffic congestion
   ```

5. **Run Simulation**: Click "Run Simulation"

6. **Check Results**: Look for:
   - ✅ Related policies mentioned
   - ✅ Similar schemes cited
   - ✅ Budget comparisons
   - ✅ Evidence-based predictions
   - ✅ Source citations

**What to expect in results**:
- References to Namma Metro expansion
- Comparison with Delhi/Mumbai metro projects
- Karnataka's infrastructure budget mentioned
- Related transportation policies cited
- Evidence from government sources

---

## 📊 Expected Results Summary

### All States Available (6)
✅ Karnataka - 6 policies + Budget  
✅ Maharashtra - 4 policies  
✅ Tamil Nadu - 3 policies  
✅ Delhi - 4 policies  
✅ West Bengal - 2 policies  
✅ Gujarat - 2 policies  

### National Policies (20+)
✅ Economic: 3 policies  
✅ Social: 3 policies  
✅ Infrastructure: 3 policies  
✅ Agriculture: 2 policies  
✅ Education: 2 policies  

### Search Functionality
✅ "electricity" → 2 results  
✅ "metro" → Multiple results  
✅ "women" → Multiple results  
✅ "education" → Multiple results  

### Budget Data
✅ Karnataka: ₹4.09 lakh crore  
✅ GSDP projections available  
✅ Sector allocations detailed  

---

## 🐛 Troubleshooting

### Issue: 404 Not Found
**Solution**: Check if backend is running on http://localhost:8000

### Issue: Empty Results
**Solution**: 
- Check spelling of state name (case-sensitive)
- Try different search terms
- Verify endpoint URL

### Issue: Server Error
**Solution**:
- Check backend logs
- Restart backend server
- Run test: `python backend/test_knowledge_base.py`

---

## ✅ Testing Checklist

Use this checklist to verify everything works:

- [ ] Knowledge base info loads: `/knowledge`
- [ ] Quick test passes: `/knowledge/test`
- [ ] States list shows 6 states: `/knowledge/states`
- [ ] Karnataka policies load: `/knowledge/state/Karnataka`
- [ ] Gruha Jyothi details show: `/knowledge/policy/Karnataka/social/gruha_jyothi`
- [ ] Search for "electricity" finds 2 results: `/knowledge/search?q=electricity`
- [ ] Karnataka budget loads: `/knowledge/budget/Karnataka`
- [ ] National economic policies show: `/knowledge/national/economic`
- [ ] Schemes list loads: `/knowledge/schemes`
- [ ] Economic data shows: `/knowledge/economic-data`
- [ ] API docs accessible: `/docs`
- [ ] Simulation shows related policies

---

## 🎉 Success Criteria

If you can access all these URLs and see proper data, the knowledge base is working perfectly:

1. ✅ http://localhost:8000/knowledge/test shows all tests passing
2. ✅ http://localhost:8000/knowledge/states shows 6 states
3. ✅ http://localhost:8000/knowledge/state/Karnataka shows policies
4. ✅ http://localhost:8000/knowledge/search?q=electricity finds results
5. ✅ Simulation references related policies

---

## 📞 Quick Reference

### Main URLs
- **API Docs**: http://localhost:8000/docs
- **Knowledge Base**: http://localhost:8000/knowledge
- **Quick Test**: http://localhost:8000/knowledge/test
- **Frontend**: http://localhost:3001

### Key Endpoints
- `/knowledge` - Info
- `/knowledge/test` - Quick test
- `/knowledge/states` - List states
- `/knowledge/state/{state}` - State policies
- `/knowledge/search?q={query}` - Search
- `/knowledge/budget/{state}` - Budget data

---

**Start Testing**: http://localhost:8000/knowledge/test

**Full API Docs**: http://localhost:8000/docs

**Happy Testing!** 🎉
