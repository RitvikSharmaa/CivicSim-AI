from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
from app.services.simulation_engine import SimulationEngine
from app.db import get_database
from bson import ObjectId
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/simulation", tags=["simulation"])

class RegionData(BaseModel):
    state: str

class SimulationRequest(BaseModel):
    policy_text: str
    enable_optimization: bool = True
    region: Optional[RegionData] = None

class OptimizationRequest(BaseModel):
    simulation_id: str

@router.post("/simulate")
async def run_simulation(
    request: SimulationRequest,
    db = Depends(get_database)
):
    """Run complete simulation pipeline"""
    try:
        engine = SimulationEngine()
        
        # Convert region to dict if provided
        region_dict = None
        if request.region:
            region_dict = {
                "state": request.region.state
            }
        
        # Execute simulation with region
        result = await engine.run_simulation(
            request.policy_text,
            request.enable_optimization,
            region=region_dict
        )
        
        # Store results in MongoDB
        simulation_doc = {
            "policy_id": None,  # Link if policy exists
            "region": region_dict,
            "metrics": result.get("simulation_metrics"),
            "impact_predictions": result.get("impact_predictions"),
            "optimization_result": result.get("optimization_result"),
            "explanation": result.get("explanation"),
            "timestamp": datetime.utcnow()
        }
        
        sim_result = await db.simulations.insert_one(simulation_doc)
        simulation_id = str(sim_result.inserted_id)
        
        logger.info(f"Simulation completed for {region_dict}: {simulation_id}")
        
        return {
            "simulation_id": simulation_id,
            "results": {
                "metrics": result.get("simulation_metrics"),
                "impact_predictions": result.get("impact_predictions"),
                "optimization": result.get("optimization_result"),
                "explanation": result.get("explanation")
            }
        }
    
    except Exception as e:
        logger.error(f"Simulation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{simulation_id}")
async def get_simulation(
    simulation_id: str,
    db = Depends(get_database)
):
    """Retrieve simulation results"""
    try:
        simulation = await db.simulations.find_one({"_id": ObjectId(simulation_id)})
        
        if not simulation:
            raise HTTPException(status_code=404, detail="Simulation not found")
        
        simulation["_id"] = str(simulation["_id"])
        return simulation
    
    except Exception as e:
        logger.error(f"Error retrieving simulation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/optimize")
async def optimize_policy(
    request: OptimizationRequest,
    db = Depends(get_database)
):
    """Run optimization on existing simulation"""
    try:
        # Retrieve simulation
        simulation = await db.simulations.find_one({"_id": ObjectId(request.simulation_id)})
        
        if not simulation:
            raise HTTPException(status_code=404, detail="Simulation not found")
        
        # Run optimization agent
        from app.agents.optimization_agent import OptimizationAgent
        
        agent = OptimizationAgent()
        state = {
            "structured_policy": simulation.get("policy_id"),
            "simulation_metrics": simulation.get("metrics")
        }
        
        result = await agent.process(state)
        
        # Update simulation with optimization results
        await db.simulations.update_one(
            {"_id": ObjectId(request.simulation_id)},
            {"$set": {"optimization_result": result["optimization_result"]}}
        )
        
        return {"optimization_result": result["optimization_result"]}
    
    except Exception as e:
        logger.error(f"Optimization error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
