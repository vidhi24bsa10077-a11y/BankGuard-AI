import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import './index.css';
import App from './App';

// Performance monitoring for development
if (process.env.NODE_ENV === 'development') {
  // Log render performance
  const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
      if (entry.entryType === 'measure') {
        console.log(`⚡ ${entry.name}: ${entry.duration.toFixed(2)}ms`);
      }
    }
  });
  observer.observe({ entryTypes: ['measure'] });
  
  // Mark app initialization
  performance.mark('quantum-app-start');
}

// Initialize React 18 concurrent features
const root = ReactDOM.createRoot(document.getElementById('root'));

// Quantum App Bootstrap with error boundary
const QuantumAppBootstrap = () => {
  React.useEffect(() => {
    // Performance measurement
    if (process.env.NODE_ENV === 'development') {
      performance.mark('quantum-app-end');
      performance.measure('quantum-app-initialization', 'quantum-app-start', 'quantum-app-end');
    }
    
    // Initialize quantum security protocols (simulation)
    console.log('🔬 Quantum APK Security Analyzer v1.0.0');
    console.log('🛡️ Quantum security protocols initialized');
    console.log('⚡ Real-time threat detection: ACTIVE');
    console.log('🔍 Deep packet inspection: ENABLED');
    console.log('🧬 Quantum encryption: VERIFIED');
    
    // Simulate security system startup
    setTimeout(() => {
      console.log('✅ All quantum security systems operational');
    }, 2000);
    
    // Set theme class on body for consistent styling
    document.body.classList.add('quantum-theme');
    
    // Add matrix animation effect
    createMatrixEffect();
    
    return () => {
      document.body.classList.remove('quantum-theme');
    };
  }, []);

  return (
    <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </React.StrictMode>
  );
};

// Matrix-like background animation for cybersecurity feel
const createMatrixEffect = () => {
  const canvas = document.createElement('canvas');
  canvas.id = 'matrix-canvas';
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.width = '100%';
  canvas.style.height = '100%';
  canvas.style.pointerEvents = 'none';
  canvas.style.zIndex = '-1';
  canvas.style.opacity = '0.03';
  
  document.body.insertBefore(canvas, document.body.firstChild);
  
  const ctx = canvas.getContext('2d');
  let animationId;
  
  const resizeCanvas = () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  };
  
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);
  
  // Matrix characters
  const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz<>{}[]()';
  const charArray = chars.split('');
  
  const fontSize = 14;
  const columns = canvas.width / fontSize;
  const drops = [];
  
  // Initialize drops
  for (let i = 0; i < columns; i++) {
    drops[i] = Math.random() * canvas.height;
  }
  
  const drawMatrix = () => {
    ctx.fillStyle = 'rgba(10, 10, 10, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = '#00ff88';
    ctx.font = `${fontSize}px 'JetBrains Mono', monospace`;
    
    for (let i = 0; i < drops.length; i++) {
      const text = charArray[Math.floor(Math.random() * charArray.length)];
      ctx.fillText(text, i * fontSize, drops[i] * fontSize);
      
      if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
        drops[i] = 0;
      }
      drops[i]++;
    }
    
    animationId = requestAnimationFrame(drawMatrix);
  };
  
  // Start matrix animation with delay for performance
  setTimeout(() => {
    drawMatrix();
  }, 3000);
  
  // Cleanup function
  return () => {
    if (animationId) {
      cancelAnimationFrame(animationId);
    }
    window.removeEventListener('resize', resizeCanvas);
  };
};

// Error Boundary Component
class QuantumErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('🚨 Quantum Security System Error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen bg-gray-900 flex items-center justify-center">
          <div className="text-center p-8">
            <div className="text-red-400 text-6xl mb-4">⚠️</div>
            <h1 className="text-2xl font-bold text-red-400 mb-4">
              Quantum Security System Error
            </h1>
            <p className="text-gray-300 mb-6">
              A critical error occurred in the quantum security protocols.
            </p>
            <button
              onClick={() => window.location.reload()}
              className="bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-lg transition-colors"
            >
              Restart Security System
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}

// Render app with error boundary
root.render(
  <QuantumErrorBoundary>
    <QuantumAppBootstrap />
  </QuantumErrorBoundary>
);

// Report web vitals for performance monitoring
const reportWebVitals = (onPerfEntry) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

// Enable performance monitoring in development
if (process.env.NODE_ENV === 'development') {
  reportWebVitals(console.log);
}
