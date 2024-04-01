import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

// Import the main component of the application
import App from './App';

// Import the function for reporting web vitals
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  // Wrap the App component with React.StrictMode to enable additional checks and warnings for potential issues
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// Report web vitals to measure performance
reportWebVitals();
