# 🚀 Quick Start Guide - CivicSim AI

Get the AI Policy Sandbox running in under 10 minutes!

## Prerequisites

- Python 3.11+
- Node.js 18+
- MongoDB Atlas account (free tier works)

## Step 1: Clone and Setup

```bash
# Navigate to project directory
cd civicsim-ai

# Make setup script executable (Linux/Mac)
chmod +x setup.sh

# Run setup
./setup.sh
```

## Step 2: Configure MongoDB

1. Create a free MongoDB Atlas account at https://www.mongodb.com/cloud/atlas
2. Create a new cluster
3. Get your connection string
4. Edit `backend/.env`:

```env
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE_NAME=civicsim_ai
SECRET_KEY=your-random-secret-key-here
DEMO_MODE=true
```

## Step 3: Start Backend

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn app.main:app --reload
```

Backend will run on `http://localhost:8000`

## Step 4: Start Frontend

Open a new terminal:

```bash
cd frontend
npm run dev
```

Frontend will run on `http://localhost:3000`

## Step 5: Test the System

### Option A: Use the Web Interface

1. Open `http://localhost:3000`
2. Enter a policy like: "Implement congestion pricing with $5 peak hour fee"
3. Click "Run Simulation"
4. View results in the dashboard

### Option B: Test via API

```bash
curl -X POST http://localhost:8000/simulation/simulate \
  -H "Content-Type: application/json" \
  -d '{
    "policy_text": "Subsidize electric vehicles with $7500 tax credit",
    "enable_optimization": true
  }'
```

### Option C: Run Test Script

```bash
cd backend
python test_simulation.py
```

## Example Policies to Try

1. **Transportation**: "Implement congestion pricing in downtown with $5 peak hour fee"
2. **Environmental**: "Build 50 EV charging stations across the city"
3. **Economic**: "Provide $7,500 tax credit for electric vehicle purchases"
4. **Infrastructure**: "Add 2 new lanes to highway and improve public transit"

## Troubleshooting

### MongoDB Connection Error
- Verify your connection string in `.env`
- Check if your IP is whitelisted in MongoDB Atlas
- Ensure network access is configured

### Port Already in Use
- Backend: Change port with `uvicorn app.main:app --port 8001`
- Frontend: Change port in `package.json` or use `PORT=3001 npm run dev`

### Module Not Found
- Backend: Ensure virtual environment is activated
- Frontend: Run `npm install` again

### CORS Errors
- Verify backend is running on port 8000
- Check CORS settings in `backend/app/main.py`

## Docker Alternative

If you prefer Docker:

```bash
docker-compose up --build
```

This starts:
- Backend on `http://localhost:8000`
- Frontend on `http://localhost:3000`
- MongoDB on `localhost:27017`

## API Documentation

Once backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Demo Mode

By default, `DEMO_MODE=true` enables:
- Fast execution (< 5 seconds)
- Mock ML models
- Deterministic results
- No external API dependencies

For production, set `DEMO_MODE=false` and configure:
- `OPENAI_API_KEY` for LLM-based policy extraction
- Train actual ML models

## Next Steps

1. Explore the dashboard visualizations
2. Try different policy types
3. Compare optimized vs original policies
4. Review AI explanations and recommendations
5. Check MongoDB collections for stored data

## Architecture Overview

```
User Input → PolicyAgent → BehaviorAgent → SimulationAgent 
→ ImpactAgent → OptimizationAgent → ExplainabilityAgent 
→ MongoDB → Dashboard
```

## Support

- Check `README.md` for detailed documentation
- Review `PROJECT_STRUCTURE.md` for architecture details
- Examine `backend/test_simulation.py` for usage examples

## Performance Tips

- Simulation completes in < 10 seconds
- Uses 10,000 synthetic agents
- Vectorized numpy operations
- Async database queries

Happy simulating! 🎉
