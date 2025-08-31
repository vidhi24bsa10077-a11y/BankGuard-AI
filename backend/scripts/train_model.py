# 📄 backend/scripts/train_model.py - Model Training Script
# ================================================================================

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
from models.banking_classifier import BankingAPKClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train_bankguard_model():
    """Train BankGuard model on DroidRL dataset"""
    try:
        print("🚀 Starting BankGuard AI Model Training")
        print("📊 Dataset: DroidRL fullset_train.csv")
        print("="*60)
        
        # Initialize classifier
        classifier = BankingAPKClassifier()
        
        # Check if dataset exists
        dataset_path = 'data/datasets/fullset_train.csv'
        if not os.path.exists(dataset_path):
            print(f"❌ Dataset not found: {dataset_path}")
            print(f"Please ensure fullset_train.csv is in: {os.path.abspath(dataset_path)}")
            return None
        
        print(f"📂 Loading dataset: {dataset_path}")
        
        # Load and examine dataset
        df = pd.read_csv(dataset_path)
        print(f"✅ Dataset loaded successfully!")
        print(f"   Shape: {df.shape}")
        print(f"   Features: {df.shape[1] - 1}")
        print(f"   Samples: {df.shape[0]}")
        
        # Check label distribution
        if 'class' in df.columns:
            label_col = 'class'
        elif 'label' in df.columns:
            label_col = 'label'
        else:
            label_col = df.columns[-1]
            print(f"⚠️  Assuming last column '{label_col}' is the label")
        
        label_counts = df[label_col].value_counts()
        print(f"📊 Label distribution:")
        for label, count in label_counts.items():
            print(f"   {label}: {count} samples ({count/len(df)*100:.1f}%)")
        
        print("\n🤖 Training ensemble model...")
        print("   Models: Random Forest + XGBoost + SVM + Logistic Regression")
        
        # Train the model
        accuracy = classifier.train_on_dataset(dataset_path)
        
        print(f"\n🎯 Training Results:")
        print(f"   Accuracy: {accuracy:.3f}")
        print(f"   Training samples: {classifier.training_samples}")
        print(f"   Features: {len(classifier.feature_names)}")
        
        # Save the trained model
        model_save_path = 'data/trained_models/bankguard_model.joblib'
        os.makedirs('data/trained_models', exist_ok=True)
        classifier.save_model(model_save_path)
        print(f"💾 Model saved: {model_save_path}")
        
        # Test prediction with sample data
        print("\n🧪 Testing prediction capability...")
        test_features = np.zeros(len(classifier.feature_names))
        
        # Set some sample permissions for testing
        if 'permission_INTERNET' in classifier.feature_names:
            idx = classifier.feature_names.index('permission_INTERNET')
            test_features[idx] = 1
        
        if 'permission_READ_PHONE_STATE' in classifier.feature_names:
            idx = classifier.feature_names.index('permission_READ_PHONE_STATE')
            test_features[idx] = 1
        
        test_result = classifier.predict_with_explanation(test_features)
        print(f"   Sample prediction: {test_result['prediction']}")
        print(f"   Risk score: {test_result['risk_score']}/10")
        print(f"   Confidence: {test_result['confidence']}%")
        
        print("\n✅ Model training completed successfully!")
        print("🚀 Ready for demo and analysis!")
        
        return classifier
        
    except Exception as e:
        print(f"❌ Training failed: {str(e)}")
        logger.error(f"Training error: {str(e)}")
        return None

if __name__ == "__main__":
    model = train_bankguard_model()
