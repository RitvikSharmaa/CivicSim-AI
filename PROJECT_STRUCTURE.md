# CivicSim AI - Project Structure

## Complete File Tree

```
civicsim-ai/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI application entry
│   │   ├── config.py                  # Configuration management
│   │   ├── db.py                      # MongoDB connection
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   ├── policy_agent.py        # NLP policy extraction
│   │   │   ├── behavior_agent.py      # LSTM behavioral prediction
│   │   │   ├── simulation_agent.py    # Agent-based simulation
│   │   │   ├── impact_agent.py        # XGBoost impact forecasting
│   │   │   ├── optimization_agent.py  # PPO policy optimization
│   │   │   └── explainability_agent.py # SHAP explanations
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── policy_schema.py       # Policy data models
│   │   │   └── simulation_schema.py   # Simulation data models
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── policy_routes.py       # Policy API endpoints
│   │   │   └── simulation_routes.py   # Simulation API endpoints
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── simulation_engine.py   # LangGraph orchestration
│   │       └── synthetic_data_generator.py
│   ├── requirements.txt
│   ├── .env.example
│   └── test_simulation.py
│
├── frontend/
│   ├── app/
│   │   ├── components/
│   │   │   ├── PolicyInput.tsx        # Policy input form
│   │   │   ├── Dashboard.tsx          # Main dashboard
│   │   │   ├── MetricsCard.tsx        # Metric display cards
│   │   │   ├── ImpactChart.tsx        # Recharts visualization
│   │   │   └── ExplanationPanel.tsx   # AI explanation display
│   │   ├── store/
│   │   │   └── simulationStore.ts     # Zustand state management
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── next.config.js
│   └── postcss.config.js
│
├── README.md
├── Dockerfile
├── docker-compose.yml
├── setup.sh
└── PROJECT_STRUCTURE.md
```

## Component Responsibilities

### Backend Agents

1. **PolicyAgent**: Extracts structured parameters from natural language
2. **BehaviorAgent**: Predicts citizen behavioral responses using LSTM
3. **SimulationAgent**: Runs agent-based simulation with infrastructure graphs
4. **ImpactAgent**: Forecasts macro-level impacts using XGBoost
5. **OptimizationAgent**: Optimizes policy parameters using PPO
6. **ExplainabilityAgent**: Generates SHAP-based explanations

### Frontend Components

1. **PolicyInput**: Natural language policy input form
2. **Dashboard**: Main results visualization container
3. **MetricsCard**: Individual metric display
4. **ImpactChart**: Bar chart for impact predictions
5. **ExplanationPanel**: AI explanation and recommendations

### Data Flow

```
User Input (Natural Language)
    ↓
PolicyAgent (Extract Structure)
    ↓
BehaviorAgent (LSTM Prediction)
    ↓
SimulationAgent (Agent-Based Sim)
    ↓
ImpactAgent (XGBoost Forecast)
    ↓
OptimizationAgent (PPO Optimization)
    ↓
ExplainabilityAgent (SHAP + Narrative)
    ↓
MongoDB Storage
    ↓
Frontend Dashboard
```

## Key Technologies

- **LangGraph**: Agent orchestration with state management
- **PyTorch**: LSTM neural network for behavioral modeling
- **XGBoost**: Gradient boosting for impact prediction
- **Stable-Baselines3**: PPO reinforcement learning
- **SHAP**: Model explainability
- **NetworkX**: Graph-based infrastructure modeling
- **FastAPI**: Async REST API
- **Next.js**: React framework with App Router
- **Zustand**: Lightweight state management
- **Recharts**: Data visualization

## MongoDB Schema

### Collections

1. **policies**: Stores policy documents with structured parameters
2. **simulations**: Stores simulation results and predictions
3. **optimization_results**: Stores optimization outcomes
4. **agent_logs**: Logs agent activities for debugging

## API Endpoints

- `POST /policy/` - Create policy
- `GET /policy/{id}` - Retrieve policy
- `POST /simulation/simulate` - Run simulation
- `GET /simulation/{id}` - Get results
- `POST /simulation/optimize` - Optimize policy

## Environment Variables

```
MONGODB_URL=mongodb+srv://...
DATABASE_NAME=civicsim_ai
SECRET_KEY=your-secret-key
OPENAI_API_KEY=optional
DEMO_MODE=true
```

## Development Workflow

1. Start MongoDB (local or Atlas)
2. Configure `.env` file
3. Run backend: `uvicorn app.main:app --reload`
4. Run frontend: `npm run dev`
5. Access at `http://localhost:3000`

## Testing

Run test simulation:
```bash
cd backend
python test_simulation.py
```

## Deployment

Use Docker Compose:
```bash
docker-compose up --build
```

Or deploy separately:
- Backend: Deploy to Cloud Run, Heroku, or AWS Lambda
- Frontend: Deploy to Vercel or Netlify
- Database: MongoDB Atlas

## Performance Considerations

- Simulation runtime: < 10 seconds
- Vectorized numpy operations
- Async database queries
- Minimal RL training steps
- Cached model predictions

## Future Enhancements

- Real-time streaming results
- Multi-city support
- Historical policy comparison
- Interactive map visualization
- User authentication
- Policy templates library
- Export to PDF reports
