import React, { useState } from 'react';
import axios from 'axios';
import toast from 'react-hot-toast';
import VehicleForm from './components/VehicleForm';
import ResultDisplay from './components/ResultDisplay';
import Header from './components/Header';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://vehicle-type-classification.onrender.com';

function App() {
  const [formData, setFormData] = useState({
    length: '',
    height: '',
    width: '',
    weight: '',
    engine_power: '',
    top_speed: '',
    axle_count: '',
    seats: '',
    fuel_type: 'petrol'
  });

  const [prediction, setPrediction] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (name, value) => {
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const validateForm = () => {
    const requiredFields = [
      'length', 'height', 'width', 'weight', 
      'engine_power', 'top_speed', 'axle_count', 'seats'
    ];

    for (let field of requiredFields) {
      if (!formData[field] || formData[field] <= 0) {
        toast.error(`Please enter a valid ${field.replace('_', ' ')}`);
        return false;
      }
    }

    // Additional validations
    if (parseFloat(formData.length) > 20) {
      toast.error('Vehicle length seems too large (max 20m)');
      return false;
    }

    if (parseFloat(formData.height) > 5) {
      toast.error('Vehicle height seems too large (max 5m)');
      return false;
    }

    if (parseFloat(formData.weight) > 100000) {
      toast.error('Vehicle weight seems too large (max 100,000kg)');
      return false;
    }

    if (parseInt(formData.seats) > 100) {
      toast.error('Number of seats seems too large (max 100)');
      return false;
    }

    return true;
  };

  const handleClassify = async () => {
    if (!validateForm()) return;

    setIsLoading(true);
    setPrediction(null);

    try {
      // Convert string values to numbers for API
      const apiData = {
        ...formData,
        length: parseFloat(formData.length),
        height: parseFloat(formData.height),
        width: parseFloat(formData.width),
        weight: parseFloat(formData.weight),
        engine_power: parseFloat(formData.engine_power),
        top_speed: parseFloat(formData.top_speed),
        axle_count: parseInt(formData.axle_count),
        seats: parseInt(formData.seats)
      };

      const response = await axios.post(`${API_BASE_URL}/predict`, apiData, {
        headers: {
          'Content-Type': 'application/json',
        },
        timeout: 15000, // 15 second timeout
        withCredentials: false // Disable credentials for CORS
      });

      setPrediction(response.data);
      toast.success('Vehicle classified successfully!');
    } catch (error) {
      console.error('Classification error:', error);
      
      if (error.response) {
        const message = error.response.data?.error || 'Classification failed';
        toast.error(message);
      } else if (error.request) {
        // Check if it's a CORS error
        if (error.message.includes('Network Error') || error.code === 'ERR_NETWORK') {
          toast.error('CORS Error: Unable to connect to backend. Please check if the API server is running and CORS is properly configured.');
        } else {
          toast.error('Unable to connect to the server. Please check if the backend is running.');
        }
      } else {
        toast.error('An unexpected error occurred');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setFormData({
      length: '',
      height: '',
      width: '',
      weight: '',
      engine_power: '',
      top_speed: '',
      axle_count: '',
      seats: '',
      fuel_type: 'petrol'
    });
    setPrediction(null);
    toast.success('Form reset successfully');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 via-purple-600 to-purple-800 py-8 px-4">
      <div className="container mx-auto max-w-4xl">
        <Header />
        
        <div className="bg-white rounded-2xl shadow-2xl overflow-hidden fade-in">
          <div className="p-8">
            <VehicleForm 
              formData={formData}
              onInputChange={handleInputChange}
              onClassify={handleClassify}
              onReset={handleReset}
              isLoading={isLoading}
            />
            
            {prediction && (
              <div className="mt-8">
                <ResultDisplay prediction={prediction} />
              </div>
            )}
          </div>
        </div>

        <div className="mt-8 text-center">
          <p className="text-white text-sm opacity-75">
            Powered by Machine Learning • Built with React & Flask
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;