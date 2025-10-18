import React from 'react';

const VehicleForm = ({ formData, onInputChange, onClassify, onReset, isLoading }) => {
  const inputFields = [
    {
      name: 'length',
      label: 'Vehicle Length (m)',
      type: 'number',
      placeholder: 'e.g., 4.5',
      step: '0.1',
      min: '0.1',
      icon: '📏'
    },
    {
      name: 'height',
      label: 'Vehicle Height (m)',
      type: 'number',
      placeholder: 'e.g., 1.8',
      step: '0.1',
      min: '0.1',
      icon: '📐'
    },
    {
      name: 'width',
      label: 'Vehicle Width (m)',
      type: 'number',
      placeholder: 'e.g., 2.0',
      step: '0.1',
      min: '0.1',
      icon: '↔️'
    },
    {
      name: 'weight',
      label: 'Vehicle Weight (kg)',
      type: 'number',
      placeholder: 'e.g., 1500',
      step: '1',
      min: '1',
      icon: '⚖️'
    },
    {
      name: 'engine_power',
      label: 'Engine Power (HP)',
      type: 'number',
      placeholder: 'e.g., 150',
      step: '1',
      min: '1',
      icon: '⚡'
    },
    {
      name: 'top_speed',
      label: 'Top Speed (km/h)',
      type: 'number',
      placeholder: 'e.g., 180',
      step: '1',
      min: '1',
      icon: '🏁'
    },
    {
      name: 'axle_count',
      label: 'Axle Count',
      type: 'number',
      placeholder: 'e.g., 2',
      step: '1',
      min: '1',
      max: '10',
      icon: '🔧'
    },
    {
      name: 'seats',
      label: 'Number of Seats',
      type: 'number',
      placeholder: 'e.g., 5',
      step: '1',
      min: '1',
      max: '100',
      icon: '💺'
    }
  ];

  const fuelOptions = [
    { value: 'petrol', label: 'Petrol', icon: '⛽' },
    { value: 'diesel', label: 'Diesel', icon: '🛢️' },
    { value: 'electric', label: 'Electric', icon: '🔋' },
    { value: 'hybrid', label: 'Hybrid', icon: '🔄' }
  ];

  return (
    <div>
      <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
        Vehicle Specifications
      </h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {inputFields.map((field) => (
          <div key={field.name} className="relative">
            <label className="block text-sm font-semibold text-gray-700 mb-2">
              <span className="mr-2">{field.icon}</span>
              {field.label}
            </label>
            <input
              type={field.type}
              value={formData[field.name]}
              onChange={(e) => onInputChange(field.name, e.target.value)}
              placeholder={field.placeholder}
              step={field.step}
              min={field.min}
              max={field.max}
              className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none"
              disabled={isLoading}
            />
          </div>
        ))}

        <div className="relative">
          <label className="block text-sm font-semibold text-gray-700 mb-2">
            <span className="mr-2">⛽</span>
            Fuel Type
          </label>
          <select
            value={formData.fuel_type}
            onChange={(e) => onInputChange('fuel_type', e.target.value)}
            className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all duration-200 outline-none appearance-none bg-white"
            disabled={isLoading}
          >
            {fuelOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.icon} {option.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="flex flex-col sm:flex-row gap-4 mt-8 justify-center">
        <button
          onClick={onClassify}
          disabled={isLoading}
          className={`px-8 py-4 rounded-lg font-semibold text-white transition-all duration-300 transform hover:scale-105 ${
            isLoading
              ? 'bg-gray-400 cursor-not-allowed'
              : 'bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 shadow-lg hover:shadow-xl'
          }`}
        >
          {isLoading ? (
            <div className="flex items-center justify-center">
              <div className="spinner mr-3"></div>
              Classifying...
            </div>
          ) : (
            <div className="flex items-center justify-center">
              <span className="mr-2">🔍</span>
              Classify Vehicle
            </div>
          )}
        </button>

        <button
          onClick={onReset}
          disabled={isLoading}
          className="px-8 py-4 rounded-lg font-semibold text-gray-700 bg-gray-200 hover:bg-gray-300 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
        >
          <span className="mr-2">🔄</span>
          Reset Form
        </button>
      </div>
    </div>
  );
};

export default VehicleForm;