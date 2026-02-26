# 🚀 Deployment Guide - CivicSim AI

## Deployment Options

### Option 1: Local Development (Recommended for Hackathon)

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Option 2: Docker Compose (Easiest)

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Services:
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- MongoDB: localhost:27017

### Option 3: Cloud Deployment

#### Backend → Google Cloud Run

```bash
# Build container
docker build -t civicsim-backend .

# Tag for GCR
docker tag civicsim-backend gcr.io/PROJECT_ID/civicsim-backend

# Push to GCR
docker push gcr.io/PROJECT_ID/civicsim-backend

# Deploy to Cloud Run
gcloud run deploy civicsim-backend \
  --image gcr.io/PROJECT_ID/civicsim-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars MONGODB_URL=$MONGODB_URL,SECRET_KEY=$SECRET_KEY
```

#### Frontend → Vercel

```bash
cd frontend

# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

Or connect GitHub repo to Vercel dashboard for auto-deployment.

#### Database → MongoDB Atlas

1. Create cluster at https://cloud.mongodb.com
2. Configure network access (allow all IPs for demo: 0.0.0.0/0)
3. Create database user
4. Get connection string
5. Update environment variables

### Option 4: AWS Deployment

#### Backend → AWS Lambda + API Gateway

```bash
# Install Serverless Framework
npm install -g serverless

# Create serverless.yml
# Deploy
serverless deploy
```

#### Frontend → AWS Amplify

```bash
# Install Amplify CLI
npm install -g @aws-amplify/cli

# Initialize
amplify init

# Add hosting
amplify add hosting

# Deploy
amplify publish
```

## Environment Configuration

### Production Environment Variables

#### Backend (.env)
```env
MONGODB_URL=mongodb+srv://user:pass@cluster.mongodb.net/
DATABASE_NAME=civicsim_ai_prod
SECRET_KEY=<generate-strong-key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENAI_API_KEY=<your-key>
DEMO_MODE=false
```

#### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

### Generate Secret Key

```python
import secrets
print(secrets.token_urlsafe(32))
```

## Database Setup

### MongoDB Atlas Configuration

1. **Create Cluster**
   - Choose free tier (M0)
   - Select region closest to users
   - Name: civicsim-cluster

2. **Database Access**
   - Create user: civicsim_user
   - Set strong password
   - Grant read/write access

3. **Network Access**
   - Development: Add your IP
   - Production: Add cloud service IPs
   - Demo: 0.0.0.0/0 (not recommended for production)

4. **Create Database**
   - Database name: civicsim_ai
   - Collections: policies, simulations, agent_logs

5. **Indexes** (for performance)
```javascript
// In MongoDB shell
db.simulations.createIndex({ "timestamp": -1 })
db.simulations.createIndex({ "policy_id": 1 })
db.policies.createIndex({ "created_at": -1 })
```

## Performance Optimization

### Backend

1. **Enable Caching**
```python
# Add to main.py
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="civicsim")
```

2. **Connection Pooling**
```python
# In db.py
client = AsyncIOMotorClient(
    settings.mongodb_url,
    maxPoolSize=50,
    minPoolSize=10
)
```

3. **Async Workers**
```bash
# Use multiple workers
uvicorn app.main:app --workers 4
```

### Frontend

1. **Build Optimization**
```bash
npm run build
npm start
```

2. **CDN for Static Assets**
- Use Vercel Edge Network
- Or configure CloudFront

3. **Image Optimization**
- Use Next.js Image component
- Enable automatic optimization

## Monitoring & Logging

### Backend Logging

```python
# Add to main.py
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    'civicsim.log',
    maxBytes=10000000,
    backupCount=5
)
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Error Tracking

```bash
# Install Sentry
pip install sentry-sdk

# Add to main.py
import sentry_sdk
sentry_sdk.init(dsn="YOUR_SENTRY_DSN")
```

### Health Checks

```python
# Already implemented in main.py
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

## Security Checklist

- [ ] Use HTTPS in production
- [ ] Set strong SECRET_KEY
- [ ] Enable CORS only for trusted origins
- [ ] Implement rate limiting
- [ ] Add input validation
- [ ] Use environment variables for secrets
- [ ] Enable MongoDB authentication
- [ ] Whitelist IP addresses
- [ ] Implement JWT authentication
- [ ] Add API key authentication
- [ ] Enable request logging
- [ ] Set up firewall rules

## Scaling Strategies

### Horizontal Scaling

1. **Backend**
   - Deploy multiple instances
   - Use load balancer
   - Session management with Redis

2. **Database**
   - MongoDB sharding
   - Read replicas
   - Connection pooling

### Vertical Scaling

1. **Increase Resources**
   - More CPU cores
   - More RAM
   - Faster storage

2. **Optimize Code**
   - Vectorized operations
   - Batch processing
   - Async operations

## Backup Strategy

### Automated Backups

```bash
# MongoDB Atlas: Enable automatic backups
# Retention: 7 days minimum

# Manual backup
mongodump --uri="mongodb+srv://..." --out=backup/
```

### Disaster Recovery

1. Regular backups (daily)
2. Test restore procedures
3. Multi-region deployment
4. Database replication

## Cost Optimization

### Free Tier Resources

- MongoDB Atlas: M0 (512MB)
- Vercel: Hobby plan
- Google Cloud Run: 2M requests/month free
- AWS Lambda: 1M requests/month free

### Estimated Costs (Production)

- MongoDB Atlas M10: ~$57/month
- Cloud Run: ~$10-50/month
- Vercel Pro: $20/month
- Total: ~$87-127/month

## Troubleshooting

### Common Issues

1. **MongoDB Connection Timeout**
   - Check network access settings
   - Verify connection string
   - Ensure IP is whitelisted

2. **CORS Errors**
   - Update allowed origins in main.py
   - Check frontend API URL

3. **Module Import Errors**
   - Verify all dependencies installed
   - Check Python version (3.11+)

4. **Port Conflicts**
   - Change ports in configuration
   - Kill existing processes

### Debug Mode

```bash
# Backend with debug logging
uvicorn app.main:app --reload --log-level debug

# Frontend with verbose output
npm run dev -- --verbose
```

## CI/CD Pipeline

### GitHub Actions Example

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy civicsim-backend \
            --image gcr.io/${{ secrets.GCP_PROJECT }}/civicsim-backend

  deploy-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        run: vercel --prod --token=${{ secrets.VERCEL_TOKEN }}
```

## Post-Deployment Checklist

- [ ] All services running
- [ ] Health checks passing
- [ ] Database connected
- [ ] API endpoints responding
- [ ] Frontend loading correctly
- [ ] Test simulation working
- [ ] Monitoring active
- [ ] Backups configured
- [ ] SSL certificate valid
- [ ] DNS configured
- [ ] Error tracking enabled
- [ ] Performance acceptable

## Support & Maintenance

### Regular Tasks

- Monitor error logs daily
- Check performance metrics weekly
- Update dependencies monthly
- Review security patches
- Backup verification
- Cost optimization review

### Emergency Contacts

- MongoDB Support: support.mongodb.com
- Vercel Support: vercel.com/support
- Google Cloud Support: cloud.google.com/support

---

**Ready for deployment!** 🚀

For hackathon demo, use Option 1 (Local) or Option 2 (Docker).
For production, use Option 3 (Cloud) with proper security.
