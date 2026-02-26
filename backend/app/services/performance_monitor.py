"""
Performance Monitoring Service - 100% FREE
No external services needed - uses Python's built-in tools
"""

import time
import logging
from functools import wraps
from typing import Callable, Dict, Any
import psutil
import os

logger = logging.getLogger(__name__)

# Performance metrics storage
_metrics = {
    "api_calls": {},
    "agent_execution": {},
    "ml_inference": {},
    "database_queries": {}
}

class PerformanceMonitor:
    """FREE performance monitoring using built-in Python tools"""
    
    @staticmethod
    def measure_time(category: str = "general"):
        """Decorator to measure execution time"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                start_time = time.time()
                start_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
                
                try:
                    result = await func(*args, **kwargs)
                    success = True
                except Exception as e:
                    success = False
                    raise e
                finally:
                    end_time = time.time()
                    end_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
                    
                    execution_time = end_time - start_time
                    memory_delta = end_memory - start_memory
                    
                    # Store metrics
                    func_name = func.__name__
                    if func_name not in _metrics[category]:
                        _metrics[category][func_name] = {
                            "calls": 0,
                            "total_time": 0,
                            "avg_time": 0,
                            "min_time": float('inf'),
                            "max_time": 0,
                            "memory_delta": 0,
                            "errors": 0
                        }
                    
                    metrics = _metrics[category][func_name]
                    metrics["calls"] += 1
                    metrics["total_time"] += execution_time
                    metrics["avg_time"] = metrics["total_time"] / metrics["calls"]
                    metrics["min_time"] = min(metrics["min_time"], execution_time)
                    metrics["max_time"] = max(metrics["max_time"], execution_time)
                    metrics["memory_delta"] = memory_delta
                    if not success:
                        metrics["errors"] += 1
                    
                    # Log slow operations
                    if execution_time > 1.0:
                        logger.warning(
                            f"SLOW: {category}.{func_name} took {execution_time:.2f}s"
                        )
                    else:
                        logger.info(
                            f"FAST: {category}.{func_name} took {execution_time:.3f}s"
                        )
                
                return result
            
            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                start_time = time.time()
                start_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
                
                try:
                    result = func(*args, **kwargs)
                    success = True
                except Exception as e:
                    success = False
                    raise e
                finally:
                    end_time = time.time()
                    end_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
                    
                    execution_time = end_time - start_time
                    memory_delta = end_memory - start_memory
                    
                    # Store metrics
                    func_name = func.__name__
                    if func_name not in _metrics[category]:
                        _metrics[category][func_name] = {
                            "calls": 0,
                            "total_time": 0,
                            "avg_time": 0,
                            "min_time": float('inf'),
                            "max_time": 0,
                            "memory_delta": 0,
                            "errors": 0
                        }
                    
                    metrics = _metrics[category][func_name]
                    metrics["calls"] += 1
                    metrics["total_time"] += execution_time
                    metrics["avg_time"] = metrics["total_time"] / metrics["calls"]
                    metrics["min_time"] = min(metrics["min_time"], execution_time)
                    metrics["max_time"] = max(metrics["max_time"], execution_time)
                    metrics["memory_delta"] = memory_delta
                    if not success:
                        metrics["errors"] += 1
                    
                    if execution_time > 1.0:
                        logger.warning(
                            f"SLOW: {category}.{func_name} took {execution_time:.2f}s"
                        )
                
                return result
            
            # Return appropriate wrapper
            import asyncio
            if asyncio.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper
        
        return decorator
    
    @staticmethod
    def get_metrics() -> Dict[str, Any]:
        """Get all performance metrics"""
        return _metrics
    
    @staticmethod
    def get_system_stats() -> Dict[str, Any]:
        """Get current system statistics"""
        process = psutil.Process(os.getpid())
        
        return {
            "cpu_percent": psutil.cpu_percent(interval=0.1),
            "memory_mb": process.memory_info().rss / 1024 / 1024,
            "memory_percent": process.memory_percent(),
            "threads": process.num_threads(),
            "open_files": len(process.open_files()),
        }
    
    @staticmethod
    def reset_metrics():
        """Reset all metrics"""
        for category in _metrics:
            _metrics[category].clear()
        logger.info("Performance metrics reset")
    
    @staticmethod
    def get_summary() -> Dict[str, Any]:
        """Get performance summary"""
        summary = {
            "total_api_calls": sum(m["calls"] for m in _metrics["api_calls"].values()),
            "total_agent_executions": sum(m["calls"] for m in _metrics["agent_execution"].values()),
            "total_ml_inferences": sum(m["calls"] for m in _metrics["ml_inference"].values()),
            "avg_response_time": 0,
            "system": PerformanceMonitor.get_system_stats()
        }
        
        # Calculate average response time
        all_times = []
        for category in _metrics.values():
            for metrics in category.values():
                if metrics["calls"] > 0:
                    all_times.append(metrics["avg_time"])
        
        if all_times:
            summary["avg_response_time"] = sum(all_times) / len(all_times)
        
        return summary

# Global instance
performance_monitor = PerformanceMonitor()
