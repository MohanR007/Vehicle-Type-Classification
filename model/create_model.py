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
    
    # Define detailed vehicle type parameters
    vehicle_types = {
        # Two-Wheeler Categories
        'Scooter': {
            'length': (1.6, 1.9), 'height': (1.1, 1.2), 'width': (0.65, 0.72),
            'weight': (100, 130), 'power': (6, 15), 'speed': (60, 90),
            'axles': (2, 2), 'seats': (2, 2), 'fuel_probs': [0.05, 0.0, 0.85, 0.1]
        },
        'Standard_Motorcycle': {
            'length': (2.0, 2.2), 'height': (1.0, 1.15), 'width': (0.75, 0.85),
            'weight': (140, 220), 'power': (15, 50), 'speed': (100, 140),
            'axles': (2, 2), 'seats': (2, 2), 'fuel_probs': [0.1, 0.0, 0.8, 0.1]
        },
        'Sports_Bike': {
            'length': (1.9, 2.1), 'height': (1.1, 1.2), 'width': (0.65, 0.75),
            'weight': (160, 220), 'power': (100, 220), 'speed': (250, 320),
            'axles': (2, 2), 'seats': (1, 2), 'fuel_probs': [0.05, 0.0, 0.9, 0.05]
        },
        'Cruiser_Bike': {
            'length': (2.2, 2.5), 'height': (1.0, 1.2), 'width': (0.85, 1.0),
            'weight': (250, 350), 'power': (60, 120), 'speed': (150, 190),
            'axles': (2, 2), 'seats': (2, 2), 'fuel_probs': [0.1, 0.0, 0.85, 0.05]
        },
        
        # Car Categories
        'Hatchback': {
            'length': (3.5, 4.2), 'height': (1.4, 1.6), 'width': (1.65, 1.8),
            'weight': (800, 1200), 'power': (70, 120), 'speed': (150, 190),
            'axles': (2, 2), 'seats': (4, 5), 'fuel_probs': [0.2, 0.15, 0.5, 0.15]
        },
        'Sedan': {
            'length': (4.3, 5.1), 'height': (1.35, 1.5), 'width': (1.75, 1.9),
            'weight': (1200, 1800), 'power': (120, 250), 'speed': (180, 230),
            'axles': (2, 2), 'seats': (4, 5), 'fuel_probs': [0.3, 0.1, 0.45, 0.15]
        },
        'Luxury_Sedan': {
            'length': (4.8, 5.5), 'height': (1.4, 1.55), 'width': (1.85, 2.0),
            'weight': (1600, 2200), 'power': (200, 400), 'speed': (220, 280),
            'axles': (2, 2), 'seats': (4, 5), 'fuel_probs': [0.4, 0.05, 0.35, 0.2]
        },
        'Wagon': {
            'length': (4.4, 5.0), 'height': (1.5, 1.7), 'width': (1.8, 1.95),
            'weight': (1300, 1900), 'power': (130, 220), 'speed': (170, 210),
            'axles': (2, 2), 'seats': (5, 7), 'fuel_probs': [0.35, 0.1, 0.4, 0.15]
        },
        
        # SUV Categories
        'Compact_SUV': {
            'length': (4.0, 4.5), 'height': (1.6, 1.75), 'width': (1.75, 1.9),
            'weight': (1300, 1700), 'power': (100, 160), 'speed': (160, 190),
            'axles': (2, 2), 'seats': (5, 5), 'fuel_probs': [0.3, 0.15, 0.4, 0.15]
        },
        'Mid_Size_SUV': {
            'length': (4.5, 5.2), 'height': (1.7, 1.9), 'width': (1.85, 2.0),
            'weight': (1800, 2500), 'power': (150, 300), 'speed': (170, 200),
            'axles': (2, 2), 'seats': (5, 7), 'fuel_probs': [0.4, 0.1, 0.35, 0.15]
        },
        'Full_Size_SUV': {
            'length': (5.0, 5.8), 'height': (1.8, 2.1), 'width': (1.95, 2.2),
            'weight': (2300, 3200), 'power': (250, 450), 'speed': (180, 220),
            'axles': (2, 2), 'seats': (6, 8), 'fuel_probs': [0.5, 0.05, 0.3, 0.15]
        },
        
        # Commercial Vehicles
        'Pickup_Truck': {
            'length': (5.0, 6.2), 'height': (1.8, 2.0), 'width': (1.9, 2.1),
            'weight': (1800, 2800), 'power': (200, 350), 'speed': (150, 180),
            'axles': (2, 2), 'seats': (2, 5), 'fuel_probs': [0.3, 0.05, 0.6, 0.05]
        },
        'Light_Truck': {
            'length': (5.5, 7.5), 'height': (2.2, 2.8), 'width': (1.9, 2.3),
            'weight': (3000, 8000), 'power': (150, 300), 'speed': (90, 130),
            'axles': (2, 3), 'seats': (2, 3), 'fuel_probs': [0.7, 0.1, 0.15, 0.05]
        },
        'Heavy_Truck': {
            'length': (7.0, 20.0), 'height': (3.0, 4.2), 'width': (2.3, 2.8),
            'weight': (8000, 45000), 'power': (300, 700), 'speed': (80, 120),
            'axles': (3, 8), 'seats': (1, 3), 'fuel_probs': [0.85, 0.05, 0.08, 0.02]
        },
        
        # Bus Categories
        'Mini_Bus': {
            'length': (6.0, 8.0), 'height': (2.3, 2.8), 'width': (2.0, 2.3),
            'weight': (3500, 6000), 'power': (120, 200), 'speed': (120, 140),
            'axles': (2, 2), 'seats': (12, 25), 'fuel_probs': [0.5, 0.2, 0.2, 0.1]
        },
        'City_Bus': {
            'length': (9.0, 12.0), 'height': (2.8, 3.2), 'width': (2.4, 2.6),
            'weight': (8000, 15000), 'power': (200, 350), 'speed': (80, 100),
            'axles': (2, 3), 'seats': (25, 50), 'fuel_probs': [0.7, 0.15, 0.1, 0.05]
        },
        'Coach_Bus': {
            'length': (11.0, 15.0), 'height': (3.2, 4.0), 'width': (2.5, 2.8),
            'weight': (15000, 25000), 'power': (350, 500), 'speed': (90, 120),
            'axles': (3, 4), 'seats': (40, 80), 'fuel_probs': [0.8, 0.1, 0.08, 0.02]
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
            # Generate axles
            if params['axles'][0] == params['axles'][1]:
                axles = params['axles'][0]
            else:
                axles = np.random.randint(params['axles'][0], params['axles'][1] + 1)
            
            # Generate seats
            if params['seats'][0] == params['seats'][1]:
                seats = params['seats'][0]
            else:
                seats = np.random.randint(params['seats'][0], params['seats'][1] + 1)
            
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