#!/bin/bash

# Build script for Render deployment

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Creating ML model..."
cd model
python create_model.py
cd ..

echo "Installing frontend dependencies..."
cd frontend
npm install
npm run build
cd ..

echo "Build completed successfully!"