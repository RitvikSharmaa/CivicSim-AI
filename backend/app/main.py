from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import connect_to_mongo, close_mongo_connection, db
from app.routes import policy_routes, simulation_routes, india_routes, performance_routes, knowledge_routes, knowledge_mongo_routes
from app.services.knowledge_base_service import initialize_kb_service
from app.config import get_settings
from app.logging_config import setup_logging
import logging

# Setup production logging
logger = setup_logging()

# Get settings
settings = get_settings()

app = FastAPI(
    title="CivicSim AI - India Policy Simulation Platform",
    description="Multi-Agent AI system for policy simulation across all 36 Indian states & UTs using 100% FREE data sources",
    version="2.0.0-production",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS with production settings
allowed_origins = settings.allowed_origins.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup/Shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("Starting CivicSim AI - India Edition")
    logger.info(f"Demo Mode: {settings.demo_mode}")
    logger.info(f"MongoDB URI: {settings.mongodb_uri[:20]}...")
    logger.info(f"Allowed Origins: {allowed_origins}")
    
    await connect_to_mongo()
    await initialize_kb_service(db.client, settings.mongodb_db_name)
    
    logger.info("✅ CivicSim AI backend started successfully!")
    logger.info("📊 6 AI Agents ready")
    logger.info("🇮🇳 36 States & UTs covered")
    logger.info("🤖 ML/DL models loaded and cached")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down CivicSim AI")
    await close_mongo_connection()
    logger.info("✅ Shutdown complete")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "2.0.0-production",
        "demo_mode": settings.demo_mode,
        "agents": 6,
        "states_covered": 36,
        "ml_models": 6
    }

# Include routers
app.include_router(policy_routes.router)
app.include_router(simulation_routes.router)
app.include_router(india_routes.router)
app.include_router(performance_routes.router)
app.include_router(knowledge_routes.router)
app.include_router(knowledge_mongo_routes.router)

@app.get("/")
async def root():
    return {
        "message": "CivicSim AI - AI Policy Sandbox (India Edition) - OPTIMIZED",
        "version": "2.0.0-india-optimized",
        "status": "operational",
        "features": [
            "Indian Rupees (₹) support",
            "Real Indian city data",
            "FREE data sources only",
            "Region-wise simulations",
            "Traffic congestion data",
            "Census demographics",
            "⚡ In-memory caching",
            "⚡ Model caching",
            "⚡ Database indexing",
            "⚡ Performance monitoring"
        ],
        "data_sources": [
            "Census India (FREE)",
            "TomTom Traffic Index (FREE)",
            "Reserve Bank of India (FREE)",
            "Data.gov.in (FREE)"
        ],
        "optimizations": [
            "LRU caching for static data",
            "Model weight caching",
            "Vectorized computations",
            "Database indexes",
            "Request deduplication"
        ],
        "cost": "₹0 (100% FREE)"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "edition": "India - OPTIMIZED", 
        "currency": "INR (₹)",
        "performance": "Enhanced with caching"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
