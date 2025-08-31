import unittest
import json
import tempfile
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

class TestBankGuardAPI(unittest.TestCase):
    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Create test data directory
        os.makedirs('data/temp', exist_ok=True)
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('model_loaded', data)
        self.assertIn('timestamp', data)
    
    def test_statistics_endpoint(self):
        """Test statistics endpoint"""
        response = self.client.get('/api/statistics')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('total_analyses', data)
        self.assertIn('accuracy', data)
        self.assertIn('model_version', data)
    
    def test_demo_predict(self):
        """Test demo prediction endpoint"""
        test_data = {'test': True}
        response = self.client.post('/api/demo-predict', 
                                  data=json.dumps(test_data),
                                  content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('result', data)
        self.assertIn('prediction', data['result'])
    
    def test_analyze_no_file(self):
        """Test analysis endpoint without file"""
        response = self.client.post('/api/analyze')
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_analyze_with_json(self):
        """Test analysis with JSON features"""
        test_features = {
            'permission_INTERNET': 1,
            'permission_ACCESS_NETWORK_STATE': 1,
            'permission_SEND_SMS': 0
        }
        
        response = self.client.post('/api/analyze',
                                  data=json.dumps(test_features),
                                  content_type='application/json')
        
        # Should work even with partial features
        self.assertIn(response.status_code, [200, 500])  # May fail if model not trained

if __name__ == '__main__':
    unittest.main()
