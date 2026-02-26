#!/bin/bash

# Production startup script for CivicSim AI

echo "🚀 Starting CivicSim AI - Production Mode"
echo "=========================================="

# Create logs directory
mkdir -p logs

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found! Copying from .env.example..."
    cp .env.example .env
    echo "✅ Please update .env with your configuration"
    exit 1
fi

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate || . venv/Scripts/activate

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt --quiet

# Check if ML models exist
if [ ! -f "backend/app/ml/models/india_behavior_lstm.pth" ]; then
    echo "⚠️  ML models not found! Training models..."
    python app/ml/train_india_models.py
fi

# Start server with Gunicorn
echo "🚀 Starting FastAPI server with Gunicorn..."
echo "📍 API: http://localhost:8000"
echo "📚 Docs: http://localhost:8000/api/docs"
echo "=========================================="

gunicorn app.main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --access-logfile logs/access.log \
    --error-logfile logs/error.log \
    --log-level info
