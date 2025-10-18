# CORS Troubleshooting Guide

## 🚨 Common CORS Issues and Solutions

### Problem: "Access to fetch at '...' has been blocked by CORS policy"

This happens when your frontend tries to connect to your backend but the browser blocks the request.

## ✅ Quick Fixes

### 1. **Check Backend CORS Configuration**
Make sure your Flask app has the correct CORS settings:

```python
from flask_cors import CORS

# In app.py
CORS(app, 
     origins=[
         "http://localhost:3000",
         "https://vehicle-type-classification-frontend.onrender.com"
     ],
     methods=['GET', 'POST', 'OPTIONS'],
     allow_headers=['Content-Type', 'Authorization']
)
```

### 2. **Test CORS Endpoint**
Visit this URL to test if CORS is working:
```
https://vehicle-type-classification.onrender.com/cors-test
```

### 3. **Check Environment Variables**
In your frontend deployment, make sure you set:
```
REACT_APP_API_URL=https://vehicle-type-classification.onrender.com
```

### 4. **Development vs Production URLs**
- **Development**: `http://localhost:5000`
- **Production**: `https://your-backend-url.onrender.com`

## 🔧 Testing CORS

### Browser Console Test
```javascript
fetch('https://vehicle-type-classification.onrender.com/cors-test')
  .then(response => response.json())
  .then(data => console.log('CORS working:', data))
  .catch(error => console.error('CORS error:', error));
```

### cURL Test
```bash
curl -X POST https://vehicle-type-classification.onrender.com/cors-test \
  -H "Origin: https://vehicle-type-classification-frontend.onrender.com" \
  -H "Content-Type: application/json"
```

## 🎯 Environment-Specific Solutions

### For Render Deployment:
1. **Backend Environment Variables**:
   - No special CORS variables needed
   
2. **Frontend Environment Variables**:
   ```
   REACT_APP_API_URL=https://vehicle-type-classification.onrender.com
   ```

### For Local Development:
1. **Start backend first**: `python app.py` (port 5000)
2. **Start frontend**: `npm start` (port 3000)
3. **URLs should be**: Frontend `http://localhost:3000` → Backend `http://localhost:5000`

## 🚨 Emergency Fix: Disable CORS (Development Only)

**⚠️ Warning: Only use this for local development!**

```python
# In app.py - ADD THIS ONLY FOR LOCAL TESTING
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
```

## 📝 Debugging Checklist

- [ ] Backend is running and accessible
- [ ] Frontend has correct `REACT_APP_API_URL` 
- [ ] Both services are deployed successfully
- [ ] CORS origins include your frontend URL
- [ ] Browser developer tools show the actual error
- [ ] Test the `/cors-test` endpoint directly

## 🔗 Useful Links

- [Flask-CORS Documentation](https://flask-cors.readthedocs.io/)
- [MDN CORS Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Render Environment Variables](https://render.com/docs/environment-variables)