# 🧪 Vehicle Classification Test Cases

Real-world vehicle specifications for testing the AI classification system. All data based on manufacturer specifications.

## 🏍️ Motorcycles & Bikes

| Vehicle | Length (m) | Height (m) | Width (m) | Weight (kg) | Power (HP) | Speed (km/h) | Axles | Seats | Fuel | Expected | Confidence |
|---------|------------|------------|-----------|-------------|------------|--------------|-------|-------|------|----------|------------|
| Yamaha YZF-R1 (2023) | 2.06 | 1.16 | 0.69 | 201 | 200 | 299 | 2 | 2 | petrol | Sports_Bike | ~98% |
| Honda Activa 6G | 1.83 | 1.16 | 0.68 | 118 | 8 | 83 | 2 | 2 | petrol | Scooter | ~99% |
| Harley-Davidson Fat Boy | 2.32 | 1.11 | 0.94 | 317 | 93 | 177 | 2 | 2 | petrol | Cruiser_Bike | ~97% |
| Royal Enfield Classic 350 | 2.16 | 1.09 | 0.80 | 195 | 20 | 114 | 2 | 2 | petrol | Standard_Motorcycle | ~96% |

## 🚗 Cars

| Vehicle | Length (m) | Height (m) | Width (m) | Weight (kg) | Power (HP) | Speed (km/h) | Axles | Seats | Fuel | Expected | Confidence |
|---------|------------|------------|-----------|-------------|------------|--------------|-------|-------|------|----------|------------|
| Toyota Camry (2023) | 4.88 | 1.45 | 1.84 | 1590 | 203 | 210 | 2 | 5 | petrol | Sedan | ~96% |
| BMW 3 Series 320i | 4.71 | 1.44 | 1.83 | 1540 | 184 | 230 | 2 | 5 | petrol | Luxury_Sedan | ~94% |
| Tesla Model 3 | 4.69 | 1.44 | 1.85 | 1611 | 283 | 225 | 2 | 5 | electric | Sedan | ~95% |
| Maruti Suzuki Swift | 3.85 | 1.53 | 1.74 | 865 | 90 | 165 | 2 | 5 | petrol | Hatchback | ~98% |
| Honda Civic (2023) | 4.67 | 1.42 | 1.80 | 1350 | 158 | 200 | 2 | 5 | petrol | Sedan | ~97% |
| Volkswagen Polo | 4.05 | 1.45 | 1.75 | 1155 | 110 | 190 | 2 | 5 | petrol | Hatchback | ~96% |

## 🚙 SUVs

| Vehicle | Length (m) | Height (m) | Width (m) | Weight (kg) | Power (HP) | Speed (km/h) | Axles | Seats | Fuel | Expected | Confidence |
|---------|------------|------------|-----------|-------------|------------|--------------|-------|-------|------|----------|------------|
| Toyota Fortuner (2023) | 4.80 | 1.84 | 1.86 | 2140 | 204 | 180 | 2 | 7 | diesel | Mid_Size_SUV | ~97% |
| Mahindra Thar (2023) | 3.99 | 1.85 | 1.82 | 1847 | 150 | 155 | 2 | 4 | diesel | Compact_SUV | ~92% |
| Range Rover Evoque | 4.37 | 1.65 | 1.90 | 1795 | 249 | 217 | 2 | 5 | petrol | Compact_SUV | ~89% |
| Hyundai Creta (2023) | 4.30 | 1.63 | 1.79 | 1540 | 115 | 170 | 2 | 5 | petrol | Compact_SUV | ~88% |
| Ford EcoSport (2023) | 4.00 | 1.69 | 1.77 | 1345 | 125 | 182 | 2 | 5 | petrol | Compact_SUV | ~85% |

## 🚌 Buses

| Vehicle | Length (m) | Height (m) | Width (m) | Weight (kg) | Power (HP) | Speed (km/h) | Axles | Seats | Fuel | Expected | Confidence |
|---------|------------|------------|-----------|-------------|------------|--------------|-------|-------|------|----------|------------|
| Volvo 9700 Coach | 12.0 | 3.70 | 2.55 | 18000 | 420 | 100 | 3 | 49 | diesel | Coach_Bus | ~99% |
| Tata Starbus City | 9.0 | 2.95 | 2.50 | 9500 | 180 | 80 | 2 | 33 | diesel | City_Bus | ~98% |
| Mercedes Sprinter | 7.36 | 2.75 | 2.02 | 4600 | 163 | 140 | 2 | 19 | diesel | Mini_Bus | ~85% |
| Ashok Leyland Viking | 7.4 | 2.80 | 2.10 | 5800 | 125 | 90 | 2 | 25 | diesel | Mini_Bus | ~93% |

## 🚛 Trucks

| Vehicle | Length (m) | Height (m) | Width (m) | Weight (kg) | Power (HP) | Speed (km/h) | Axles | Seats | Fuel | Expected | Confidence |
|---------|------------|------------|-----------|-------------|------------|--------------|-------|-------|------|----------|------------|
| Tata LPT 407 | 5.64 | 2.50 | 1.95 | 4200 | 85 | 95 | 2 | 3 | diesel | Light_Truck | ~94% |
| Ford F-150 (2023) | 5.92 | 1.96 | 2.03 | 2267 | 290 | 160 | 2 | 5 | petrol | Pickup_Truck | ~87% |
| Volvo FH16 Heavy | 6.24 | 4.00 | 2.55 | 8500 | 750 | 90 | 3 | 2 | diesel | Heavy_Truck | ~99% |
| Mahindra Bolero Pickup | 4.25 | 1.88 | 1.75 | 1880 | 75 | 125 | 2 | 2 | diesel | Pickup_Truck | ~91% |
| Isuzu D-Max V-Cross | 5.30 | 1.79 | 1.86 | 1950 | 134 | 175 | 2 | 5 | diesel | Pickup_Truck | ~89% |

## 🧪 API Testing Examples

### Using cURL (Command Line)
```bash
# Test Honda Activa (Scooter)
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "length": 1.83, "height": 1.16, "width": 0.68,
    "weight": 118, "engine_power": 8, "top_speed": 83,
    "axle_count": 2, "seats": 2, "fuel_type": "petrol"
  }'

# Test BMW 3 Series
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "length": 4.71, "height": 1.44, "width": 1.83,
    "weight": 1540, "engine_power": 184, "top_speed": 230,
    "axle_count": 2, "seats": 5, "fuel_type": "petrol"
  }'

# Test Toyota Fortuner SUV
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "length": 4.80, "height": 1.84, "width": 1.86,
    "weight": 2140, "engine_power": 204, "top_speed": 180,
    "axle_count": 2, "seats": 7, "fuel_type": "diesel"
  }'
```

### Python Testing Script
```python
import requests

# Quick test examples
vehicles = [
    ("Honda Activa", {"length": 1.83, "height": 1.16, "width": 0.68, "weight": 118, "engine_power": 8, "top_speed": 83, "axle_count": 2, "seats": 2, "fuel_type": "petrol"}),
    ("Toyota Camry", {"length": 4.88, "height": 1.45, "width": 1.84, "weight": 1590, "engine_power": 203, "top_speed": 210, "axle_count": 2, "seats": 5, "fuel_type": "petrol"}),
    ("Yamaha YZF-R1", {"length": 2.06, "height": 1.16, "width": 0.69, "weight": 201, "engine_power": 200, "top_speed": 299, "axle_count": 2, "seats": 2, "fuel_type": "petrol"})
]

for name, data in vehicles:
    r = requests.post("http://localhost:5000/predict", json=data)
    result = r.json()
    print(f"{name}: {result['prediction']} ({result['confidence']:.1%})")
```

### Using JavaScript (Frontend)
```javascript
// Test Mahindra Thar SUV
const tharData = {
  length: 3.99, height: 1.85, width: 1.82,
  weight: 1847, engine_power: 150, top_speed: 155,
  axle_count: 2, seats: 4, fuel_type: "diesel"
};

fetch('http://localhost:5000/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(tharData)
})
.then(response => response.json())
.then(data => {
  console.log(`Prediction: ${data.prediction}`);
  console.log(`Confidence: ${(data.confidence * 100).toFixed(1)}%`);
});

// Batch test multiple vehicles
const vehicles = [
  { name: "Honda Activa", data: {length: 1.83, height: 1.16, width: 0.68, weight: 118, engine_power: 8, top_speed: 83, axle_count: 2, seats: 2, fuel_type: "petrol"} },
  { name: "Toyota Camry", data: {length: 4.88, height: 1.45, width: 1.84, weight: 1590, engine_power: 203, top_speed: 210, axle_count: 2, seats: 5, fuel_type: "petrol"} },
  { name: "Volvo Bus", data: {length: 12.0, height: 3.7, width: 2.55, weight: 18000, engine_power: 420, top_speed: 100, axle_count: 3, seats: 49, fuel_type: "diesel"} }
];

vehicles.forEach(async (vehicle) => {
  try {
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(vehicle.data)
    });
    
    const result = await response.json();
    console.log(`${vehicle.name}: ${result.prediction} (${(result.confidence * 100).toFixed(1)}%)`);
  } catch (error) {
    console.error(`Error testing ${vehicle.name}:`, error);
  }
});
```

## 📊 Expected Results Summary

| Vehicle Category | Model | Expected Classification | Confidence Range |
|-----------------|--------|----------------------|------------------|
| 🏍️ **Two-Wheelers** | Yamaha YZF-R1 | Sports_Bike | 98% |
| 🏍️ **Two-Wheelers** | Honda Activa | Scooter | 99% |
| 🏍️ **Two-Wheelers** | Harley Fat Boy | Cruiser_Bike | 97% |
| 🏍️ **Two-Wheelers** | Royal Enfield Classic | Standard_Motorcycle | 96% |
| 🚗 **Cars** | Toyota Camry | Sedan | 96% |
| 🚗 **Cars** | BMW 3 Series | Luxury_Sedan | 94% |
| 🚗 **Cars** | Tesla Model 3 | Sedan | 95% |
| 🚗 **Cars** | Maruti Swift | Hatchback | 98% |
| 🚗 **Cars** | Honda Civic | Sedan | 97% |
| 🚗 **Cars** | Volkswagen Polo | Hatchback | 96% |
| 🚙 **SUVs** | Toyota Fortuner | Mid_Size_SUV | 97% |
| 🚙 **SUVs** | Mahindra Thar | Compact_SUV | 92% |
| 🚙 **SUVs** | Range Rover Evoque | Compact_SUV | 89% |
| 🚙 **SUVs** | Hyundai Creta | Compact_SUV | 88% |
| � **SUVs** | Ford EcoSport | Compact_SUV | 85% |
| �🚌 **Buses** | Volvo 9700 | Coach_Bus | 99% |
| 🚌 **Buses** | Tata Starbus | City_Bus | 98% |
| 🚌 **Buses** | Mercedes Sprinter | Mini_Bus | 85% |
| 🚌 **Buses** | Ashok Leyland Viking | Mini_Bus | 93% |
| 🚛 **Trucks** | Volvo FH16 | Heavy_Truck | 99% |
| 🚛 **Trucks** | Tata LPT 407 | Light_Truck | 94% |
| 🚛 **Trucks** | Ford F-150 | Pickup_Truck | 87% |
| 🚛 **Trucks** | Mahindra Bolero | Pickup_Truck | 91% |
| 🚛 **Trucks** | Isuzu D-Max V-Cross | Pickup_Truck | 89% |

## 🎯 Testing Tips

### Getting Accurate Specifications
1. **Manufacturer Website**: Official spec sheets
2. **Vehicle Manual**: Owner's manual specifications  
3. **Registration Documents**: Government vehicle registration
4. **Auto Websites**: CarDekho, AutoTrader, manufacturer sites
5. **Wikipedia**: Often has detailed specs for popular models

### Confidence Levels
- **95%+**: Very confident
- **85-94%**: Good confidence
- **70-84%**: Moderate confidence
- **<70%**: Low confidence

---

**Related Files**: [README.md](README.md) | [QUICKSTART.md](QUICKSTART.md) | [SKLEARN_SETUP.md](SKLEARN_SETUP.md)