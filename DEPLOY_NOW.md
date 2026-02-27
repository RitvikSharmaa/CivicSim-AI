# 🚀 Deploy Your App NOW - Quick Guide

## ✅ Deployment Files Ready!

All deployment configurations have been pushed to GitHub. You can now deploy in 3 simple steps:

---

## 🎯 Option 1: One-Click Deploy (Easiest)

### Step 1: Deploy Frontend (Vercel)
1. Go to https://vercel.com/new
2. Click "Import Project"
3. Select `RitvikSharmaa/CivicSim-AI`
4. Set **Root Directory**: `frontend`
5. Add environment variable:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
   ```
6. Click "Deploy"
7. ✅ Frontend live in 2 minutes!

### Step 2: Deploy Backend (Railway)
1. Go to https://railway.app/new
2. Click "Deploy from GitHub repo"
3. Select `RitvikSharmaa/CivicSim-AI`
4. Railway auto-detects Python
5. Add environment variables (copy from backend/.env)
6. Click "Deploy"
7. ✅ Backend live in 3-5 minutes!

### Step 3: Connect Them
1. Copy Railway URL (e.g., `https://civicsim-ai.up.railway.app`)
2. Go to Vercel → Settings → Environment Variables
3. Update `NEXT_PUBLIC_API_URL` with Railway URL
4. Redeploy frontend
5. ✅ Done!

---

## 🎯 Option 2: CLI Deploy (Faster)

### Deploy Frontend (Vercel CLI)
```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
cd frontend
vercel --prod

# Set environment variable
vercel env add NEXT_PUBLIC_API_URL production
# Enter: https://your-railway-url.railway.app
```

### Deploy Backend (Railway CLI)
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link project
railway link

# Deploy
railway up

# Add environment variables
railway variables set MONGODB_URI="mongodb+srv://..."
railway variables set DEMO_MODE="true"
# ... (add all from backend/.env)
```

---

## 📋 Environment Variables Needed

### Backend (Railway/Render)
```env
MONGODB_URI=mongodb+srv://n8nconnection:Ritvik@123@cluster0.yqe4zmx.mongodb.net/?appName=Cluster0
MONGODB_DB_NAME=civicsim_ai
DEMO_MODE=true
OPENROUTER_API_KEY=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
OPENROUTER_MODEL=arcee-ai/trinity-large-preview:free
SECRET_KEY=civicsim-ai-production-secret-key-2026-india
ALLOWED_ORIGINS=https://your-frontend-url.vercel.app
PORT=8000
WORKERS=2
```

### Frontend (Vercel/Netlify)
```env
NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
```

---

## 🔗 Quick Links

### Deployment Platforms
- **Vercel**: https://vercel.com/new
- **Railway**: https://railway.app/new
- **Render**: https://render.com (alternative)
- **Netlify**: https://netlify.com (alternative)

### Your Repository
- **GitHub**: https://github.com/RitvikSharmaa/CivicSim-AI
- **Deployment Guide**: [DEPLOYMENT_ONLINE.md](DEPLOYMENT_ONLINE.md)

---

## ⏱️ Deployment Time

- **Frontend (Vercel)**: 2-3 minutes
- **Backend (Railway)**: 3-5 minutes
- **Total**: ~5-8 minutes

---

## ✅ Post-Deployment Checklist

After deployment:
- [ ] Test frontend URL
- [ ] Test backend health: `https://your-backend-url/health`
- [ ] Test API docs: `https://your-backend-url/api/docs`
- [ ] Run a simulation from frontend
- [ ] Check logs for errors
- [ ] Update README with live URLs

---

## 🎉 Your URLs

After deployment, you'll have:
- **Frontend**: `https://civicsim-ai.vercel.app`
- **Backend**: `https://civicsim-ai.up.railway.app`
- **API Docs**: `https://civicsim-ai.up.railway.app/api/docs`

---

## 🐛 Troubleshooting

### Frontend Can't Connect
- Check `NEXT_PUBLIC_API_URL` is set correctly
- Verify backend is running
- Check CORS settings in backend

### Backend Won't Start
- Check environment variables
- Verify MongoDB connection
- Check logs in Railway dashboard
- Ensure ML models are included

### 502 Bad Gateway
- Backend is starting (wait 1-2 minutes)
- Check Railway logs
- Verify Procfile is correct

---

## 💡 Pro Tips

1. **Use Railway for Backend** - Better for Python apps
2. **Use Vercel for Frontend** - Best for Next.js
3. **MongoDB Atlas** - Already configured
4. **Check Logs** - First place to debug
5. **Test Locally First** - Ensure everything works

---

## 📞 Need Help?

1. Check [DEPLOYMENT_ONLINE.md](DEPLOYMENT_ONLINE.md) for detailed guide
2. Review platform documentation
3. Check GitHub Issues
4. Test locally first

---

## 🚀 Ready to Deploy?

### Quick Start:
1. **Vercel**: https://vercel.com/new → Import `RitvikSharmaa/CivicSim-AI`
2. **Railway**: https://railway.app/new → Deploy from GitHub
3. **Connect**: Update environment variables
4. **Test**: Visit your URLs
5. **Share**: Tell the world!

---

**Your app will be live in less than 10 minutes! 🎉**

**Start here**: https://vercel.com/new

---

**Built with ❤️ for Indian Government • 100% FREE & Open Source**
