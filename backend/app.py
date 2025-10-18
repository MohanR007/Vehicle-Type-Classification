from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
# Configure CORS for production
CORS(app, origins=[
    "http://localhost:3000",
    "https://*.onrender.com",
    "https://vtc-frontend.onrender.com"
])

# Global variable to store the model
model = None
feature_columns = [
    'length', 'height', 'width', 'weight', 
    'engine_power', 'top_speed', 'axle_count', 
    'seats', 'fuel_type_diesel', 'fuel_type_electric', 
    'fuel_type_hybrid', 'fuel_type_petrol'
]

def load_model():
    """Load the pretrained model"""
    global model
    try:
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, '..', 'model', 'vehicle_model.pkl')
        model_path = os.path.normpath(model_path)  # Normalize the path
        
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            print(f"NEW DETAILED Model loaded successfully from {model_path}")
            if hasattr(model, 'classes_'):
                print(f"Model classes: {list(model.classes_)}")
        else:
            print(f"Model file not found at {model_path}")
            # Create a dummy model for demonstration
            create_dummy_model()
    except Exception as e:
        print(f"Error loading model: {e}")
        create_dummy_model()

def create_dummy_model():
    """Create a dummy model for demonstration purposes"""
    global model
    from sklearn.ensemble import RandomForestClassifier
    
    # Create dummy training data
    np.random.seed(42)
    n_samples = 1000
    
    # Generate synthetic features
    X = np.random.rand(n_samples, 12)
    
    # Create realistic vehicle data ranges
    X[:, 0] = np.random.uniform(2, 15, n_samples)  # length (2-15m)
    X[:, 1] = np.random.uniform(1.2, 4, n_samples)  # height (1.2-4m)
    X[:, 2] = np.random.uniform(1.5, 3, n_samples)  # width (1.5-3m)
    X[:, 3] = np.random.uniform(500, 40000, n_samples)  # weight (500-40000kg)
    X[:, 4] = np.random.uniform(50, 500, n_samples)  # engine_power (50-500hp)
    X[:, 5] = np.random.uniform(60, 300, n_samples)  # top_speed (60-300km/h)
    X[:, 6] = np.random.randint(2, 8, n_samples)  # axle_count (2-7)
    X[:, 7] = np.random.randint(1, 60, n_samples)  # seats (1-60)
    
    # One-hot encoded fuel type (last 4 columns)
    fuel_types = np.zeros((n_samples, 4))
    fuel_choice = np.random.randint(0, 4, n_samples)
    fuel_types[np.arange(n_samples), fuel_choice] = 1
    X[:, 8:12] = fuel_types
    
    # Generate labels based on realistic rules
    y = []
    for i in range(n_samples):
        length, height, weight, seats = X[i, 0], X[i, 1], X[i, 3], X[i, 7]
        
        if length < 3 and seats <= 2:
            y.append('Bike')
        elif length < 5.5 and weight < 2500 and seats <= 7:
            y.append('Car')
        elif 5 <= length <= 6 and weight < 3000 and seats <= 7:
            y.append('SUV')
        elif length > 8 and seats > 20:
            y.append('Bus')
        elif weight > 7500:
            y.append('Truck')
        else:
            y.append('Car')  # default
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save the model
    os.makedirs('../model', exist_ok=True)
    joblib.dump(model, '../model/vehicle_model.pkl')
    print("Dummy model created and saved successfully")

def preprocess_input(data):
    """Preprocess input data for prediction"""
    # Create feature vector
    features = [
        float(data['length']),
        float(data['height']),
        float(data['width']),
        float(data['weight']),
        float(data['engine_power']),
        float(data['top_speed']),
        int(data['axle_count']),
        int(data['seats']),
    ]
    
    # One-hot encode fuel type
    fuel_type = data['fuel_type'].lower()
    fuel_encoding = [0, 0, 0, 0]  # diesel, electric, hybrid, petrol
    
    if fuel_type == 'diesel':
        fuel_encoding[0] = 1
    elif fuel_type == 'electric':
        fuel_encoding[1] = 1
    elif fuel_type == 'hybrid':
        fuel_encoding[2] = 1
    elif fuel_type == 'petrol':
        fuel_encoding[3] = 1
    
    features.extend(fuel_encoding)
    
    return np.array(features).reshape(1, -1)

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        'message': 'Vehicle Type Classification API',
        'status': 'active',
        'model_loaded': model is not None,
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Detailed health check for monitoring"""
    return jsonify({
        'status': 'healthy' if model is not None else 'unhealthy',
        'model_loaded': model is not None,
        'api_version': '1.0.0',
        'python_version': '3.11.0',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Predict vehicle type based on input features"""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        data = request.get_json()
        
        # Validate required fields
        required_fields = [
            'length', 'height', 'width', 'weight', 
            'engine_power', 'top_speed', 'axle_count', 
            'seats', 'fuel_type'
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
        
        # Preprocess input
        features = preprocess_input(data)
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Get prediction probabilities if available
        confidence = None
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(features)[0]
            confidence = float(max(probabilities))
        
        return jsonify({
            'prediction': prediction,
            'confidence': confidence,
            'input_data': data,
            'timestamp': datetime.now().isoformat()
        })
    
    except ValueError as e:
        return jsonify({'error': f'Invalid input data: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app.route('/model-info', methods=['GET'])
def model_info():
    """Get information about the loaded model"""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    info = {
        'model_type': str(type(model).__name__),
        'feature_count': len(feature_columns),
        'features': feature_columns
    }
    
    if hasattr(model, 'classes_'):
        info['classes'] = list(model.classes_)
    
    return jsonify(info)

if __name__ == '__main__':
    print("Starting Flask app with detailed model...")
    load_model()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

# Load model on startup (for production)
load_model()