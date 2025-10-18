"""
Vehicle Classification Model Generator

This script creates a dummy machine learning model for vehicle type classification.
The model will be saved as a .pkl file and can be loaded by the Flask backend.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def create_synthetic_data(n_samples=2000):
    """Create synthetic vehicle data for training"""
    np.random.seed(42)
    
    data = []
    labels = []
    
    # Define vehicle type parameters
    vehicle_types = {
        'Bike': {
            'length': (1.8, 2.5), 'height': (1.0, 1.3), 'width': (0.6, 0.9),
            'weight': (150, 400), 'power': (10, 200), 'speed': (60, 200),
            'axles': (2, 2), 'seats': (1, 2), 'fuel_probs': [0.1, 0.0, 0.7, 0.2]
        },
        'Car': {
            'length': (3.5, 5.5), 'height': (1.3, 1.8), 'width': (1.6, 2.1),
            'weight': (900, 2500), 'power': (80, 400), 'speed': (120, 250),
            'axles': (2, 2), 'seats': (2, 7), 'fuel_probs': [0.3, 0.1, 0.4, 0.2]
        },
        'SUV': {
            'length': (4.2, 6.0), 'height': (1.6, 2.2), 'width': (1.8, 2.3),
            'weight': (1500, 3500), 'power': (120, 500), 'speed': (140, 220),
            'axles': (2, 2), 'seats': (5, 8), 'fuel_probs': [0.4, 0.05, 0.3, 0.25]
        },
        'Bus': {
            'length': (8.0, 15.0), 'height': (2.5, 4.0), 'width': (2.3, 2.8),
            'weight': (8000, 25000), 'power': (200, 500), 'speed': (80, 120),
            'axles': (2, 4), 'seats': (20, 80), 'fuel_probs': [0.7, 0.15, 0.1, 0.05]
        },
        'Truck': {
            'length': (6.0, 20.0), 'height': (2.2, 4.2), 'width': (2.2, 2.8),
            'weight': (3500, 45000), 'power': (200, 600), 'speed': (80, 140),
            'axles': (2, 8), 'seats': (1, 3), 'fuel_probs': [0.8, 0.05, 0.1, 0.05]
        }
    }
    
    # Generate samples for each vehicle type
    samples_per_type = n_samples // len(vehicle_types)
    
    for vehicle_type, params in vehicle_types.items():
        for _ in range(samples_per_type):
            # Generate features
            length = np.random.uniform(*params['length'])
            height = np.random.uniform(*params['height'])
            width = np.random.uniform(*params['width'])
            weight = np.random.uniform(*params['weight'])
            power = np.random.uniform(*params['power'])
            speed = np.random.uniform(*params['speed'])
            axles = np.random.randint(*params['axles']) if params['axles'][0] == params['axles'][1] else np.random.randint(params['axles'][0], params['axles'][1] + 1)
            seats = np.random.randint(*params['seats']) if params['seats'][0] == params['seats'][1] else np.random.randint(params['seats'][0], params['seats'][1] + 1)
            
            # Generate fuel type based on probabilities
            fuel_choice = np.random.choice(4, p=params['fuel_probs'])
            fuel_onehot = [0, 0, 0, 0]
            fuel_onehot[fuel_choice] = 1
            
            # Combine features
            features = [length, height, width, weight, power, speed, axles, seats] + fuel_onehot
            
            data.append(features)
            labels.append(vehicle_type)
    
    return np.array(data), np.array(labels)

def train_model():
    """Train and save the vehicle classification model"""
    print("Generating synthetic vehicle data...")
    X, y = create_synthetic_data(2000)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    print(f"Features: {X_train.shape[1]}")
    print(f"Classes: {np.unique(y)}")
    
    # Train the model
    print("Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.3f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model
    os.makedirs('.', exist_ok=True)
    joblib.dump(model, 'vehicle_model.pkl')
    print(f"Model saved as 'vehicle_model.pkl'")
    
    return model

if __name__ == "__main__":
    model = train_model()
    
    # Test prediction
    print("\nTesting model with sample data...")
    
    # Test cases: [length, height, width, weight, power, speed, axles, seats, diesel, electric, hybrid, petrol]
    test_cases = [
        ([2.0, 1.1, 0.8, 200, 150, 180, 2, 1, 0, 0, 0, 1], "Bike"),
        ([4.5, 1.5, 1.9, 1500, 150, 180, 2, 5, 0, 0, 0, 1], "Car"),
        ([5.2, 1.9, 2.1, 2200, 250, 200, 2, 7, 1, 0, 0, 0], "SUV"),
        ([12.0, 3.2, 2.5, 15000, 350, 100, 3, 50, 1, 0, 0, 0], "Bus"),
        ([8.5, 3.0, 2.4, 12000, 400, 120, 4, 2, 1, 0, 0, 0], "Truck")
    ]
    
    for features, expected in test_cases:
        prediction = model.predict([features])[0]
        confidence = max(model.predict_proba([features])[0])
        print(f"Expected: {expected:5} | Predicted: {prediction:5} | Confidence: {confidence:.2f}")