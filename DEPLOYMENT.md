# Render Deployment Guide

This guide will help you deploy the Vehicle Type Classification project on Render.

## Prerequisites

1. **GitHub Repository**: Push your code to a GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com)

## Deployment Steps

### Option 1: Using Render Dashboard (Recommended)

#### Step 1: Deploy Backend (Flask API)
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `vtc-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && cd model && python create_model.py`
   - **Start Command**: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Plan**: Free
5. Add Environment Variables:
   - `PYTHON_VERSION` = `3.11.0`
   - `FLASK_ENV` = `production`
6. Click "Create Web Service"

#### Step 2: Deploy Frontend (React App)
1. Click "New +" → "Web Service"
2. Connect the same GitHub repository
3. Configure the service:
   - **Name**: `vtc-frontend`
   - **Environment**: `Node`
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Start Command**: `cd frontend && npx serve -s build -p $PORT`
   - **Plan**: Free
4. Add Environment Variables:
   - `NODE_VERSION` = `18.17.0`
   - `REACT_APP_API_URL` = `https://vtc-backend.onrender.com`
5. Click "Create Web Service"

### Option 2: Using render.yaml (Infrastructure as Code)

1. The `render.yaml` file in your repository defines both services
2. In Render Dashboard:
   - Go to "Blueprint" → "New Blueprint Instance"
   - Connect your GitHub repository
   - Render will automatically deploy both services

## Important Files for Deployment

✅ **requirements.txt** - Python dependencies  
✅ **Procfile** - Process definition  
✅ **runtime.txt** - Python version specification  
✅ **render.yaml** - Render configuration  
✅ **build.sh** - Build script  

## Environment Variables

### Backend Environment Variables
- `PORT` - Automatically set by Render
- `PYTHON_VERSION` - `3.11.0`
- `FLASK_ENV` - `production`

### Frontend Environment Variables  
- `PORT` - Automatically set by Render
- `NODE_VERSION` - `18.17.0`
- `REACT_APP_API_URL` - Your backend URL (e.g., `https://vtc-backend.onrender.com`)

## Post-Deployment

1. **Test Backend**: Visit `https://your-backend-url.onrender.com/` for health check
2. **Test Frontend**: Visit `https://your-frontend-url.onrender.com/`
3. **Test API Integration**: Use the frontend to make predictions

## Troubleshooting

### Common Issues:

1. **Build Failures**:
   - Check build logs in Render dashboard
   - Verify all dependencies in requirements.txt/package.json
   - Ensure Python/Node versions are correct

2. **CORS Errors**:
   - Update `REACT_APP_API_URL` in frontend environment variables
   - Verify CORS settings in backend/app.py

3. **Model Loading Issues**:
   - Ensure model is created during build process
   - Check that build command includes `cd model && python create_model.py`

4. **Frontend API Calls Failing**:
   - Verify backend URL is accessible
   - Check environment variable `REACT_APP_API_URL`
   - Test backend endpoints directly

## URLs After Deployment

- **Backend API**: `https://vtc-backend.onrender.com`
- **Frontend App**: `https://vtc-frontend.onrender.com`
- **API Documentation**: `https://vtc-backend.onrender.com/model-info`

## Free Tier Limitations

- Services sleep after 15 minutes of inactivity
- Cold start times may be 30+ seconds
- 750 hours/month usage limit

## Production Recommendations

1. Use paid plans for consistent uptime
2. Set up custom domains
3. Configure environment-specific settings
4. Add monitoring and logging
5. Implement CI/CD pipeline

---

**Need Help?** Check [Render Documentation](https://render.com/docs) or [GitHub Issues](https://github.com/MohanR007/vtc/issues)