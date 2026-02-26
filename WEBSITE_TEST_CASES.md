# 🧪 Website Test Cases - CivicSim AI Policy Sandbox

## 🌐 Access Information

### URLs
- **Frontend**: http://localhost:3001 (or http://localhost:3000)
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Knowledge Base API**: http://localhost:8000/knowledge

### Prerequisites
- ✅ Backend server running on port 8000
- ✅ Frontend server running on port 3001
- ✅ MongoDB connected
- ✅ ML models trained and loaded

---

## 📋 Test Categories

1. [Homepage & Navigation](#1-homepage--navigation)
2. [State Selection & Data Display](#2-state-selection--data-display)
3. [Policy Simulation](#3-policy-simulation)
4. [Knowledge Base Integration](#4-knowledge-base-integration)
5. [Interactive Maps](#5-interactive-maps)
6. [Performance & Responsiveness](#6-performance--responsiveness)
7. [API Endpoints](#7-api-endpoints)

---

## 1. Homepage & Navigation

### Test 1.1: Homepage Loads Successfully
**Steps**:
1. Open http://localhost:3001
2. Wait for page to load

**Expected Results**:
- ✅ Page loads within 2 seconds
- ✅ Logo visible in header
- ✅ "CivicSim AI" title displayed
- ✅ Hero section shows "36 States & UTs" and "37 Cities"
- ✅ Navigation menu visible
- ✅ Footer with copyright information

**Status**: [ ] Pass [ ] Fail

---

### Test 1.2: Hero Section Content
**Steps**:
1. Scroll to hero section
2. Read the content

**Expected Results**:
- ✅ Headline: "Simulate Policy Impact Across India"
- ✅ Subheadline mentions AI-powered predictions
- ✅ Statistics show: "36 States & UTs" and "37 Cities"
- ✅ "Start Simulation" button visible
- ✅ "View All States" button visible
- ✅ Indian flag colors (saffron, white, green) in design

**Status**: [ ] Pass [ ] Fail

---

### Test 1.3: Navigation Buttons Work
**Steps**:
1. Click "Start Simulation" button in hero section
2. Observe page behavior
3. Scroll back to top
4. Click "View All States" button

**Expected Results**:
- ✅ "Start Simulation" scrolls to simulator section
- ✅ Smooth scrolling animation
- ✅ "View All States" scrolls to states showcase
- ✅ No page reload or errors

**Status**: [ ] Pass [ ] Fail

---

## 2. State Selection & Data Display

### Test 2.1: States Showcase Displays All States
**Steps**:
1. Scroll to "Explore All Indian States" section
2. Count the state cards displayed

**Expected Results**:
- ✅ Section title: "Explore All Indian States"
- ✅ Search bar visible
- ✅ Region filter buttons (All, North, South, East, West, Northeast, Central)
- ✅ 36 state/UT cards displayed initially
- ✅ Each card shows: State name, Capital, Population, Region badge

**Status**: [ ] Pass [ ] Fail

---

### Test 2.2: Search Functionality
**Steps**:
1. Click on search bar
2. Type "Karnataka"
3. Observe results
4. Clear search
5. Type "Delhi"

**Expected Results**:
- ✅ Search filters states in real-time
- ✅ "Karnataka" shows only Karnataka card
- ✅ "Delhi" shows only Delhi card
- ✅ Search is case-insensitive
- ✅ Partial matches work (e.g., "Karn" shows Karnataka)

**Status**: [ ] Pass [ ] Fail

---

### Test 2.3: Region Filter Works
**Steps**:
1. Click "South" region filter
2. Observe displayed states
3. Click "North" region filter
4. Click "All" to reset

**Expected Results**:
- ✅ "South" shows: Karnataka, Tamil Nadu, Andhra Pradesh, Telangana, Kerala
- ✅ "North" shows: Delhi, Punjab, Haryana, Himachal Pradesh, Uttarakhand, J&K, Ladakh
- ✅ Active filter button highlighted
- ✅ "All" shows all 36 states/UTs
- ✅ State count updates correctly

**Status**: [ ] Pass [ ] Fail

---

### Test 2.4: View Data Button - Expandable Cards
**Steps**:
1. Find Karnataka card
2. Click "View Data" button
3. Observe card expansion
4. Click "View Data" again

**Expected Results**:
- ✅ Card expands smoothly
- ✅ Shows detailed data: Population, GDP, Literacy Rate, Unemployment
- ✅ "Simulate for Karnataka" button appears
- ✅ Clicking again collapses the card
- ✅ Only one card expanded at a time
- ✅ No popup or modal

**Status**: [ ] Pass [ ] Fail

---

### Test 2.5: Multiple States Data View
**Steps**:
1. Click "View Data" on Karnataka
2. Click "View Data" on Maharashtra
3. Observe behavior

**Expected Results**:
- ✅ Karnataka card collapses when Maharashtra is clicked
- ✅ Only Maharashtra card is expanded
- ✅ Smooth transition animation
- ✅ No layout issues

**Status**: [ ] Pass [ ] Fail

---

### Test 2.6: Simulate Button in Expanded Card
**Steps**:
1. Click "View Data" on Karnataka
2. Click "Simulate for Karnataka" button
3. Observe page behavior

**Expected Results**:
- ✅ Page scrolls to simulator section
- ✅ State selector shows "Karnataka"
- ✅ City selector shows "Bengaluru"
- ✅ Smooth scrolling animation
- ✅ Ready to enter policy

**Status**: [ ] Pass [ ] Fail

---

## 3. Policy Simulation

### Test 3.1: State and City Selection
**Steps**:
1. Scroll to simulator section
2. Click state dropdown
3. Select "Karnataka"
4. Click city dropdown
5. Select "Bengaluru"

**Expected Results**:
- ✅ State dropdown shows all 36 states/UTs
- ✅ City dropdown updates based on state
- ✅ Bengaluru appears for Karnataka
- ✅ Mumbai appears for Maharashtra
- ✅ Selection persists

**Status**: [ ] Pass [ ] Fail

---

### Test 3.2: Policy Input - Transportation
**Steps**:
1. Select State: Karnataka, City: Bengaluru
2. Enter policy: "Increase metro rail budget by ₹5000 crore to reduce traffic congestion"
3. Click "Run Simulation"
4. Wait for results

**Expected Results**:
- ✅ Simulation starts (loading indicator)
- ✅ Results appear within 5-10 seconds
- ✅ Shows impact metrics (Traffic, Pollution, Economy)
- ✅ Shows related policies from knowledge base
- ✅ Charts/graphs display data
- ✅ Explanation panel shows reasoning

**Status**: [ ] Pass [ ] Fail

---

### Test 3.3: Policy Input - Social Welfare
**Steps**:
1. Select State: Karnataka, City: Bengaluru
2. Enter policy: "Provide ₹2000 monthly assistance to women heads of families"
3. Click "Run Simulation"

**Expected Results**:
- ✅ Simulation completes successfully
- ✅ Shows impact on: Household income, Women empowerment, Economy
- ✅ References Gruha Lakshmi scheme (existing Karnataka scheme)
- ✅ Compares with similar schemes in other states
- ✅ Shows budget implications

**Status**: [ ] Pass [ ] Fail

---

### Test 3.4: Policy Input - Infrastructure
**Steps**:
1. Select State: Maharashtra, City: Mumbai
2. Enter policy: "Build 100 km of new metro lines with ₹50,000 crore investment"
3. Click "Run Simulation"

**Expected Results**:
- ✅ Simulation completes
- ✅ Shows impact on: Urban mobility, Traffic congestion, Employment
- ✅ References Mumbai Metro expansion plans
- ✅ Compares with Bengaluru/Delhi metro projects
- ✅ Shows timeline and phasing

**Status**: [ ] Pass [ ] Fail

---

### Test 3.5: Policy Input - Education
**Steps**:
1. Select State: Delhi, City: New Delhi
2. Enter policy: "Increase education budget by ₹5000 crore for government schools"
3. Click "Run Simulation"

**Expected Results**:
- ✅ Simulation completes
- ✅ Shows impact on: Learning outcomes, Infrastructure, Teacher quality
- ✅ References Delhi Education Model
- ✅ Shows enrollment and quality improvements
- ✅ Budget breakdown displayed

**Status**: [ ] Pass [ ] Fail

---

### Test 3.6: Policy Input - Healthcare
**Steps**:
1. Select State: Tamil Nadu, City: Chennai
2. Enter policy: "Expand free healthcare coverage to ₹5 lakh per family"
3. Click "Run Simulation"

**Expected Results**:
- ✅ Simulation completes
- ✅ Shows impact on: Healthcare access, Out-of-pocket expenses, Hospital admissions
- ✅ References Ayushman Bharat and state schemes
- ✅ Shows beneficiary coverage
- ✅ Financial implications clear

**Status**: [ ] Pass [ ] Fail

---

### Test 3.7: Multiple Simulations
**Steps**:
1. Run simulation for Karnataka
2. Change state to Maharashtra
3. Run another simulation
4. Compare results

**Expected Results**:
- ✅ Previous results cleared
- ✅ New simulation runs successfully
- ✅ Results specific to Maharashtra
- ✅ No data mixing between simulations
- ✅ Can run unlimited simulations

**Status**: [ ] Pass [ ] Fail

---

## 4. Knowledge Base Integration

### Test 4.1: Related Policies Displayed
**Steps**:
1. Run simulation: "Increase metro budget by ₹5000 crore" for Karnataka
2. Check results for related policies section

**Expected Results**:
- ✅ Shows "Related Policies" section
- ✅ Lists Namma Metro Phase 2 & 3
- ✅ Lists other state metro projects (Mumbai, Delhi)
- ✅ Shows national infrastructure policies
- ✅ Each policy has: Name, Budget, Impact areas

**Status**: [ ] Pass [ ] Fail

---

### Test 4.2: Policy Citations and Sources
**Steps**:
1. Run any simulation
2. Look for policy references in explanation

**Expected Results**:
- ✅ Mentions specific government schemes
- ✅ Cites budget documents
- ✅ References official data sources
- ✅ Shows policy launch dates
- ✅ Mentions implementing departments

**Status**: [ ] Pass [ ] Fail

---

### Test 4.3: Budget Comparisons
**Steps**:
1. Run simulation with budget component
2. Check if existing budget data is referenced

**Expected Results**:
- ✅ Compares with state budget allocations
- ✅ Shows percentage of total budget
- ✅ References Karnataka Budget 2025-26 (if Karnataka)
- ✅ Shows sector-wise allocations
- ✅ Fiscal impact mentioned

**Status**: [ ] Pass [ ] Fail

---

### Test 4.4: Similar Schemes Across States
**Steps**:
1. Run simulation for women welfare scheme in Karnataka
2. Check for references to similar schemes

**Expected Results**:
- ✅ Mentions Gruha Lakshmi (Karnataka)
- ✅ Mentions Lakshmir Bhandar (West Bengal)
- ✅ Mentions Kalaignar Magalir Urimai Thogai (Tamil Nadu)
- ✅ Shows comparison of amounts and beneficiaries
- ✅ Highlights best practices

**Status**: [ ] Pass [ ] Fail

---

## 5. Interactive Maps

### Test 5.1: Map Loads Successfully
**Steps**:
1. Scroll to map section (if visible)
2. Wait for map to load

**Expected Results**:
- ✅ OpenStreetMap loads
- ✅ India map centered
- ✅ All states visible
- ✅ Zoom controls work
- ✅ Pan/drag works

**Status**: [ ] Pass [ ] Fail

---

### Test 5.2: State Markers on Map
**Steps**:
1. Look for city markers on map
2. Click on a marker

**Expected Results**:
- ✅ 37 city markers visible
- ✅ Markers color-coded by region
- ✅ Clicking marker shows city info
- ✅ Shows: City name, State, Population
- ✅ "Simulate" button in popup

**Status**: [ ] Pass [ ] Fail

---

### Test 5.3: Map Interaction with Simulation
**Steps**:
1. Click Bengaluru marker on map
2. Click "Simulate" in popup
3. Observe simulator section

**Expected Results**:
- ✅ Simulator updates to Karnataka/Bengaluru
- ✅ Page scrolls to simulator
- ✅ Ready to enter policy
- ✅ Map selection persists

**Status**: [ ] Pass [ ] Fail

---

## 6. Performance & Responsiveness

### Test 6.1: Page Load Performance
**Steps**:
1. Open http://localhost:3001 in new tab
2. Measure load time
3. Check browser console for errors

**Expected Results**:
- ✅ Initial load < 2 seconds
- ✅ No console errors
- ✅ No 404 errors
- ✅ All images load
- ✅ Fonts load correctly

**Status**: [ ] Pass [ ] Fail

---

### Test 6.2: Simulation Performance
**Steps**:
1. Run a simulation
2. Measure time from click to results
3. Check for lag or freezing

**Expected Results**:
- ✅ Results appear within 5-10 seconds
- ✅ No page freezing
- ✅ Loading indicator shows progress
- ✅ UI remains responsive
- ✅ Can cancel simulation

**Status**: [ ] Pass [ ] Fail

---

### Test 6.3: Mobile Responsiveness
**Steps**:
1. Open browser DevTools (F12)
2. Toggle device toolbar (Ctrl+Shift+M)
3. Select iPhone 12 Pro
4. Test all features

**Expected Results**:
- ✅ Layout adapts to mobile screen
- ✅ Navigation menu collapses
- ✅ State cards stack vertically
- ✅ Buttons are touch-friendly
- ✅ Text is readable
- ✅ No horizontal scrolling

**Status**: [ ] Pass [ ] Fail

---

### Test 6.4: Tablet Responsiveness
**Steps**:
1. In DevTools, select iPad
2. Test all features

**Expected Results**:
- ✅ Layout optimized for tablet
- ✅ 2-column grid for state cards
- ✅ All features accessible
- ✅ Touch interactions work
- ✅ Proper spacing

**Status**: [ ] Pass [ ] Fail

---

### Test 6.5: Desktop Responsiveness
**Steps**:
1. Test on 1920x1080 resolution
2. Test on 1366x768 resolution
3. Test on 2560x1440 resolution

**Expected Results**:
- ✅ Layout scales properly
- ✅ Content centered
- ✅ No overflow issues
- ✅ Images scale correctly
- ✅ Readable on all resolutions

**Status**: [ ] Pass [ ] Fail

---

## 7. API Endpoints

### Test 7.1: Knowledge Base Info
**URL**: http://localhost:8000/knowledge

**Steps**:
1. Open URL in browser
2. Check JSON response

**Expected Results**:
```json
{
  "name": "Indian Policy Knowledge Base",
  "status": "operational",
  "coverage": {
    "total_policies": "60+",
    "states_covered": ["Karnataka", "Maharashtra", ...]
  }
}
```

**Status**: [ ] Pass [ ] Fail

---

### Test 7.2: Quick Test Endpoint
**URL**: http://localhost:8000/knowledge/test

**Steps**:
1. Open URL in browser
2. Check all tests pass

**Expected Results**:
```json
{
  "tests": {
    "get_policy": "✅ Pass",
    "search": "✅ Pass (2 results)",
    "state_policies": "✅ Pass (7 categories)",
    "budget": "✅ Pass"
  },
  "overall": "✅ All tests passed"
}
```

**Status**: [ ] Pass [ ] Fail

---

### Test 7.3: List States
**URL**: http://localhost:8000/knowledge/states

**Expected Results**:
- ✅ Shows 6 states
- ✅ Each state has policy_count
- ✅ Budget availability shown
- ✅ Categories listed

**Status**: [ ] Pass [ ] Fail

---

### Test 7.4: Get Karnataka Policies
**URL**: http://localhost:8000/knowledge/state/Karnataka

**Expected Results**:
- ✅ Shows economic policies (2)
- ✅ Shows social policies (3): Gruha Jyothi, Gruha Lakshmi, Anna Bhagya
- ✅ Shows infrastructure policies (1)
- ✅ Shows budget_2025_26 data
- ✅ All amounts in INR

**Status**: [ ] Pass [ ] Fail

---

### Test 7.5: Search Policies
**URL**: http://localhost:8000/knowledge/search?q=electricity

**Expected Results**:
- ✅ Returns 2+ results
- ✅ Includes Karnataka Gruha Jyothi
- ✅ Includes Delhi Free Electricity
- ✅ Each result has state, category, policy name, data

**Status**: [ ] Pass [ ] Fail

---

### Test 7.6: Get Budget Data
**URL**: http://localhost:8000/knowledge/budget/Karnataka

**Expected Results**:
```json
{
  "state": "Karnataka",
  "year": "2025_26",
  "budget": {
    "total_outlay": 408647000000,
    "gsdp_projection": 3070103000000,
    "gsdp_growth": 7.0,
    "key_allocations": {...}
  }
}
```

**Status**: [ ] Pass [ ] Fail

---

### Test 7.7: National Policies
**URL**: http://localhost:8000/knowledge/national/economic

**Expected Results**:
- ✅ Shows 3 policies: Make in India, Atmanirbhar Bharat, Digital India
- ✅ Each has ministry, launched date, objective, budget
- ✅ Impact areas listed

**Status**: [ ] Pass [ ] Fail

---

### Test 7.8: Get All Schemes
**URL**: http://localhost:8000/knowledge/schemes

**Expected Results**:
- ✅ Lists central_sector schemes
- ✅ Lists centrally_sponsored schemes
- ✅ Lists state_schemes by state
- ✅ Karnataka shows: Gruha Jyothi, Gruha Lakshmi, Anna Bhagya, Yuva Nidhi, Shakti

**Status**: [ ] Pass [ ] Fail

---

### Test 7.9: Economic Data
**URL**: http://localhost:8000/knowledge/economic-data

**Expected Results**:
- ✅ Shows national indicators: GDP growth, inflation, unemployment
- ✅ Shows state-wise data for Karnataka, Maharashtra
- ✅ GSDP, per capita income, unemployment rate

**Status**: [ ] Pass [ ] Fail

---

### Test 7.10: API Documentation
**URL**: http://localhost:8000/docs

**Expected Results**:
- ✅ Swagger UI loads
- ✅ Shows all endpoints
- ✅ "knowledge" section visible
- ✅ Can test endpoints interactively
- ✅ Request/response schemas shown

**Status**: [ ] Pass [ ] Fail

---

## 8. Edge Cases & Error Handling

### Test 8.1: Empty Policy Input
**Steps**:
1. Select state and city
2. Leave policy input empty
3. Click "Run Simulation"

**Expected Results**:
- ✅ Shows error message
- ✅ "Please enter a policy description"
- ✅ No simulation runs
- ✅ UI remains stable

**Status**: [ ] Pass [ ] Fail

---

### Test 8.2: Invalid State Selection
**Steps**:
1. Try to run simulation without selecting state
2. Observe behavior

**Expected Results**:
- ✅ Shows error message
- ✅ "Please select a state"
- ✅ Highlights state selector
- ✅ No crash

**Status**: [ ] Pass [ ] Fail

---

### Test 8.3: Very Long Policy Input
**Steps**:
1. Enter 1000+ character policy description
2. Run simulation

**Expected Results**:
- ✅ Accepts long input
- ✅ Simulation runs successfully
- ✅ Results are relevant
- ✅ No truncation issues

**Status**: [ ] Pass [ ] Fail

---

### Test 8.4: Special Characters in Policy
**Steps**:
1. Enter policy with special characters: "Increase budget by ₹5,000 crore (50% more) for metro!"
2. Run simulation

**Expected Results**:
- ✅ Handles special characters correctly
- ✅ Extracts ₹5,000 crore correctly
- ✅ Simulation runs successfully
- ✅ No parsing errors

**Status**: [ ] Pass [ ] Fail

---

### Test 8.5: Network Error Handling
**Steps**:
1. Stop backend server
2. Try to run simulation
3. Observe error handling

**Expected Results**:
- ✅ Shows user-friendly error message
- ✅ "Unable to connect to server"
- ✅ Suggests checking connection
- ✅ No crash or blank screen

**Status**: [ ] Pass [ ] Fail

---

### Test 8.6: Rapid Multiple Clicks
**Steps**:
1. Click "Run Simulation" button 10 times rapidly
2. Observe behavior

**Expected Results**:
- ✅ Only one simulation runs
- ✅ Button disabled during simulation
- ✅ No duplicate requests
- ✅ UI remains stable

**Status**: [ ] Pass [ ] Fail

---

## 9. Accessibility

### Test 9.1: Keyboard Navigation
**Steps**:
1. Use Tab key to navigate through page
2. Use Enter to activate buttons
3. Use arrow keys in dropdowns

**Expected Results**:
- ✅ All interactive elements accessible via keyboard
- ✅ Focus indicators visible
- ✅ Logical tab order
- ✅ Can complete full simulation with keyboard only

**Status**: [ ] Pass [ ] Fail

---

### Test 9.2: Screen Reader Compatibility
**Steps**:
1. Enable screen reader (NVDA/JAWS)
2. Navigate through page
3. Run a simulation

**Expected Results**:
- ✅ All text read correctly
- ✅ Button labels clear
- ✅ Form fields labeled
- ✅ Results announced
- ✅ ARIA labels present

**Status**: [ ] Pass [ ] Fail

---

### Test 9.3: Color Contrast
**Steps**:
1. Use browser DevTools Lighthouse
2. Run accessibility audit
3. Check color contrast ratios

**Expected Results**:
- ✅ All text meets WCAG AA standards (4.5:1)
- ✅ Buttons have sufficient contrast
- ✅ Links distinguishable
- ✅ No color-only information

**Status**: [ ] Pass [ ] Fail

---

## 10. Browser Compatibility

### Test 10.1: Chrome
**Steps**: Test all features in Chrome

**Expected Results**: ✅ All features work

**Status**: [ ] Pass [ ] Fail

---

### Test 10.2: Firefox
**Steps**: Test all features in Firefox

**Expected Results**: ✅ All features work

**Status**: [ ] Pass [ ] Fail

---

### Test 10.3: Safari
**Steps**: Test all features in Safari

**Expected Results**: ✅ All features work

**Status**: [ ] Pass [ ] Fail

---

### Test 10.4: Edge
**Steps**: Test all features in Edge

**Expected Results**: ✅ All features work

**Status**: [ ] Pass [ ] Fail

---

## 📊 Test Summary Template

### Overall Results
- **Total Tests**: 60+
- **Passed**: ___
- **Failed**: ___
- **Skipped**: ___
- **Pass Rate**: ___%

### Critical Issues Found
1. 
2. 
3. 

### Minor Issues Found
1. 
2. 
3. 

### Recommendations
1. 
2. 
3. 

---

## 🎯 Priority Test Scenarios

### Must Test (Critical)
1. ✅ Homepage loads
2. ✅ State selection works
3. ✅ Policy simulation runs
4. ✅ Results display correctly
5. ✅ Knowledge base integration works
6. ✅ API endpoints respond

### Should Test (Important)
1. ✅ Search and filters work
2. ✅ Expandable cards function
3. ✅ Mobile responsiveness
4. ✅ Error handling
5. ✅ Multiple simulations

### Nice to Test (Optional)
1. ✅ Map interactions
2. ✅ Accessibility features
3. ✅ Browser compatibility
4. ✅ Performance metrics
5. ✅ Edge cases

---

## 📝 Testing Notes

### Environment
- **OS**: Windows
- **Browser**: ___________
- **Screen Resolution**: ___________
- **Date**: ___________
- **Tester**: ___________

### Additional Observations
- 
- 
- 

---

## ✅ Quick Checklist

Use this for rapid testing:

- [ ] Homepage loads
- [ ] Can select state
- [ ] Can run simulation
- [ ] Results show up
- [ ] Related policies displayed
- [ ] Search works
- [ ] Filters work
- [ ] View Data expands cards
- [ ] Simulate button works
- [ ] Mobile view works
- [ ] API endpoints work
- [ ] No console errors

---

**Start Testing**: http://localhost:3001

**API Testing**: http://localhost:8000/docs

**Knowledge Base**: http://localhost:8000/knowledge/test

**Happy Testing!** 🎉
