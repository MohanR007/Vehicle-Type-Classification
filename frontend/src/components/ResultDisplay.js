import React from 'react';

const ResultDisplay = ({ prediction }) => {
  const getVehicleEmoji = (vehicleType) => {
    const vehicleEmojis = {
      'Bike': '🏍️',
      'Car': '🚗',
      'SUV': '🚙',
      'Bus': '🚌',
      'Truck': '🚛',
      'Motorcycle': '🏍️',
      'Van': '🚐'
    };
    return vehicleEmojis[vehicleType] || '🚗';
  };

  const getConfidenceColor = (confidence) => {
    if (confidence >= 0.8) return 'text-green-600 bg-green-100';
    if (confidence >= 0.6) return 'text-yellow-600 bg-yellow-100';
    return 'text-red-600 bg-red-100';
  };

  const getConfidenceLabel = (confidence) => {
    if (confidence >= 0.8) return 'High Confidence';
    if (confidence >= 0.6) return 'Medium Confidence';
    return 'Low Confidence';
  };

  return (
    <div className="bg-gradient-to-r from-green-50 to-blue-50 rounded-xl p-6 border-2 border-green-200 fade-in">
      <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
        🎯 Classification Result
      </h3>
      
      <div className="text-center mb-6">
        <div className="text-6xl mb-4 animate-bounce">
          {getVehicleEmoji(prediction.prediction)}
        </div>
        <div className="text-3xl font-bold text-gray-800 mb-2">
          {prediction.prediction}
        </div>
        <div className="text-lg text-gray-600">
          Predicted Vehicle Type
        </div>
      </div>

      {prediction.confidence && (
        <div className="bg-white rounded-lg p-4 mb-4">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm font-semibold text-gray-700">
              Model Confidence
            </span>
            <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getConfidenceColor(prediction.confidence)}`}>
              {getConfidenceLabel(prediction.confidence)}
            </span>
          </div>
          
          <div className="w-full bg-gray-200 rounded-full h-3 mb-2">
            <div 
              className="bg-gradient-to-r from-blue-500 to-green-500 h-3 rounded-full transition-all duration-1000 ease-out"
              style={{ width: `${(prediction.confidence * 100)}%` }}
            ></div>
          </div>
          
          <div className="text-center">
            <span className="text-lg font-bold text-gray-800">
              {(prediction.confidence * 100).toFixed(1)}%
            </span>
          </div>
        </div>
      )}

      <div className="bg-white rounded-lg p-4">
        <h4 className="font-semibold text-gray-700 mb-3 flex items-center">
          <span className="mr-2">📋</span>
          Input Summary
        </h4>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-3 text-sm">
          <div className="flex justify-between">
            <span className="text-gray-600">Length:</span>
            <span className="font-semibold">{prediction.input_data.length}m</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Height:</span>
            <span className="font-semibold">{prediction.input_data.height}m</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Width:</span>
            <span className="font-semibold">{prediction.input_data.width}m</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Weight:</span>
            <span className="font-semibold">{prediction.input_data.weight}kg</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Power:</span>
            <span className="font-semibold">{prediction.input_data.engine_power}HP</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">Seats:</span>
            <span className="font-semibold">{prediction.input_data.seats}</span>
          </div>
        </div>
      </div>

      <div className="mt-4 text-center text-xs text-gray-500">
        <span className="mr-2">🕒</span>
        Classified at: {new Date(prediction.timestamp).toLocaleString()}
      </div>
    </div>
  );
};

export default ResultDisplay;