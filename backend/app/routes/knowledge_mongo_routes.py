"""
MongoDB-based Knowledge Base API Routes
High-performance routes using MongoDB for policy data
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.knowledge_base_service import get_kb_service
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/knowledge/v2", tags=["knowledge-v2"])

@router.get("/")
async def knowledge_base_info():
    """Get information about the MongoDB knowledge base"""
    kb_service = await get_kb_service()
    stats = await kb_service.get_statistics()
    
    return {
        "name": "Indian Policy Knowledge Base (MongoDB)",
        "version": "2.0.0",
        "status": "operational",
        "storage": "MongoDB",
        "features": [
            "Full-text search",
            "Advanced filtering",
            "Aggregation queries",
            "Real-time statistics"
        ],
        "statistics": stats,
        "endpoints": {
            "get_policy": "/knowledge/v2/policy/{state}/{category}/{policy_key}",
            "get_state_policies": "/knowledge/v2/state/{state}",
            "get_state_summary": "/knowledge/v2/state/{state}/summary",
            "search_policies": "/knowledge/v2/search?q={query}",
            "get_related": "/knowledge/v2/related?type={policy_type}&state={state}",
            "get_budget": "/knowledge/v2/budget/{state}",
            "list_states": "/knowledge/v2/states",
            "get_national": "/knowledge/v2/national/{category}",
            "top_by_budget": "/knowledge/v2/top-budget",
            "by_impact_area": "/knowledge/v2/impact/{area}"
        }
    }

@router.get("/states")
async def list_states():
    """List all states with policy data"""
    kb_service = await get_kb_service()
    states = await kb_service.get_all_states()
    
    # Get summary for each state
    state_info = []
    for state in states:
        summary = await kb_service.get_state_summary(state)
        state_info.append({
            "state": state,
            "policy_count": summary.get("total_policies", 0),
            "total_budget": summary.get("total_budget", 0),
            "categories": list(summary.get("categories", {}).keys())
        })
    
    return {
        "total_states": len(states),
        "states": state_info
    }

@router.get("/policy/{state}/{category}/{policy_key}")
async def get_policy(state: str, category: str, policy_key: str):
    """Get specific policy details"""
    kb_service = await get_kb_service()
    policy = await kb_service.get_policy(state, category, policy_key)
    
    if not policy:
        raise HTTPException(
            status_code=404,
            detail=f"Policy not found: {state}/{category}/{policy_key}"
        )
    
    return {
        "state": state,
        "category": category,
        "policy_key": policy_key,
        "policy": policy
    }

@router.get("/state/{state}")
async def get_state_policies(state: str):
    """Get all policies for a specific state"""
    kb_service = await get_kb_service()
    policies = await kb_service.get_state_policies(state)
    
    if not policies:
        raise HTTPException(
            status_code=404,
            detail=f"No policies found for state: {state}"
        )
    
    # Group by category
    grouped = {}
    for policy in policies:
        category = policy.get("category", "other")
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(policy)
    
    return {
        "state": state,
        "total_policies": len(policies),
        "categories": grouped
    }

@router.get("/state/{state}/summary")
async def get_state_summary(state: str):
    """Get summary statistics for a state"""
    kb_service = await get_kb_service()
    summary = await kb_service.get_state_summary(state)
    
    if not summary or summary.get("total_policies", 0) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for state: {state}"
        )
    
    return summary

@router.get("/search")
async def search_policies(
    q: str = Query(..., min_length=2, description="Search query"),
    limit: int = Query(50, ge=1, le=100, description="Maximum results")
):
    """Full-text search across all policies"""
    kb_service = await get_kb_service()
    results = await kb_service.search_policies(q, limit=limit)
    
    return {
        "query": q,
        "total_results": len(results),
        "results": results
    }

@router.get("/related")
async def get_related_policies(
    type: str = Query(..., description="Policy type or keyword"),
    state: Optional[str] = Query(None, description="Filter by state"),
    limit: int = Query(10, ge=1, le=50)
):
    """Get related policies by type"""
    kb_service = await get_kb_service()
    related = await kb_service.get_related_policies(type, state, limit=limit)
    
    return {
        "policy_type": type,
        "state": state or "all",
        "total_related": len(related),
        "related_policies": related
    }

@router.get("/budget/{state}")
async def get_budget(state: str, year: str = "2025_26"):
    """Get budget data for a state"""
    kb_service = await get_kb_service()
    budget = await kb_service.get_budget_data(state, year)
    
    if not budget:
        raise HTTPException(
            status_code=404,
            detail=f"Budget data not found for {state} ({year})"
        )
    
    return {
        "state": state,
        "year": year,
        "budget": budget
    }

@router.get("/national/{category}")
async def get_national_policies(category: str):
    """Get national policies by category"""
    valid_categories = ["economic", "social", "infrastructure", "agriculture", "education"]
    
    if category not in valid_categories:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Must be one of: {', '.join(valid_categories)}"
        )
    
    kb_service = await get_kb_service()
    policies = await kb_service.get_national_policies(category)
    
    return {
        "category": category,
        "total_policies": len(policies),
        "policies": policies
    }

@router.get("/top-budget")
async def get_top_by_budget(limit: int = Query(10, ge=1, le=50)):
    """Get policies with highest budget allocations"""
    kb_service = await get_kb_service()
    policies = await kb_service.get_top_policies_by_budget(limit=limit)
    
    return {
        "total_results": len(policies),
        "policies": policies
    }

@router.get("/impact/{area}")
async def get_by_impact_area(area: str):
    """Get policies by impact area"""
    kb_service = await get_kb_service()
    policies = await kb_service.get_policies_by_impact_area(area)
    
    return {
        "impact_area": area,
        "total_policies": len(policies),
        "policies": policies
    }

@router.get("/statistics")
async def get_statistics():
    """Get overall knowledge base statistics"""
    kb_service = await get_kb_service()
    stats = await kb_service.get_statistics()
    
    return stats
