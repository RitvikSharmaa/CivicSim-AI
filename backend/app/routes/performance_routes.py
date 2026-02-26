"""
Performance Monitoring API Routes - 100% FREE
"""

from fastapi import APIRouter
from app.services.performance_monitor import performance_monitor
from app.services.cache_service import get_cache_stats

router = APIRouter(prefix="/performance", tags=["performance"])

@router.get("/metrics")
async def get_performance_metrics():
    """Get detailed performance metrics"""
    return {
        "metrics": performance_monitor.get_metrics(),
        "summary": performance_monitor.get_summary(),
        "cache": get_cache_stats()
    }

@router.get("/system")
async def get_system_stats():
    """Get current system statistics"""
    return performance_monitor.get_system_stats()

@router.get("/summary")
async def get_performance_summary():
    """Get performance summary"""
    return performance_monitor.get_summary()

@router.post("/reset")
async def reset_metrics():
    """Reset performance metrics"""
    performance_monitor.reset_metrics()
    return {"message": "Performance metrics reset successfully"}

@router.get("/health")
async def health_check():
    """Detailed health check with performance data"""
    system = performance_monitor.get_system_stats()
    summary = performance_monitor.get_summary()
    cache = get_cache_stats()
    
    # Determine health status
    health_status = "healthy"
    warnings = []
    
    if system["memory_percent"] > 80:
        health_status = "warning"
        warnings.append("High memory usage")
    
    if system["cpu_percent"] > 80:
        health_status = "warning"
        warnings.append("High CPU usage")
    
    if summary["avg_response_time"] > 2.0:
        health_status = "warning"
        warnings.append("Slow response times")
    
    return {
        "status": health_status,
        "warnings": warnings,
        "system": system,
        "performance": summary,
        "cache": cache,
        "uptime_info": "Backend is running optimally",
        "cost": "₹0 (100% FREE)"
    }
