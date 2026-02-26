@echo off
REM Production startup script for CivicSim AI (Windows)

echo 🚀 Starting CivicSim AI - Production Mode
echo ==========================================

REM Create logs directory
if not exist logs mkdir logs

REM Check if .env exists
if not exist .env (
    echo ⚠️  .env file not found! Copying from .env.example...
    copy .env.example .env
    echo ✅ Please update .env with your configuration
    exit /b 1
)

REM Check Python version
python --version

REM Check if virtual environment exists
if not exist venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install/update dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt --quiet

REM Check if ML models exist
if not exist backend\app\ml\models\india_behavior_lstm.pth (
    echo ⚠️  ML models not found! Training models...
    python app\ml\train_india_models.py
)

REM Start server with Uvicorn (Gunicorn not available on Windows)
echo 🚀 Starting FastAPI server...
echo 📍 API: http://localhost:8000
echo 📚 Docs: http://localhost:8000/api/docs
echo ==========================================

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1
