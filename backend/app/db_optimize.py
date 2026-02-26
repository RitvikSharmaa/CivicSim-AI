"""
Database Optimization Script
Adds indexes for faster queries - 100% FREE (MongoDB Atlas free tier)
"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def optimize_database():
    """Add indexes to MongoDB collections for faster queries"""
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.database_name]
    
    logger.info("Starting database optimization...")
    
    # Indexes for indian_simulations collection
    logger.info("Creating indexes for indian_simulations...")
    await db.indian_simulations.create_index("timestamp")
    await db.indian_simulations.create_index([("region.state", 1), ("region.city", 1)])
    await db.indian_simulations.create_index("real_data_used")
    await db.indian_simulations.create_index([("timestamp", -1)])  # Descending for recent queries
    
    # Indexes for policies collection
    logger.info("Creating indexes for policies...")
    await db.policies.create_index("created_at")
    await db.policies.create_index("status")
    await db.policies.create_index([("created_at", -1)])
    
    # Indexes for simulations collection
    logger.info("Creating indexes for simulations...")
    await db.simulations.create_index("policy_id")
    await db.simulations.create_index("timestamp")
    await db.simulations.create_index([("timestamp", -1)])
    
    # Indexes for optimization_results collection
    logger.info("Creating indexes for optimization_results...")
    await db.optimization_results.create_index("original_policy_id")
    await db.optimization_results.create_index("reward_score")
    
    # Indexes for agent_logs collection
    logger.info("Creating indexes for agent_logs...")
    await db.agent_logs.create_index("agent_name")
    await db.agent_logs.create_index("timestamp")
    await db.agent_logs.create_index([("timestamp", -1)])
    
    # Compound indexes for common queries
    logger.info("Creating compound indexes...")
    await db.indian_simulations.create_index([
        ("region.state", 1), 
        ("region.city", 1), 
        ("timestamp", -1)
    ])
    
    logger.info("✅ Database optimization complete!")
    logger.info("All indexes created for faster queries (FREE on MongoDB Atlas)")
    
    # Get collection stats
    stats = await db.command("dbstats")
    logger.info(f"Database size: {stats.get('dataSize', 0) / (1024*1024):.2f} MB")
    logger.info(f"Index size: {stats.get('indexSize', 0) / (1024*1024):.2f} MB")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(optimize_database())
