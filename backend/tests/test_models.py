# 📄 backend/tests/test_models.py - Model Testing
# ================================================================================

import unittest
import numpy as np
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.banking_classifier import BankingAPKClassifier

class TestBankingClassifier(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.classifier = BankingAPKClassifier()
        
        # Create sample test data
        self.sample_features = np.array([[1, 0, 1, 0, 1] + [0] * 578])  # 583 features total
        self.sample_labels = np.array([1])  # Malicious
    
    def test_model_initialization(self):
        """Test model initialization"""
        self.assertIsNotNone(self.classifier.model)
        self.assertIsNotNone(self.classifier.scaler)
        self.assertFalse(self.classifier.is_trained)
    
    def test_feature_vector_conversion(self):
        """Test feature dictionary to vector conversion"""
        feature_dict = {
            'permission_INTERNET': 1,
            'permission_SEND_SMS': 0,
            'permission_CAMERA': 1
        }
        
        # This will only work after training when feature_names is set
        if self.classifier.feature_names:
            vector = self.classifier._dict_to_vector(feature_dict)
            self.assertEqual(vector.shape[1], len(self.classifier.feature_names))
    
    def test_prediction_format(self):
        """Test prediction result format"""
        if not self.classifier.is_trained:
            # Skip if model not trained
            self.skipTest("Model not trained")
        
        result = self.classifier.predict_with_explanation(self.sample_features[0])
        
        # Check required fields
        required_fields = ['prediction', 'risk_score', 'confidence', 'explanation']
        for field in required_fields:
            self.assertIn(field, result)
        
        # Check value ranges
        self.assertIn(result['prediction'], ['LEGITIMATE', 'MALICIOUS'])
        self.assertGreaterEqual(result['risk_score'], 0)
        self.assertLessEqual(result['risk_score'], 10)
        self.assertGreaterEqual(result['confidence'], 0)
        self.assertLessEqual(result['confidence'], 100)

if __name__ == '__main__':
    unittest.main()
