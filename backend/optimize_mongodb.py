"""
MongoDB Optimization Script
- Remove unnecessary collections
- Optimize indexes
- Clean up old data
- Compact database
"""

import asyncio
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def optimize_database():
    """Optimize MongoDB database"""
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.database_name]
    
    try:
        logger.info("🔧 Starting database optimization...")
        
        # 1. List all collections
        collections = await db.list_collection_names()
        logger.info(f"📊 Found collections: {collections}")
        
        # 2. Keep only necessary collections
        necessary_collections = ["policies", "schemes", "economic_data"]
        
        for collection in collections:
            if collection not in necessary_collections:
                # Check if it's a simulation/log collection
                if collection in ["agent_logs", "indian_simulations", "optimization_results", "simulations"]:
                    count = await db[collection].count_documents({})
                    logger.info(f"   {collection}: {count} documents")
                    
                    # Keep only recent data (last 100 records)
                    if count > 100:
                        # Get oldest documents
                        cursor = db[collection].find().sort("_id", 1).limit(count - 100)
                        old_docs = await cursor.to_list(length=count - 100)
                        old_ids = [doc["_id"] for doc in old_docs]
                        
                        result = await db[collection].delete_many({"_id": {"$in": old_ids}})
                        logger.info(f"   ✅ Deleted {result.deleted_count} old documents from {collection}")
        
        # 3. Optimize policies collection
        logger.info("\n📚 Optimizing policies collection...")
        
        # Remove duplicate policies
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "state": "$state",
                        "category": "$category",
                        "policy_key": "$policy_key"
                    },
                    "ids": {"$push": "$_id"},
                    "count": {"$sum": 1}
                }
            },
            {
                "$match": {"count": {"$gt": 1}}
            }
        ]
        
        cursor = db.policies.aggregate(pipeline)
        duplicates = await cursor.to_list(length=None)
        
        if duplicates:
            logger.info(f"   Found {len(duplicates)} duplicate policy groups")
            for dup in duplicates:
                # Keep first, delete rest
                ids_to_delete = dup["ids"][1:]
                result = await db.policies.delete_many({"_id": {"$in": ids_to_delete}})
                logger.info(f"   ✅ Removed {result.deleted_count} duplicates")
        else:
            logger.info("   ✅ No duplicates found")
        
        # 4. Create/update indexes
        logger.info("\n🔍 Optimizing indexes...")
        
        # Drop old indexes
        existing_indexes = await db.policies.index_information()
        for index_name in existing_indexes:
            if index_name != "_id_":
                await db.policies.drop_index(index_name)
                logger.info(f"   Dropped old index: {index_name}")
        
        # Create optimized indexes
        await db.policies.create_index([
            ("name", "text"),
            ("objective", "text"),
            ("impact_areas", "text"),
            ("department", "text")
        ], name="text_search_optimized", weights={
            "name": 10,
            "objective": 5,
            "impact_areas": 3,
            "department": 1
        })
        logger.info("   ✅ Created weighted text search index")
        
        await db.policies.create_index([("state", 1), ("category", 1)], name="state_category")
        logger.info("   ✅ Created state-category index")
        
        await db.policies.create_index([("level", 1)], name="level")
        logger.info("   ✅ Created level index")
        
        await db.policies.create_index([("budget_allocation", -1)], name="budget_desc")
        logger.info("   ✅ Created budget index")
        
        await db.policies.create_index([("launched", -1)], name="launched_desc")
        logger.info("   ✅ Created launch date index")
        
        # 5. Get final statistics
        logger.info("\n📊 Final Statistics:")
        total_policies = await db.policies.count_documents({})
        logger.info(f"   Total Policies: {total_policies}")
        
        # Size by collection
        stats = await db.command("dbStats")
        logger.info(f"   Database Size: {stats['dataSize'] / 1024 / 1024:.2f} MB")
        logger.info(f"   Index Size: {stats['indexSize'] / 1024 / 1024:.2f} MB")
        
        logger.info("\n✅ Database optimization complete!")
        
    except Exception as e:
        logger.error(f"❌ Optimization failed: {e}")
        raise
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(optimize_database())
