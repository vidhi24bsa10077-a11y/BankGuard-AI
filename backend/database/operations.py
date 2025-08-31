# 📄 backend/database/operations.py - Database Manager
# ================================================================================

import json
import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self, db_path='data/analysis_results.json'):
        """Initialize database manager (simple JSON file for demo)"""
        self.db_path = db_path
        self.ensure_db_exists()
    
    def ensure_db_exists(self):
        """Ensure database file exists"""
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            if not os.path.exists(self.db_path):
                with open(self.db_path, 'w') as f:
                    json.dump({'analyses': [], 'metadata': {'created': datetime.now().isoformat()}}, f)
                logger.info(f"📁 Database initialized: {self.db_path}")
        except Exception as e:
            logger.error(f"Database initialization failed: {str(e)}")
    
    def save_analysis(self, analysis_data):
        """Save analysis result to database"""
        try:
            # Load existing data
            with open(self.db_path, 'r') as f:
                db_data = json.load(f)
            
            # Add new analysis
            analysis_id = str(int(datetime.now().timestamp()))
            analysis_data['analysis_id'] = analysis_id
            analysis_data['saved_at'] = datetime.now().isoformat()
            
            db_data['analyses'].append(analysis_data)
            
            # Save back to file
            with open(self.db_path, 'w') as f:
                json.dump(db_data, f, indent=2)
            
            logger.info(f"💾 Analysis saved: {analysis_id}")
            return analysis_id
            
        except Exception as e:
            logger.error(f"Failed to save analysis: {str(e)}")
            return None
    
    def get_analysis(self, analysis_id):
        """Retrieve analysis by ID"""
        try:
            with open(self.db_path, 'r') as f:
                db_data = json.load(f)
            
            for analysis in db_data['analyses']:
                if analysis.get('analysis_id') == analysis_id:
                    return analysis
            
            return None
            
        except Exception as e:
            logger.error(f"Failed to retrieve analysis {analysis_id}: {str(e)}")
            return None
    
    def get_all_analyses(self, limit=100):
        """Get all analyses (limited)"""
        try:
            with open(self.db_path, 'r') as f:
                db_data = json.load(f)
            
            return db_data['analyses'][-limit:]  # Return latest analyses
            
        except Exception as e:
            logger.error(f"Failed to retrieve analyses: {str(e)}")
            return []
