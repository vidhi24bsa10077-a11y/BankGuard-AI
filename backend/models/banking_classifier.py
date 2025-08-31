# 📄 backend/models/banking_classifier.py - ML Model for DroidRL Dataset
# ================================================================================

import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import xgboost as xgb
import time
import logging

logger = logging.getLogger(__name__)

class BankingAPKClassifier:
    def __init__(self):
        """Initialize the banking APK classifier for DroidRL dataset"""
        self.scaler = StandardScaler()
        self.model = None
        self.feature_names = None
        self.is_trained = False
        self.training_samples = 0
        
        # Banking-specific permission weights (DroidRL feature naming)
        self.critical_features = {
            'permission_SEND_SMS': 9.0,
            'permission_READ_SMS': 8.5,
            'permission_CALL_PHONE': 8.0,
            'permission_READ_PHONE_STATE': 7.5,
            'permission_SYSTEM_ALERT_WINDOW': 9.5,
            'permission_WRITE_EXTERNAL_STORAGE': 6.0,
            'permission_CAMERA': 6.5,
            'permission_RECORD_AUDIO': 8.0,
            'permission_ACCESS_FINE_LOCATION': 5.5,
            'permission_INTERNET': 4.0
        }
        
        self._build_ensemble_model()
    
    def _build_ensemble_model(self):
        """Build ensemble model optimized for DroidRL dataset"""
        # Random Forest - excellent for permission features
        rf_model = RandomForestClassifier(
            n_estimators=300,
            max_depth=20,
            min_samples_split=5,
            min_samples_leaf=2,
            max_features='sqrt',
            random_state=42,
            n_jobs=-1
        )
        
        # XGBoost - great for structured features
        xgb_model = xgb.XGBClassifier(
            n_estimators=200,
            max_depth=15,
            learning_rate=0.1,
            subsample=0.9,
            colsample_bytree=0.8,
            random_state=42,
            eval_metric='logloss'
        )
        
        # SVM with RBF kernel
        svm_model = SVC(
            kernel='rbf',
            C=1.0,
            gamma='scale',
            probability=True,
            random_state=42
        )
        
        # Logistic Regression for interpretability
        lr_model = LogisticRegression(
            C=1.0,
            solver='liblinear',
            random_state=42,
            max_iter=1000
        )
        
        # Create ensemble with optimized weights
        self.model = VotingClassifier(
            estimators=[
                ('rf', rf_model),
                ('xgb', xgb_model),
                ('svm', svm_model),
                ('lr', lr_model)
            ],
            voting='soft',
            weights=[0.35, 0.30, 0.20, 0.15]  # RF gets highest weight
        )
        
        logger.info("✅ Ensemble model created: RF + XGBoost + SVM + LogisticRegression")
    
    def train_on_dataset(self, dataset_path='data/datasets/fullset_train.csv'):
        """Train model on DroidRL dataset"""
        try:
            logger.info(f"📊 Loading DroidRL dataset from: {dataset_path}")
            
            # Load the DroidRL dataset
            df = pd.read_csv(dataset_path)
            logger.info(f"Dataset loaded: {df.shape[0]} samples, {df.shape[1]} features")
            
            # Prepare features and labels
            # DroidRL dataset has 'class' column: 0=benign, 1=malware
            if 'class' in df.columns:
                X = df.drop(['class'], axis=1).values
                y = df['class'].values
                self.feature_names = df.drop(['class'], axis=1).columns.tolist()
            elif 'label' in df.columns:
                X = df.drop(['label'], axis=1).values
                y = df['label'].values
                self.feature_names = df.drop(['label'], axis=1).columns.tolist()
            else:
                # Assume last column is label
                X = df.iloc[:, :-1].values
                y = df.iloc[:, -1].values
                self.feature_names = df.columns[:-1].tolist()
            
            self.training_samples = X.shape[0]
            logger.info(f"Features: {len(self.feature_names)}")
            logger.info(f"Benign samples: {np.sum(y == 0)}")
            logger.info(f"Malware samples: {np.sum(y == 1)}")
            
            # Split for training and testing
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            logger.info("🔄 Scaling features...")
            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)
            
            logger.info("🤖 Training ensemble model...")
            # Train ensemble model
            self.model.fit(X_train_scaled, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test_scaled)
            accuracy = accuracy_score(y_test, y_pred)
            
            logger.info(f"✅ Model training completed!")
            logger.info(f"📈 Test Accuracy: {accuracy:.3f}")
            
            # Cross-validation for robustness
            cv_scores = cross_val_score(self.model, X_train_scaled, y_train, cv=5)
            logger.info(f"📊 Cross-validation accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
            
            print("\n" + "="*50)
            print("🎯 DETAILED CLASSIFICATION REPORT:")
            print("="*50)
            print(classification_report(y_test, y_pred, target_names=['Benign', 'Malware']))
            print("\n📊 CONFUSION MATRIX:")
            print(confusion_matrix(y_test, y_pred))
            print("="*50)
            
            self.is_trained = True
            return accuracy
            
        except Exception as e:
            logger.error(f"❌ Training failed: {str(e)}")
            raise
    
    def predict_with_explanation(self, features):
        """Predict with detailed explanation"""
        start_time = time.time()
        
        try:
            if not self.is_trained:
                raise ValueError("Model not trained. Call train_on_dataset() first.")
            
            # Handle different input formats
            if isinstance(features, dict):
                feature_vector = self._dict_to_vector(features)
            elif isinstance(features, list):
                feature_vector = np.array(features).reshape(1, -1)
            else:
                feature_vector = np.array(features).reshape(1, -1)
            
            # Ensure correct number of features
            if feature_vector.shape[1] != len(self.feature_names):
                logger.warning(f"Feature mismatch: got {feature_vector.shape[1]}, expected {len(self.feature_names)}")
                # Pad or truncate as needed
                if feature_vector.shape[1] < len(self.feature_names):
                    padding = np.zeros((1, len(self.feature_names) - feature_vector.shape[1]))
                    feature_vector = np.concatenate([feature_vector, padding], axis=1)
                else:
                    feature_vector = feature_vector[:, :len(self.feature_names)]
            
            # Scale features
            feature_vector_scaled = self.scaler.transform(feature_vector)
            
            # Make prediction
            prediction = self.model.predict(feature_vector_scaled)[0]
            prediction_proba = self.model.predict_proba(feature_vector_scaled)[0]
            
            # Calculate risk score (0-10 scale)
            risk_score = prediction_proba[1] * 10
            confidence = max(prediction_proba)
            
            # Generate explanation
            explanation = self._generate_explanation(feature_vector[0], prediction, risk_score)
            
            processing_time = time.time() - start_time
            
            return {
                'prediction': 'MALICIOUS' if prediction == 1 else 'LEGITIMATE',
                'risk_score': round(risk_score, 2),
                'confidence': round(confidence * 100, 1),
                'explanation': explanation,
                'processing_time': round(processing_time, 2),
                'prediction_probabilities': {
                    'legitimate': round(prediction_proba[0] * 100, 1),
                    'malicious': round(prediction_proba[1] * 100, 1)
                }
            }
            
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            return {
                'prediction': 'ERROR',
                'risk_score': 0,
                'confidence': 0,
                'explanation': {'summary': f'Analysis failed: {str(e)}'},
                'processing_time': 0
            }
    
    def _generate_explanation(self, feature_vector, prediction, risk_score):
        """Generate human-readable explanation"""
        explanation = {
            'summary': '',
            'key_indicators': [],
            'risk_factors': [],
            'recommendation': ''
        }
        
        # Analyze critical features
        critical_features_detected = []
        for i, feature_name in enumerate(self.feature_names):
            if i < len(feature_vector) and feature_vector[i] == 1:
                if feature_name in self.critical_features:
                    critical_features_detected.append({
                        'feature': feature_name,
                        'risk_weight': self.critical_features[feature_name],
                        'explanation': self._get_feature_explanation(feature_name)
                    })
        
        # Sort by risk weight
        critical_features_detected.sort(key=lambda x: x['risk_weight'], reverse=True)
        
        # Generate summary
        if prediction == 1:  # Malicious
            explanation['summary'] = f"APK classified as MALICIOUS with {risk_score:.1f}/10 risk score."
            explanation['recommendation'] = "⚠️ IMMEDIATE ACTION: Block this application and investigate further."
            explanation['key_indicators'] = [f"Critical feature: {f['feature']}" for f in critical_features_detected[:3]]
        else:  # Legitimate
            explanation['summary'] = f"APK appears LEGITIMATE with {risk_score:.1f}/10 risk score."
            explanation['recommendation'] = "✅ Application appears safe. Continue routine monitoring."
            explanation['key_indicators'] = ["Normal permission patterns", "Standard app behavior", "No malicious signatures"]
        
        explanation['risk_factors'] = critical_features_detected
        
        return explanation
    
    def _get_feature_explanation(self, feature_name):
        """Get explanation for feature importance"""
        explanations = {
            'permission_SEND_SMS': 'Can send SMS - potential for premium rate fraud',
            'permission_READ_SMS': 'Can read SMS - may intercept OTP codes',
            'permission_CALL_PHONE': 'Can make phone calls - unusual for banking apps',
            'permission_SYSTEM_ALERT_WINDOW': 'Can display overlays - screen hijacking risk',
            'permission_CAMERA': 'Camera access - potential for unauthorized recording',
            'permission_RECORD_AUDIO': 'Audio recording - privacy violation risk',
            'permission_ACCESS_FINE_LOCATION': 'Location tracking - privacy concern',
            'permission_WRITE_EXTERNAL_STORAGE': 'File system access - data theft potential'
        }
        
        return explanations.get(feature_name, f'Feature {feature_name} detected')
    
    def _dict_to_vector(self, features_dict):
        """Convert feature dictionary to vector"""
        if self.feature_names is None:
            raise ValueError("Feature names not defined. Train model first.")
        
        feature_vector = []
        for feature_name in self.feature_names:
            feature_vector.append(features_dict.get(feature_name, 0))
        
        return np.array(feature_vector).reshape(1, -1)
    
    def save_model(self, model_path):
        """Save trained model and components"""
        try:
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            
            model_data = {
                'model': self.model,
                'scaler': self.scaler,
                'feature_names': self.feature_names,
                'is_trained': self.is_trained,
                'training_samples': self.training_samples,
                'critical_features': self.critical_features
            }
            
            joblib.dump(model_data, model_path)
            logger.info(f"💾 Model saved to: {model_path}")
            
        except Exception as e:
            logger.error(f"Failed to save model: {str(e)}")
            raise
    
    def load_model(self, model_path):
        """Load pre-trained model"""
        try:
            model_data = joblib.load(model_path)
            
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.feature_names = model_data['feature_names']
            self.is_trained = model_data['is_trained']
            self.training_samples = model_data.get('training_samples', 0)
            self.critical_features = model_data.get('critical_features', {})
            
            logger.info(f"📂 Model loaded from: {model_path}")
            logger.info(f"Features: {len(self.feature_names)}")
            logger.info(f"Training samples: {self.training_samples}")
            
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise
