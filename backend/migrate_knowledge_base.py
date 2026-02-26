"""
Migration script to populate MongoDB with policy knowledge base
Run this once to migrate from in-memory to MongoDB
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_settings
from app.knowledge.policy_knowledge_base import policy_kb
from app.services.knowledge_base_service import KnowledgeBaseService
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def migrate_policies():
    """Migrate all policies to MongoDB"""
    settings = get_settings()
    
    # Connect to MongoDB
    client = AsyncIOMotorClient(settings.mongodb_url)
    kb_service = KnowledgeBaseService(client, settings.database_name)
    
    try:
        # Initialize indexes
        logger.info("Creating indexes...")
        await kb_service.initialize_indexes()
        
        # Clear existing policies (optional - comment out if you want to keep existing)
        logger.info("Clearing existing policies...")
        await kb_service.policies_collection.delete_many({})
        
        all_policies = []
        
        # Migrate national policies
        logger.info("Migrating national policies...")
        for category, policies in policy_kb.policies["national"].items():
            for policy_key, policy_data in policies.items():
                doc = {
                    "level": "national",
                    "state": "national",
                    "category": category,
                    "policy_key": policy_key,
                    **policy_data
                }
                all_policies.append(doc)
        
        logger.info(f"Prepared {len(all_policies)} national policies")
        
        # Migrate state policies
        logger.info("Migrating state policies...")
        state_count = 0
        for state, state_data in policy_kb.policies.items():
            if state == "national":
                continue
            
            state_count += 1
            for category, policies in state_data.items():
                if category.startswith("budget_"):
                    # Handle budget documents separately
                    doc = {
                        "level": "state",
                        "state": state,
                        "document_type": "budget",
                        "year": category.replace("budget_", ""),
                        "category": "budget",
                        "policy_key": f"{state}_budget_{category}",
                        **policies
                    }
                    all_policies.append(doc)
                elif isinstance(policies, dict):
                    for policy_key, policy_data in policies.items():
                        doc = {
                            "level": "state",
                            "state": state,
                            "category": category,
                            "policy_key": policy_key,
                            **policy_data
                        }
                        all_policies.append(doc)
        
        logger.info(f"Prepared {len(all_policies)} total policies from {state_count} states")
        
        # Bulk insert all policies
        if all_policies:
            logger.info("Inserting policies into MongoDB...")
            inserted_count = await kb_service.bulk_insert_policies(all_policies)
            logger.info(f"✅ Successfully inserted {inserted_count} policies")
        
        # Get statistics
        stats = await kb_service.get_statistics()
        logger.info(f"\n📊 Knowledge Base Statistics:")
        logger.info(f"   Total Policies: {stats['total_policies']}")
        logger.info(f"   Total States: {stats['total_states']}")
        logger.info(f"   National Policies: {stats['national_policies']}")
        logger.info(f"   State Policies: {stats['state_policies']}")
        logger.info(f"   Total Budget: ₹{stats['total_budget_allocation']:,.0f}")
        
        # Test search
        logger.info("\n🔍 Testing search functionality...")
        search_results = await kb_service.search_policies("electricity", limit=5)
        logger.info(f"   Found {len(search_results)} results for 'electricity'")
        
        # Test state query
        logger.info("\n🏛️ Testing state query...")
        karnataka_policies = await kb_service.get_state_policies("Karnataka")
        logger.info(f"   Found {len(karnataka_policies)} policies for Karnataka")
        
        logger.info("\n✅ Migration completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Migration failed: {e}")
        raise
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(migrate_policies())
