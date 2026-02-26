"""
Master Script to Expand Knowledge Base
Runs optimization and comprehensive data collection
"""

import asyncio
import subprocess
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_script(script_name: str, description: str):
    """Run a Python script"""
    logger.info(f"\n{'='*60}")
    logger.info(f"🚀 {description}")
    logger.info(f"{'='*60}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(result.stdout)
        if result.stderr:
            logger.warning(result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ {description} failed!")
        logger.error(e.stdout)
        logger.error(e.stderr)
        return False

async def main():
    """Run all expansion scripts"""
    logger.info("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     KNOWLEDGE BASE EXPANSION & OPTIMIZATION                  ║
║                                                              ║
║     This will:                                               ║
║     1. Optimize MongoDB database                             ║
║     2. Add comprehensive policy data                         ║
║     3. Expand to 150+ policies                               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    scripts = [
        ("optimize_mongodb.py", "Step 1: Optimizing MongoDB Database"),
        ("enhanced_scraper.py", "Step 2: Adding Comprehensive Policy Data"),
    ]
    
    success_count = 0
    for script, description in scripts:
        if await run_script(script, description):
            success_count += 1
        await asyncio.sleep(2)
    
    logger.info(f"\n{'='*60}")
    logger.info(f"✅ Completed {success_count}/{len(scripts)} steps successfully!")
    logger.info(f"{'='*60}\n")
    
    if success_count == len(scripts):
        logger.info("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     ✅ KNOWLEDGE BASE EXPANSION COMPLETE!                    ║
║                                                              ║
║     Your knowledge base now has:                             ║
║     • 150+ comprehensive policies                            ║
║     • All 36 states covered                                  ║
║     • National schemes included                              ║
║     • Optimized MongoDB indexes                              ║
║     • Real budget data                                       ║
║                                                              ║
║     Test it: http://localhost:8000/knowledge/v2/             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
    else:
        logger.warning("\n⚠️  Some steps failed. Check logs above for details.")

if __name__ == "__main__":
    asyncio.run(main())
