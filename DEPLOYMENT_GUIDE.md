# 🚀 Deployment Guide - CivicSim AI

## Quick Start (Development)

### Backend
```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm run dev
```

Access: http://localhost:3000

---

## Production Deployment

### Option 1: Docker (Recommended)

```bash
# Build and run
docker-compose up -d

# Access
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
```

### Option 2: Manual Deployment

#### Backend (FastAPI)
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export MONGODB_URI="mongodb://localhost:27017"
export DEMO_MODE="true"

# Run with Gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

#### Frontend (Next.js)
```bash
cd frontend

# Install dependencies
npm install

# Build
npm run build

# Run production server
npm start
```

---

## Environment Variables

### Backend (.env)
```env
# MongoDB
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=civicsim_ai

# Demo Mode (set to false for LLM)
DEMO_MODE=true

# OpenRouter (optional)
OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=anthropic/claude-3-sonnet

# CORS
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## MongoDB Setup

### Local MongoDB
```bash
# Install MongoDB
# Windows: Download from mongodb.com
# Linux: sudo apt install mongodb

# Start MongoDB
mongod --dbpath /path/to/data

# Create indexes (optional)
mongo civicsim_ai
db.indian_simulations.createIndex({ "timestamp": -1 })
db.indian_simulations.createIndex({ "region.state": 1 })
```

### MongoDB Atlas (Cloud)
1. Create account at mongodb.com/cloud/atlas
2. Create free cluster
3. Get connection string
4. Update MONGODB_URI in .env

---

## Server Requirements

### Minimum
- CPU: 2 cores
- RAM: 4 GB
- Storage: 10 GB
- OS: Linux/Windows

### Recommended
- CPU: 4 cores
- RAM: 8 GB
- Storage: 20 GB
- OS: Ubuntu 22.04 LTS

---

## Deployment Platforms

### Vercel (Frontend)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd frontend
vercel --prod
```

### Railway (Backend + MongoDB)
1. Connect GitHub repo
2. Add MongoDB service
3. Set environment variables
4. Deploy

### AWS/GCP/Azure
- Use EC2/Compute Engine/VM
- Install Docker
- Run docker-compose
- Configure security groups
- Set up load balancer

---

## Performance Tuning

### Backend
```python
# app/main.py
app = FastAPI(
    title="CivicSim AI",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Add caching
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="civicsim")
```

### Frontend
```javascript
// next.config.js
module.exports = {
  compress: true,
  poweredByHeader: false,
  generateEtags: true,
  images: {
    domains: ['localhost'],
  },
}
```

---

## Monitoring

### Backend Logs
```bash
# View logs
tail -f logs/app.log

# With Docker
docker logs -f civicsim-backend
```

### Health Check
```bash
curl http://localhost:8000/health
```

---

## Troubleshooting

### Backend won't start
- Check Python version (3.13+)
- Verify MongoDB connection
- Check port 8000 availability
- Review logs

### Frontend won't build
- Clear .next folder
- Delete node_modules
- Run npm install
- Check Node version (18+)

### Models not loading
- Verify models exist in backend/backend/app/ml/models/
- Check file permissions
- Retrain if needed: `python app/ml/train_india_models.py`

### Slow performance
- Enable model caching (already done)
- Add Redis for API caching
- Use CDN for frontend
- Optimize MongoDB indexes

---

## Security Checklist

- [ ] Change default passwords
- [ ] Enable HTTPS/SSL
- [ ] Set up firewall rules
- [ ] Add rate limiting
- [ ] Enable CORS properly
- [ ] Sanitize user inputs
- [ ] Keep dependencies updated
- [ ] Regular backups

---

## Backup Strategy

### MongoDB Backup
```bash
# Backup
mongodump --db civicsim_ai --out /backup/$(date +%Y%m%d)

# Restore
mongorestore --db civicsim_ai /backup/20260227
```

### Code Backup
```bash
# Git backup
git push origin main

# Full backup
tar -czf civicsim-backup-$(date +%Y%m%d).tar.gz .
```

---

## Scaling

### Horizontal Scaling
- Multiple backend instances behind load balancer
- MongoDB replica set
- Redis cluster for caching
- CDN for static assets

### Vertical Scaling
- Increase server resources
- Optimize database queries
- Add more workers to Gunicorn
- Enable HTTP/2

---

## Support

For issues or questions:
- Check logs first
- Review this guide
- Test with curl/Postman
- Check MongoDB connection
- Verify environment variables

---

**Built with ❤️ for Indian Government • 100% FREE & Open Source**
