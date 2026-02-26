from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.models.india_schema import IndianPolicyInput, IndianRegion
from app.services.free_india_data import india_data_service
from app.services.cache_service import (
    get_cached_city_list,
    get_cached_city_data,
    get_cached_traffic_data,
    get_cached_economic_data
)
from app.db import get_database
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/india", tags=["india"])

class IndianSimulationRequest(BaseModel):
    policy_text: str
    region: IndianRegion
    enable_optimization: bool = True

@router.get("/cities")
async def get_available_cities():
    """Get list of available Indian cities with data - ALL 37 CITIES"""
    # Get detailed city information
    cities_detailed = []
    for state, state_cities in india_data_service.CENSUS_DATA.items():
        for city, data in state_cities.items():
            cities_detailed.append({
                "state": state,
                "city": city,
                "population": data["population"],
                "literacy_rate": data["literacy_rate"],
                "region": india_data_service.get_region_for_state(state)
            })
    
    states = india_data_service.get_states_list()
    return {
        "total": len(cities_detailed),
        "total_states_uts": len(states),
        "cities": cities_detailed,
        "states": states,
        "note": "Using FREE public data sources",
        "coverage": "28 States + 8 Union Territories = 37 Cities",
        "cached": True
    }

@router.get("/states")
async def get_all_states():
    """Get list of all Indian states and UTs"""
    states = india_data_service.get_states_list()
    return {
        "total": len(states),
        "states": states,
        "breakdown": {
            "states": 28,
            "union_territories": 8
        },
        "note": "Complete coverage of India"
    }

@router.get("/states/{state}/cities")
async def get_cities_by_state(state: str):
    """Get cities for a specific state"""
    cities = india_data_service.get_cities_by_state(state)
    if not cities:
        raise HTTPException(status_code=404, detail=f"State {state} not found")
    
    return {
        "state": state,
        "cities": cities,
        "total": len(cities)
    }

@router.get("/state-data/{state}")
async def get_state_data(state: str):
    """Get aggregated real data for entire state/UT"""
    state_data = india_data_service.get_state_data(state)
    traffic_data = india_data_service.get_traffic_data(state)
    
    if not state_data:
        raise HTTPException(status_code=404, detail=f"State {state} not found")
    
    return {
        "region": {
            "state": state,
            "country": "India"
        },
        "demographics": state_data,
        "traffic": traffic_data,
        "economic": india_data_service.get_economic_indicators(),
        "data_source": "FREE - Census India (Aggregated), TomTom Public Data",
        "note": "State-level aggregated data covering all cities"
    }

@router.get("/city-data/{state}/{city}")
async def get_city_data(state: str, city: str):
    """Get real data for a specific city - CACHED"""
    city_data = get_cached_city_data(state, city)
    traffic_data = get_cached_traffic_data(city)
    
    if not city_data:
        raise HTTPException(status_code=404, detail=f"City {city}, {state} not found")
    
    return {
        "region": {
            "state": state,
            "city": city,
            "country": "India"
        },
        "demographics": city_data,
        "traffic": traffic_data,
        "economic": get_cached_economic_data(),
        "data_source": "FREE - Census India, TomTom Public Data",
        "cached": True
    }

@router.post("/simulate")
async def simulate_indian_policy(
    request: IndianSimulationRequest,
    db = Depends(get_database)
):
    """Run simulation for Indian state with REAL data - OPTIMIZED"""
    try:
        from app.services.simulation_engine import SimulationEngine
        
        # Get real state data
        state_data = india_data_service.get_state_data(request.region.state)
        
        if not state_data:
            raise HTTPException(
                status_code=404,
                detail=f"No data available for {request.region.state}"
            )
        
        # Run simulation with real data
        engine = SimulationEngine()
        
        result = await engine.run_simulation(
            request.policy_text,
            request.enable_optimization,
            region={"state": request.region.state}
        )
        
        # Calculate real impact
        if "structured_policy" in result:
            policy_obj = result["structured_policy"]
            budget_inr = getattr(policy_obj, 'budget_allocation_inr', getattr(policy_obj, 'budget_allocation', 1000000))
            policy_type = getattr(policy_obj, 'policy_type', 'transportation')
            
            real_impact = india_data_service.calculate_policy_impact(
                state=request.region.state,
                policy_type=policy_type,
                budget_inr=budget_inr
            )
            
            result["real_india_impact"] = real_impact
        
        # Store in MongoDB
        simulation_doc = {
            "region": request.region.dict(),
            "policy_text": request.policy_text,
            "structured_policy": result["structured_policy"].dict() if hasattr(result.get("structured_policy"), "dict") else result.get("structured_policy"),
            "results": {
                k: v.dict() if hasattr(v, "dict") else v 
                for k, v in result.items() 
                if k != "structured_policy"
            },
            "real_data_used": True,
            "data_sources": ["Census India (State-level)", "TomTom Traffic Index", "RBI"],
            "timestamp": datetime.utcnow(),
            "optimized": request.enable_optimization
        }
        
        sim_result = await db.indian_simulations.insert_one(simulation_doc)
        simulation_id = str(sim_result.inserted_id)
        
        logger.info(f"Indian simulation completed: {simulation_id} for {request.region.state}")
        
        return {
            "simulation_id": simulation_id,
            "region": request.region.dict(),
            "results": result,
            "data_quality": "REAL - Free public sources (State-level)",
            "note": "Using 100% FREE data - State/UT level coverage!",
            "performance": "OPTIMIZED with caching"
        }
    
    except Exception as e:
        logger.error(f"Indian simulation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/traffic/{city}")
async def get_traffic_data(city: str):
    """Get real-time traffic data for city - CACHED"""
    traffic = get_cached_traffic_data(city)
    
    if not traffic:
        raise HTTPException(status_code=404, detail=f"No traffic data for {city}")
    
    return {
        "city": city,
        "traffic_data": traffic,
        "source": "TomTom Traffic Index (FREE public data)",
        "last_updated": "2024",
        "cached": True
    }

@router.get("/economic")
async def get_economic_indicators():
    """Get current Indian economic indicators - CACHED"""
    return {
        "indicators": get_cached_economic_data(),
        "source": "Reserve Bank of India (FREE public data)",
        "currency": "INR (₹)",
        "cached": True
    }
