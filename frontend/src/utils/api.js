/ 📄 frontend/src/utils/api.js - API Helper Functions
// ================================================================================

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

class APIClient {
  constructor() {
    this.baseURL = API_BASE_URL;
    this.timeout = 30000; // 30 seconds
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    
    const config = {
      timeout: this.timeout,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      },
      ...options
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error(`API request failed: ${error.message}`);
      throw error;
    }
  }

  // Health check
  async healthCheck() {
    return this.request('/api/health');
  }

  // APK Analysis
  async analyzeAPK(file) {
    const formData = new FormData();
    formData.append('apk_file', file);

    return this.request('/api/analyze', {
      method: 'POST',
      headers: {}, // Let browser set Content-Type for FormData
      body: formData
    });
  }

  // Demo prediction (with simulated data)
  async demoPredict(data = {}) {
    return this.request('/api/demo-predict', {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }

  // Batch analysis
  async batchAnalyze(files) {
    const formData = new FormData();
    files.forEach(file => {
      formData.append('apk_files', file);
    });

    return this.request('/api/batch-analyze', {
      method: 'POST',
      headers: {},
      body: formData
    });
  }

  // Get statistics
  async getStatistics() {
    return this.request('/api/statistics');
  }

  // Get analysis report
  async getReport(analysisId) {
    return this.request(`/api/reports/${analysisId}`);
  }

  // Train model (admin function)
  async trainModel() {
    return this.request('/api/train-model', {
      method: 'POST'
    });
  }
}

export const apiClient = new APIClient();

// Utility functions for API responses
export const handleAPIError = (error) => {
  console.error('API Error:', error);
  
  if (error.message.includes('fetch')) {
    return 'Network error. Please check your connection and try again.';
  }
  
  if (error.message.includes('timeout')) {
    return 'Request timeout. The analysis is taking longer than expected.';
  }
  
  return error.message || 'An unexpected error occurred.';
};

export const validateAPKFile = (file) => {
  const errors = [];
  
  if (!file) {
    errors.push('No file selected');
    return errors;
  }
  
  // Check file extension
  if (!file.name.toLowerCase().endsWith('.apk')) {
    errors.push('File must be an APK file (.apk extension)');
  }
  
  // Check file size (50MB limit)
  const maxSize = 50 * 1024 * 1024;
  if (file.size > maxSize) {
    errors.push(`File size must be less than 50MB (current: ${formatFileSize(file.size)})`);
  }
  
  // Check minimum size
  const minSize = 1024; // 1KB
  if (file.size < minSize) {
    errors.push('File appears to be too small to be a valid APK');
  }
  
  return errors;
};
