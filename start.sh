#!/bin/bash

# Start script for production
echo "Starting Vehicle Type Classification API..."

# Set production environment
export FLASK_ENV=production
export PORT=${PORT:-5000}

# Start the Flask app with Gunicorn
cd backend
gunicorn --bind 0.0.0.0:$PORT --timeout 120 --workers 1 app:app