"""Test MongoDB connection"""
import asyncio
from app.db import connect_to_mongo, close_mongo_connection

async def test_connection():
    try:
        await connect_to_mongo()
        print("✅ MongoDB connected successfully")
        await close_mongo_connection()
        return True
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_connection())
    exit(0 if result else 1)
