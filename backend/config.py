# 📄 backend/config.py - Configuration Settings
# ================================================================================

import os
from datetime import timedelta

class Config:
    """Application configuration"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bankguard-ai-secret-key-2025'
    DEBUG = True
    
    # File upload settings
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
    UPLOAD_FOLDER = 'data/temp/'
    ALLOWED_EXTENSIONS = {'apk'}
    
    # Model settings
    MODEL_PATH = 'data/trained_models/bankguard_model.joblib'
    DATASET_PATH = 'data/datasets/fullset_train.csv'
    VALIDATION_DATASET_PATH = 'data/datasets/data_set2.csv'
    
    # Database settings
    DATABASE_PATH = 'data/analysis_results.json'
    
    # API settings
    API_RATE_LIMIT = '100 per minute'
    API_TIMEOUT = 30  # seconds
    
    # Security settings
    CORS_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']
    
    # Logging settings
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'logs/bankguard.log'
    
    # Model performance thresholds
    MIN_ACCURACY_THRESHOLD = 0.90
    MAX_FALSE_POSITIVE_RATE = 0.05
    
    # Demo settings
    DEMO_MODE = True
    SIMULATION_DELAY = 2.0  # seconds
    
    @staticmethod
    def init_app(app):
        """Initialize app with configuration"""
        # Create necessary directories
        os.makedirs('data/temp', exist_ok=True)
        os.makedirs('data/trained_models', exist_ok=True)
        os.makedirs('data/datasets', exist_ok=True)
        os.makedirs('logs', exist_ok=True)
