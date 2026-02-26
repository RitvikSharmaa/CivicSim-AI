"""
FREE Caching Service - No Redis needed!
Uses Python's built-in functools.lru_cache for in-memory caching
"""

from functools import lru_cache, wraps
from typing import Any, Callable
import time
import hashlib
import json

# Simple in-memory cache with TTL
_cache = {}
_cache_timestamps = {}

def timed_cache(ttl_seconds: int = 300):
    """
    Decorator for caching with TTL (Time To Live)
    FREE alternative to Redis - uses in-memory caching
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key from function name and arguments
            cache_key = _create_cache_key(func.__name__, args, kwargs)
            
            # Check if cached and not expired
            if cache_key in _cache:
                timestamp = _cache_timestamps.get(cache_key, 0)
                if time.time() - timestamp < ttl_seconds:
                    return _cache[cache_key]
            
            # Call function and cache result
            result = func(*args, **kwargs)
            _cache[cache_key] = result
            _cache_timestamps[cache_key] = time.time()
            
            return result
        
        return wrapper
    return decorator

def _create_cache_key(func_name: str, args: tuple, kwargs: dict) -> str:
    """Create a unique cache key from function name and arguments"""
    key_data = {
        "func": func_name,
        "args": str(args),
        "kwargs": str(sorted(kwargs.items()))
    }
    key_string = json.dumps(key_data, sort_keys=True)
    return hashlib.md5(key_string.encode()).hexdigest()

def clear_cache():
    """Clear all cached data"""
    _cache.clear()
    _cache_timestamps.clear()

def get_cache_stats() -> dict:
    """Get cache statistics"""
    return {
        "total_entries": len(_cache),
        "memory_usage_mb": sum(len(str(v)) for v in _cache.values()) / (1024 * 1024),
        "oldest_entry_age": time.time() - min(_cache_timestamps.values()) if _cache_timestamps else 0
    }

# Pre-cache frequently accessed data
@lru_cache(maxsize=256)
def get_cached_city_list():
    """Cache city list - rarely changes - ALL 36 CITIES"""
    from app.services.free_india_data import india_data_service
    return india_data_service.get_available_cities()

@lru_cache(maxsize=64)
def get_cached_states_list():
    """Cache states list - ALL 28 STATES + 8 UTs"""
    from app.services.free_india_data import india_data_service
    return india_data_service.get_states_list()

@lru_cache(maxsize=512)
def get_cached_city_data(state: str, city: str):
    """Cache city data - static data - ALL CITIES"""
    from app.services.free_india_data import india_data_service
    return india_data_service.get_city_data(state, city)

@lru_cache(maxsize=256)
def get_cached_traffic_data(city: str):
    """Cache traffic data - updates infrequently - ALL CITIES"""
    from app.services.free_india_data import india_data_service
    return india_data_service.get_traffic_data(city)

@lru_cache(maxsize=32)
def get_cached_economic_data():
    """Cache economic indicators - updates daily"""
    from app.services.free_india_data import india_data_service
    return india_data_service.get_economic_indicators()
