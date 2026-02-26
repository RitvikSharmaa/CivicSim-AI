# 🚀 Online Deployment Guide

## Quick Deploy (100% FREE)

This guide will help you deploy CivicSim AI online using free platforms:
- **Frontend**: Vercel (FREE)
- **Backend**: Railway (FREE)
- **Database**: MongoDB Atlas (FREE)

---

## 📋 Prerequisites

1. GitHub account (you have this ✅)
2. Vercel account (free)
3. Railway account (free)
4. MongoDB Atlas account (you have this ✅)

---

## 🎯 Step-by-Step Deployment

### Part 1: Deploy Backend (Railway)

#### 1. Create Railway Account
1. Go to https://railway.app
2. Click "Login" → "Login with GitHub"
3. Authorize Railway

#### 2. Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `RitvikSharmaa/CivicSim-AI`
4. Railway will auto-detect Python

#### 3. Configure Environment Variables
Click on your service → "Variables" → Add these:

```env
MONGODB_URI=mongodb+srv://n8nconnection:Ritvik@123@cluster0.yqe4zmx.mongodb.net/?appName=Cluster0
MONGODB_DB_NAME=civicsim_ai
DEMO_MODE=true
OPENROUTER_API_KEY=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
OPENROUTER_MODEL=arcee-ai/trinity-large-preview:free
SECRET_KEY=civicsim-ai-production-secret-key-2026-india
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALLOWED_ORIGINS=https://your-frontend-url.vercel.app
HOST=0.0.0.0
PORT=8000
WORKERS=2
LOG_LEVEL=INFO
ENABLE_CACHING=true
CACHE_TTL=3600
```

#### 4. Configure Build Settings
1. Go to "Settings" → "Build"
2. Root Directory: `backend`
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --timeout 120`

#### 5. Deploy
1. Click "Deploy"
2. Wait 3-5 minutes for deployment
3. Copy your Railway URL (e.g., `https://civicsim-ai-production.up.railway.app`)

#### 6. Test Backend
```bash
curl https://your-railway-url.railway.app/health
```

Should return:
```json
{
  "status": "healthy",
  "version": "2.0.0-production",
  "demo_mode": true,
  "agents": 6,
  "states_covered": 36,
  "ml_models": 6
}
```

---

### Part 2: Deploy Frontend (Vercel)

#### 1. Create Vercel Account
1. Go to https://vercel.com
2. Click "Sign Up" → "Continue with GitHub"
3. Authorize Vercel

#### 2. Import Project
1. Click "Add New..." → "Project"
2. Import `RitvikSharmaa/CivicSim-AI`
3. Vercel will auto-detect Next.js

#### 3. Configure Project
1. **Root Directory**: `frontend`
2. **Framework Preset**: Next.js
3. **Build Command**: `npm run build`
4. **Output Directory**: `.next`

#### 4. Add Environment Variable
Click "Environment Variables" → Add:
```
NEXT_PUBLIC_API_URL=https://your-railway-url.railway.app
```
(Use the Railway URL from Part 1)

#### 5. Deploy
1. Click "Deploy"
2. Wait 2-3 minutes
3. Your site will be live at `https://your-project.vercel.app`

#### 6. Update Backend CORS
Go back to Railway → Variables → Update:
```
ALLOWED_ORIGINS=https://your-project.vercel.app,http://localhost:3000
```

---

## 🎉 Your App is Live!

### URLs
- **Frontend**: https://your-project.vercel.app
- **Backend**: https://your-railway-url.railway.app
- **API Docs**: https://your-railway-url.railway.app/api/docs

---

## 🔧 Alternative: Deploy with Render (Backend)

If Railway doesn't work, use Render:

#### 1. Create Render Account
1. Go to https://render.com
2. Sign up with GitHub

#### 2. Create Web Service
1. Click "New +" → "Web Service"
2. Connect `RitvikSharmaa/CivicSim-AI`
3. Configure:
   - **Name**: civicsim-ai-backend
   - **Root Directory**: `backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`

#### 3. Add Environment Variables
Same as Railway (see above)

#### 4. Deploy
Click "Create Web Service"

---

## 🔧 Alternative: Deploy with Netlify (Frontend)

If Vercel doesn't work, use Netlify:

#### 1. Create Netlify Account
1. Go to https://netlify.com
2. Sign up with GitHub

#### 2. Import Project
1. Click "Add new site" → "Import an existing project"
2. Choose GitHub → Select `RitvikSharmaa/CivicSim-AI`
3. Configure:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/.next`

#### 3. Add Environment Variable
Site settings → Environment variables:
```
NEXT_PUBLIC_API_URL=https://your-backend-url
```

---

## 📊 Monitoring & Maintenance

### Check Backend Health
```bash
curl https://your-backend-url/health
```

### View Logs
- **Railway**: Dashboard → Logs
- **Vercel**: Dashboard → Deployments → View Function Logs
- **Render**: Dashboard → Logs

### Update Deployment
Just push to GitHub:
```bash
git add .
git commit -m "Update feature"
git push origin main
```

Both Vercel and Railway will auto-deploy!

---

## 🎯 Custom Domain (Optional)

### Vercel
1. Go to Project Settings → Domains
2. Add your domain
3. Update DNS records as instructed

### Railway
1. Go to Settings → Domains
2. Add custom domain
3. Update DNS records

---

## 🔒 Security Checklist

Before going live:
- [ ] Update SECRET_KEY in backend
- [ ] Enable HTTPS (automatic on Vercel/Railway)
- [ ] Set proper CORS origins
- [ ] Review environment variables
- [ ] Test all endpoints
- [ ] Monitor error logs

---

## 💰 Cost Breakdown

### FREE Tier Limits
- **Vercel**: 100GB bandwidth/month, unlimited projects
- **Railway**: $5 free credit/month (~500 hours)
- **MongoDB Atlas**: 512MB storage, shared cluster
- **Render**: 750 hours/month free

### If You Exceed Free Tier
- **Vercel Pro**: $20/month
- **Railway**: Pay as you go ($0.000231/GB-hour)
- **MongoDB Atlas**: $9/month for 2GB
- **Render**: $7/month for 400 hours

---

## 🐛 Troubleshooting

### Backend Won't Start
1. Check logs in Railway/Render
2. Verify environment variables
3. Check MongoDB connection
4. Ensure ML models are included

### Frontend Can't Connect to Backend
1. Check NEXT_PUBLIC_API_URL
2. Verify CORS settings in backend
3. Test backend health endpoint
4. Check browser console for errors

### Slow Performance
1. Enable caching (ENABLE_CACHING=true)
2. Reduce workers if memory limited
3. Optimize ML model loading
4. Use CDN for static assets

---

## 📞 Quick Commands

### Test Backend
```bash
# Health check
curl https://your-backend-url/health

# Get states
curl https://your-backend-url/india/states

# Test simulation
curl -X POST https://your-backend-url/simulation/simulate \
  -H "Content-Type: application/json" \
  -d '{
    "policy_text": "Increase metro budget by ₹5000 crore",
    "region": {"state": "Karnataka"},
    "enable_optimization": true
  }'
```

### View Logs
```bash
# Railway CLI
railway logs

# Vercel CLI
vercel logs
```

---

## 🎉 Success Checklist

- [ ] Backend deployed on Railway/Render
- [ ] Frontend deployed on Vercel/Netlify
- [ ] MongoDB Atlas connected
- [ ] Environment variables set
- [ ] CORS configured
- [ ] Health check passing
- [ ] Frontend can reach backend
- [ ] Simulation working
- [ ] Custom domain (optional)

---

## 📚 Resources

- **Railway Docs**: https://docs.railway.app
- **Vercel Docs**: https://vercel.com/docs
- **Render Docs**: https://render.com/docs
- **MongoDB Atlas**: https://docs.atlas.mongodb.com

---

## 🚀 Your App is Ready!

Once deployed, share your live URLs:
- **Live App**: https://your-project.vercel.app
- **API Docs**: https://your-backend-url/api/docs
- **GitHub**: https://github.com/RitvikSharmaa/CivicSim-AI

---

**Built with ❤️ for Indian Government • 100% FREE & Open Source**

**Deployed and Ready to Use! 🎉**
