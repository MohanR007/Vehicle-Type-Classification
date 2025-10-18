import React from 'react';

const Header = () => {
  return (
    <div className="text-center mb-8 fade-in">
      <h1 className="text-5xl font-bold text-white mb-4">
        🚗 Vehicle Type Classification
      </h1>
      <p className="text-xl text-white opacity-90 mb-2">
        Predict vehicle types using machine learning
      </p>
      <p className="text-lg text-white opacity-75">
        Enter vehicle specifications to get an AI-powered classification
      </p>
      <div className="mt-6 flex justify-center space-x-4 text-3xl">
        <span className="animate-bounce">🏍️</span>
        <span className="animate-bounce" style={{ animationDelay: '0.1s' }}>🚙</span>
        <span className="animate-bounce" style={{ animationDelay: '0.2s' }}>🚌</span>
        <span className="animate-bounce" style={{ animationDelay: '0.3s' }}>🚛</span>
      </div>
    </div>
  );
};

export default Header;