# 🚗 Vehicle Type Classification

A full-stack web application that uses machine learning to classify vehicle types based on physical characteristics. Built with React frontend and Flask backend.

![ML](https://img.shields.io/badge/ML-99.3%25_Accuracy-brightgreen) ![React](https://img.shields.io/badge/React-18.2.0-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.3-red)

## 🎯 Features

- **Frontend**: React with Tailwind CSS, responsive design, real-time validation
- **Backend**: Flask API with Random Forest classifier (99.2% accuracy) 
- **Vehicle Categories**: 17 detailed types including Scooter, Sports Bike, Sedan, Hatchback, Compact SUV, Pickup Truck, etc.
- **Input Features**: Length, Height, Width, Weight, Engine Power, Top Speed, Axles, Seats, Fuel Type

## 📁 Project Structure

```
vtc/
├── backend/         # Flask API (app.py, requirements.txt)
├── frontend/        # React app (src/, package.json)
├── model/          # ML model (create_model.py, vehicle_model.pkl)
└── .vscode/        # VS Code tasks and configuration
```

## 🚀 Quick Start

**Prerequisites:** Node.js (v14+), Python (v3.8+)

### VS Code Tasks (Recommended)
1. Open VS Code: `Ctrl+Shift+P` → `Tasks: Run Task` → `Setup Complete Project`
2. Start servers: `Start Backend Server` and `Start Frontend Server`

### Manual Setup
```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend (new terminal)
cd frontend
npm install
npm start
```

**URLs:** Frontend http://localhost:3000 | Backend http://localhost:5000

## 🎯 Usage

1. Enter vehicle details (length, height, width, weight, engine power, top speed, axles, seats, fuel type)
2. Click "Classify Vehicle" for instant prediction
3. View result and confidence score

**Supported Categories:**
- **Two-Wheelers:** 🛵 Scooter, 🏍️ Standard Motorcycle, 🏁 Sports Bike, 🏍️ Cruiser Bike
- **Cars:** 🚗 Hatchback, 🚙 Sedan, 🚘 Luxury Sedan, 🚐 Station Wagon  
- **SUVs:** 🚙 Compact SUV, 🚙 Mid-Size SUV, � Full-Size SUV
- **Trucks:** 🛻 Pickup Truck, � Light Commercial Truck, �🚛 Heavy Truck
- **Buses:** 🚐 Mini Bus, 🚌 City Bus, 🚌 Coach Bus

## 🔧 API Endpoints

- `GET /` - Health check
- `POST /predict` - Classify vehicle (returns prediction and confidence)
- `GET /model-info` - Model details

**Example:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"length": 4.88, "height": 1.45, "width": 1.84, "weight": 1590, "engine_power": 203, "top_speed": 210, "axle_count": 2, "seats": 5, "fuel_type": "petrol"}'
```

## 🧪 Test Cases

See [TEST_CASES.md](TEST_CASES.md) for real vehicle examples.

## 🛠️ Troubleshooting

**Common Issues:**
- **PowerShell Policy**: Use Command Prompt or `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **Python Dependencies**: Try `pip install -r requirements-legacy.txt`
- **Model Missing**: Run `python create_model.py` in model folder
- **Port Issues**: Backend uses 5000, Frontend uses 3000

## 🌐 Deployment

This project is ready for deployment on Render, Heroku, or similar platforms.

**Quick Deploy to Render:**
1. Push code to GitHub
2. Connect repository to Render
3. Deploy backend and frontend as separate services

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

MIT License - feel free to use this project for learning and development.

---

**⭐ Star this project if you find it helpful!**