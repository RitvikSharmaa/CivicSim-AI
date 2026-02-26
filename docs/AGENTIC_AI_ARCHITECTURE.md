# Agentic AI Architecture

## Overview

This project implements a **Multi-Agent AI System** using **LangGraph** for orchestration. The system consists of **6 specialized AI agents** that work together to analyze policy impacts.

---

## 🤖 What is Agentic AI?

**Agentic AI** refers to AI systems where multiple autonomous agents:
- Have specific roles and responsibilities
- Make independent decisions
- Communicate and collaborate with each other
- Work towards a common goal
- Can adapt their behavior based on context

Unlike traditional AI pipelines, agentic systems are:
- **Modular**: Each agent is independent
- **Scalable**: Easy to add/remove agents
- **Flexible**: Agents can be reordered or conditionally executed
- **Intelligent**: Agents make decisions, not just process data

---

## 🏗️ System Architecture

### Orchestration Framework: **LangGraph**

**File**: `backend/app/services/simulation_engine.py`

```python
class SimulationEngine:
    """LangGraph-based orchestration of all agents"""
    
    def _build_graph(self):
        workflow = StateGraph(SimulationState)
        
        # Add agent nodes
        workflow.add_node("policy", self.policy_agent.process)
        workflow.add_node("behavior", self.behavior_agent.process)
        workflow.add_node("simulation", self.simulation_agent.process)
        workflow.add_node("impact", self.impact_agent.process)
        workflow.add_node("optimization", self.optimization_agent.process)
        workflow.add_node("explainability", self.explainability_agent.process)
        
        # Define execution flow
        workflow.set_entry_point("policy")
        workflow.add_edge("policy", "behavior")
        workflow.add_edge("behavior", "simulation")
        workflow.add_edge("simulation", "impact")
        
        # Conditional routing
        workflow.add_conditional_edges(
            "impact",
            self._should_optimize,
            {"optimize": "optimization", "skip": "explainability"}
        )
```

**Key Features**:
- **State Management**: Shared state across all agents
- **Conditional Routing**: Dynamic execution paths
- **Async Execution**: Non-blocking agent processing
- **Error Handling**: Graceful fallbacks

---

## 🎯 The 6 AI Agents

### 1. **Policy Agent** 🏛️
**File**: `backend/app/agents/policy_agent.py`

**Role**: Natural Language Understanding (NLU) for policy extraction

**Capabilities**:
- Parses natural language policy descriptions
- Extracts structured parameters (budget, timeline, enforcement)
- Converts INR amounts (crore, lakh, rupees)
- Determines policy type (transportation, economic, environmental, etc.)
- Queries knowledge base for related policies
- Uses LLM (OpenRouter) or rule-based extraction

**Input**: 
```
"Increase metro rail budget by ₹5000 crore to reduce traffic congestion"
```

**Output**:
```python
IndianStructuredPolicy(
    budget_allocation_inr=50000000000,  # 5000 crore
    policy_type="transportation",
    implementation_timeline_days=90,
    enforcement_level=0.7,
    incentive_structure={...},
    infrastructure_changes={...}
)
```

**AI Techniques**:
- Regex pattern matching for INR extraction
- Keyword-based classification
- Optional LLM integration (GPT-4, Claude)
- Knowledge base retrieval

---

### 2. **Behavior Agent** 🧠
**File**: `backend/app/agents/behavior_agent.py`

**Role**: Predict citizen behavioral responses using Deep Learning

**Capabilities**:
- Uses trained **LSTM neural network** (PyTorch)
- Predicts 4 behavioral metrics
- Adjusts predictions based on state characteristics (literacy, income, urbanization)
- Caches model for performance

**Input**: Policy parameters + State data

**Output**:
```python
{
    "adaptation_rate": 0.75,           # How quickly citizens adapt
    "compliance_probability": 0.82,    # Likelihood of compliance
    "satisfaction_score": 0.68,        # Citizen satisfaction
    "economic_impact_personal": 0.15   # Personal economic impact
}
```

**AI Techniques**:
- **LSTM (Long Short-Term Memory)** neural network
- Feature engineering (10 features)
- StandardScaler normalization
- State-specific adjustments

**Model Details**:
- Input: 10 features (budget, timeline, enforcement, demographics)
- Hidden: 32 LSTM units
- Output: 4 predictions (sigmoid activation)
- Framework: PyTorch

---

### 3. **Simulation Agent** 🎮
**File**: `backend/app/agents/simulation_agent.py`

**Role**: Agent-Based Modeling (ABM) for system simulation

**Capabilities**:
- Simulates 10,000 virtual citizens
- Models infrastructure as a graph (NetworkX)
- Calculates real-world metrics using state data
- Computes congestion, energy load, dissatisfaction, economic stability

**Input**: Policy + Behavioral predictions + Real state data

**Output**:
```python
{
    "congestion_score": 0.645,
    "energy_load": 0.35,
    "dissatisfaction_index": 0.42,
    "economic_stability": 0.78,
    "infrastructure_stress": {...}
}
```

**AI Techniques**:
- **Agent-Based Modeling (ABM)**
- Graph theory (NetworkX)
- Monte Carlo simulation
- Real data integration

**Infrastructure Model**:
- 100-node graph (Barabási-Albert model)
- Nodes: residential, commercial, industrial
- Edges: roads with capacity
- Cached for performance

---

### 4. **Impact Agent** 📊
**File**: `backend/app/agents/impact_agent.py`

**Role**: Predict macro-level impacts using Machine Learning

**Capabilities**:
- Uses 4 trained **XGBoost models**
- Predicts congestion, inflation, dissatisfaction, energy stress
- Provides confidence intervals
- Integrates real economic data (RBI)

**Input**: Simulation metrics + Policy + State data

**Output**:
```python
{
    "congestion_score": 0.645,
    "inflation_rate": 0.052,
    "dissatisfaction_index": 0.42,
    "energy_stress": 0.35,
    "confidence_intervals": {...},
    "real_data_used": True
}
```

**AI Techniques**:
- **XGBoost (Gradient Boosting)**
- 4 separate regression models
- Feature importance analysis
- Ensemble predictions

**Model Details**:
- Input: 8 features
- Trees: 100 per model
- Max depth: 5
- Framework: XGBoost

---

### 5. **Optimization Agent** 🔧
**File**: `backend/app/agents/optimization_agent.py`

**Role**: Optimize policy parameters using Reinforcement Learning

**Capabilities**:
- Uses **PPO (Proximal Policy Optimization)**
- Creates custom Gym environment
- Optimizes 5 policy parameters
- Multi-objective reward function

**Input**: Policy + Simulation metrics

**Output**:
```python
{
    "optimized_parameters": {
        "budget_allocation_inr": 52000000000,
        "enforcement_level": 0.75,
        "implementation_timeline_days": 85,
        "tax_reduction": 0.18,
        "subsidy": 5500
    },
    "reward_score": -0.98,
    "improvement_percentage": 8.1,
    "comparison_metrics": {...}
}
```

**AI Techniques**:
- **Reinforcement Learning (RL)**
- **PPO (Proximal Policy Optimization)**
- Custom Gym environment
- Multi-objective optimization

**RL Environment**:
- Action space: 5D continuous (±30% adjustments)
- Observation space: 8D continuous (policy state)
- Reward: Multi-objective (congestion, satisfaction, economy)
- Framework: Stable-Baselines3

---

### 6. **Explainability Agent** 📚
**File**: `backend/app/agents/explainability_agent.py`

**Role**: Generate comprehensive human-readable explanations

**Capabilities**:
- Creates 10-section comprehensive report
- Uses **SHAP (SHapley Additive exPlanations)**
- Provides feature importance
- Generates 8 strategic recommendations with priority levels
- Includes risk assessment and data sources

**Input**: All previous agent outputs

**Output**:
```python
{
    "narrative_summary": "COMPREHENSIVE POLICY ANALYSIS REPORT...",
    "shap_values": {...},
    "feature_importance": {
        "budget_allocation_inr": 0.25,
        "tax_reduction": 0.22,
        "enforcement_level": 0.18,
        ...
    },
    "recommendations": [
        {
            "priority": "High",
            "category": "Budget Allocation",
            "recommendation": "Increase budget by 10-15%",
            "rationale": "SHAP shows 25% influence",
            "action_items": [...]
        },
        ...
    ]
}
```

**AI Techniques**:
- **SHAP (SHapley Additive exPlanations)**
- Natural Language Generation (NLG)
- Template-based reporting
- Feature importance ranking

**Report Sections**:
1. Executive Summary
2. Policy Overview
3. State/UT Profile
4. Current Traffic & Infrastructure
5. Economic Indicators
6. Predicted Impact
7. Optimization Recommendations
8. Key Impact Drivers (SHAP)
9. Risk Assessment
10. Data Sources & Methodology

---

## 🔄 Agent Workflow

```
User Input: "Increase metro budget by ₹5000 crore"
    ↓
┌─────────────────────────────────────────────────┐
│ 1. POLICY AGENT (NLU)                          │
│    - Parse natural language                     │
│    - Extract budget: ₹5000 crore               │
│    - Determine type: transportation             │
│    - Query knowledge base                       │
└─────────────────────────────────────────────────┘
    ↓ Structured Policy
┌─────────────────────────────────────────────────┐
│ 2. BEHAVIOR AGENT (LSTM)                       │
│    - Load trained neural network                │
│    - Predict citizen responses                  │
│    - Adaptation: 0.75, Compliance: 0.82        │
└─────────────────────────────────────────────────┘
    ↓ Behavioral Predictions
┌─────────────────────────────────────────────────┐
│ 3. SIMULATION AGENT (ABM)                      │
│    - Simulate 10,000 agents                     │
│    - Model infrastructure graph                 │
│    - Calculate metrics with real data           │
└─────────────────────────────────────────────────┘
    ↓ Simulation Metrics
┌─────────────────────────────────────────────────┐
│ 4. IMPACT AGENT (XGBoost)                      │
│    - Load 4 trained models                      │
│    - Predict macro impacts                      │
│    - Congestion, inflation, satisfaction        │
└─────────────────────────────────────────────────┘
    ↓ Impact Predictions
┌─────────────────────────────────────────────────┐
│ 5. OPTIMIZATION AGENT (RL/PPO)                 │
│    - Create Gym environment                     │
│    - Train PPO agent                            │
│    - Optimize 5 parameters                      │
│    - Improvement: +8.1%                         │
└─────────────────────────────────────────────────┘
    ↓ Optimized Parameters
┌─────────────────────────────────────────────────┐
│ 6. EXPLAINABILITY AGENT (SHAP)                 │
│    - Generate comprehensive report              │
│    - Calculate SHAP values                      │
│    - Create 8 recommendations                   │
│    - Risk assessment                            │
└─────────────────────────────────────────────────┘
    ↓
Final Results to User
```

---

## 🧩 State Management

**Shared State** (TypedDict):
```python
class SimulationState(TypedDict):
    policy_input: str                    # Original user input
    structured_policy: Any               # From Policy Agent
    behavior_output: Dict                # From Behavior Agent
    simulation_metrics: Dict             # From Simulation Agent
    impact_predictions: Dict             # From Impact Agent
    optimization_result: Dict            # From Optimization Agent
    explanation: Dict                    # From Explainability Agent
    enable_optimization: bool            # User preference
    region: Dict                         # State/UT selection
```

Each agent:
1. Receives the current state
2. Processes its specific task
3. Updates the state with its output
4. Passes state to next agent

---

## 🎛️ Conditional Routing

**Dynamic Execution Path**:

```python
def _should_optimize(self, state: SimulationState) -> str:
    """Decide whether to run optimization"""
    return "optimize" if state.get("enable_optimization", True) else "skip"
```

**Flow**:
- If `enable_optimization=True`: Impact → Optimization → Explainability
- If `enable_optimization=False`: Impact → Explainability (skip optimization)

This allows users to:
- Get faster results (skip optimization)
- Get optimized recommendations (include optimization)

---

## 🚀 Key Agentic Features

### 1. **Autonomy**
Each agent makes independent decisions:
- Policy Agent decides extraction method (LLM vs rule-based)
- Behavior Agent adjusts predictions based on state context
- Simulation Agent calculates metrics using real data
- Impact Agent provides confidence intervals
- Optimization Agent determines best parameters
- Explainability Agent prioritizes recommendations

### 2. **Communication**
Agents communicate through shared state:
- Structured data passing (not just text)
- Type-safe interfaces (TypedDict)
- Async message passing

### 3. **Collaboration**
Agents build on each other's work:
- Behavior Agent uses Policy Agent's output
- Simulation Agent uses Behavior Agent's predictions
- Impact Agent uses Simulation Agent's metrics
- Optimization Agent improves Impact Agent's results
- Explainability Agent synthesizes all outputs

### 4. **Adaptability**
System adapts to context:
- Different states/UTs get different predictions
- Real data integration (not static)
- Conditional optimization
- Fallback mechanisms

### 5. **Modularity**
Easy to modify/extend:
- Add new agents (e.g., Risk Agent, Compliance Agent)
- Replace agents (e.g., swap LSTM with Transformer)
- Reorder execution
- Add parallel execution

---

## 🔧 Technologies Used

| Component | Technology |
|-----------|-----------|
| Orchestration | **LangGraph** |
| State Management | TypedDict, Pydantic |
| Agent Communication | Async/Await |
| Deep Learning | PyTorch (LSTM) |
| Machine Learning | XGBoost |
| Reinforcement Learning | Stable-Baselines3 (PPO) |
| Explainability | SHAP |
| Agent-Based Modeling | NetworkX |
| NLU | Regex + Optional LLM |

---

## 📊 Performance Metrics

### Agent Execution Times (Optimized):
- Policy Agent: ~50ms (rule-based) or ~2s (LLM)
- Behavior Agent: ~100ms (cached model)
- Simulation Agent: ~200ms (cached graph)
- Impact Agent: ~150ms (cached models)
- Optimization Agent: ~500ms (limited training)
- Explainability Agent: ~300ms

**Total Pipeline**: ~1.3 seconds (without LLM) or ~3 seconds (with LLM)

### Optimizations:
- Model caching (85% faster)
- Graph caching (90% faster)
- Vectorized operations
- Async execution
- Minimal RL training steps

---

## 🎯 Agentic AI Benefits

### vs Traditional Pipeline:
| Traditional Pipeline | Agentic AI System |
|---------------------|-------------------|
| Sequential, rigid | Flexible, conditional |
| Monolithic | Modular |
| Hard to debug | Agent-level debugging |
| Difficult to extend | Easy to add agents |
| No decision-making | Autonomous decisions |
| Static flow | Dynamic routing |

### Real-World Advantages:
1. **Scalability**: Add agents without rewriting system
2. **Maintainability**: Fix one agent without affecting others
3. **Testability**: Test agents independently
4. **Flexibility**: Change execution order dynamically
5. **Intelligence**: Agents make context-aware decisions
6. **Transparency**: Clear agent responsibilities

---

## 🔮 Future Enhancements

### Potential New Agents:
1. **Risk Agent**: Assess implementation risks
2. **Compliance Agent**: Check legal/regulatory compliance
3. **Stakeholder Agent**: Analyze stakeholder impacts
4. **Timeline Agent**: Create detailed implementation plans
5. **Budget Agent**: Optimize budget allocation
6. **Communication Agent**: Generate public announcements

### Advanced Features:
1. **Multi-Agent Debate**: Agents discuss and reach consensus
2. **Hierarchical Agents**: Manager agents coordinating worker agents
3. **Parallel Execution**: Run independent agents simultaneously
4. **Agent Learning**: Agents improve from past simulations
5. **Human-in-the-Loop**: Agents request human input when uncertain

---

## 📚 References

- LangGraph: https://langchain-ai.github.io/langgraph/
- Multi-Agent Systems: https://en.wikipedia.org/wiki/Multi-agent_system
- Agent-Based Modeling: https://en.wikipedia.org/wiki/Agent-based_model
- Reinforcement Learning: https://spinningup.openai.com/
- SHAP: https://shap.readthedocs.io/

---

**Built with ❤️ for Indian Government • 100% FREE & Open Source**
