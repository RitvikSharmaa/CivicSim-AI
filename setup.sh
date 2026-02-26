#!/bin/bash

echo "🚀 Setting up CivicSim AI..."

# Backend setup
echo "📦 Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  Please edit backend/.env with your MongoDB credentials"
fi

cd ..

# Frontend setup
echo "📦 Setting up frontend..."
cd frontend
npm install
cd ..

echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo "1. Backend: cd backend && uvicorn app.main:app --reload"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "Or use Docker: docker-compose up"
