# Testing Instructions - Hero Map with Government Style

## Quick Start

### 1. Start the Backend
```bash
cd backend
uvicorn app.main:app --reload
```
Wait for: `Application startup complete`

### 2. Start the Frontend (New Terminal)
```bash
cd frontend
npm run dev
```
Wait for: `Ready on http://localhost:3000`

### 3. Open Browser
Navigate to: **http://localhost:3000**

## What You Should See

### Hero Section (Top of Page)
- Clean blue gradient background
- Indian flag colored borders (orange-white-green) at top and bottom
- Large heading: "Complete India Policy Simulation"
- Orange badge: "Government of India Initiative"

### Interactive Map (Right Side)
- Large India map (650px)
- Blue colored states
- Map title: "🗺️ Interactive India Map"
- Subtitle: "Hover over any state for real-time data"

### Stats Cards (Below Map)
- 4 colorful cards showing:
  - States & UTs: 36
  - Cities: 37
  - Accuracy: 99.86%
  - Cost: ₹0

## Testing the Hover Functionality

### Step 1: Hover Over a State
Move your mouse over any state on the map (e.g., Karnataka, Punjab, Maharashtra)

### Step 2: Watch for Tooltip
A dark tooltip should appear showing:
```
Karnataka
─────────────────
Population: 8,443,675
Vehicles: 7,200,000
Literacy: 88.71%
Congestion: 74.4%
Income: ₹48,000
```

### Step 3: Move Around
- Tooltip should follow your cursor
- Try different states to see different data
- Tooltip should disappear when you move away

## States to Test

### Large States (High Population)
- Maharashtra (Mumbai + Pune)
- Delhi (New Delhi)
- Karnataka (Bengaluru)
- Tamil Nadu (Chennai)
- West Bengal (Kolkata)

### Small States/UTs
- Goa (Panaji)
- Sikkim (Gangtok)
- Lakshadweep (Kavaratti)
- Ladakh (Leh)

### Different Regions
- North: Punjab, Haryana, Himachal Pradesh
- South: Kerala, Andhra Pradesh, Telangana
- East: Bihar, Jharkhand, Odisha
- West: Gujarat, Rajasthan
- Northeast: Assam, Meghalaya, Mizoram

## What to Check

### Visual Design
- [ ] Clean, professional government website look
- [ ] No excessive glow or cyber effects
- [ ] Indian flag borders visible at top and bottom
- [ ] Map is large and easy to see (650px)
- [ ] No decorative frames around map
- [ ] Stats cards are colorful and clear

### Functionality
- [ ] Map loads correctly
- [ ] All states are visible and colored
- [ ] Hovering changes state color to orange
- [ ] Tooltip appears on hover
- [ ] Tooltip shows correct state name
- [ ] Tooltip shows real data (population, vehicles, etc.)
- [ ] Tooltip follows cursor smoothly
- [ ] Tooltip disappears when moving away
- [ ] Loading spinner shows while fetching data

### Data Accuracy
- [ ] Population numbers look realistic
- [ ] Literacy rates are percentages (60-95%)
- [ ] Income is in Indian Rupees (₹)
- [ ] Congestion levels vary by state
- [ ] No "undefined" or "null" values

## Troubleshooting

### Map Not Showing
- Check browser console for errors (F12)
- Verify frontend is running on port 3000
- Clear browser cache and reload

### Tooltip Not Appearing
- Check if backend is running on port 8000
- Test API directly: `curl http://localhost:8000/india/state-data/Karnataka`
- Check browser console for network errors

### Data Not Loading
- Verify backend is connected
- Check MongoDB is running (if needed)
- Look for "Loading data..." in tooltip

### Wrong Data Showing
- Verify state name matches exactly
- Check backend logs for errors
- Test with different states

## Expected Behavior

### On Page Load
1. Hero section appears immediately
2. Map loads within 1-2 seconds
3. Stats cards show correct numbers
4. No errors in console

### On Hover
1. State color changes to orange instantly
2. Tooltip appears within 100ms
3. Data fetches in background (< 500ms)
4. Tooltip shows "Loading data..." if slow
5. Real data populates tooltip
6. Tooltip follows cursor smoothly

### On Move Away
1. State color returns to blue
2. Tooltip disappears immediately
3. No lingering effects

## Success Criteria

✓ Map displays all 36 states/UTs
✓ Hover changes state color
✓ Tooltip appears with state name
✓ Real data loads and displays
✓ Design looks clean and professional
✓ No cyber effects or excessive styling
✓ Indian flag accents visible
✓ All data in Indian Rupees (₹)
✓ No errors in console
✓ Smooth user experience

## If Everything Works

You should be able to:
1. See a clean, government-style hero section
2. Hover over any state and see its real data
3. Navigate the map easily
4. Read all information clearly
5. Experience smooth interactions

## Report Issues

If something doesn't work:
1. Note which state you hovered on
2. Check browser console for errors
3. Check backend logs for errors
4. Take a screenshot if visual issue
5. Note what you expected vs what happened

---

**Status**: Ready for testing
**Last Updated**: Current session
**Build Status**: ✓ Successful
**Backend Test**: ✓ Passed
