# 📄 scripts/demo_data_generator.py - Generate Demo Data
# ================================================================================

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta

def generate_demo_dataset():
    """Generate demo dataset matching DroidRL format"""
    print("🎲 Generating demo dataset...")
    
    # DroidRL has 583 features (457 permissions + 126 intents)
    n_samples = 1000
    n_features = 583
    
    # Generate random binary features
    X = np.random.choice([0, 1], size=(n_samples, n_features), p=[0.8, 0.2])
    
    # Generate labels (30% malicious, 70% benign)
    y = np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])
    
    # Create feature names (simplified)
    feature_names = []
    
    # Permission features (457)
    permission_names = [
        'INTERNET', 'ACCESS_NETWORK_STATE', 'ACCESS_WIFI_STATE', 'VIBRATE',
        'WAKE_LOCK', 'CAMERA', 'RECORD_AUDIO', 'READ_PHONE_STATE',
        'SEND_SMS', 'READ_SMS', 'RECEIVE_SMS', 'CALL_PHONE',
        'SYSTEM_ALERT_WINDOW', 'BIND_ACCESSIBILITY_SERVICE',
        'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION',
        'WRITE_EXTERNAL_STORAGE', 'READ_EXTERNAL_STORAGE'
    ]
    
    # Extend to 457 permissions
    for i in range(457):
        if i < len(permission_names):
            feature_names.append(f'permission_{permission_names[i]}')
        else:
            feature_names.append(f'permission_FEATURE_{i}')
    
    # Intent features (126)
    for i in range(126):
        feature_names.append(f'intent_ACTION_{i}')
    
    # Create DataFrame
    df = pd.DataFrame(X, columns=feature_names)
    df['class'] = y
    
    # Make malicious samples more suspicious
    malicious_mask = df['class'] == 1
    
    # Increase suspicious permissions for malicious samples
    suspicious_perms = ['permission_SEND_SMS', 'permission_READ_SMS', 'permission_SYSTEM_ALERT_WINDOW']
    for perm in suspicious_perms:
        if perm in df.columns:
            df.loc[malicious_mask, perm] = np.random.choice([0, 1], 
                                                          size=malicious_mask.sum(), 
                                                          p=[0.3, 0.7])
    
    # Save dataset
    os.makedirs('data/datasets', exist_ok=True)
    output_path = 'data/datasets/demo_fullset_train.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✅ Demo dataset saved: {output_path}")
    print(f"   Shape: {df.shape}")
    print(f"   Benign: {(df['class'] == 0).sum()}")
    print(f"   Malicious: {(df['class'] == 1).sum()}")
    
    return output_path

def generate_analysis_history():
    """Generate fake analysis history for demo"""
    print("📊 Generating analysis history...")
    
    analyses = []
    
    for i in range(50):
        risk_score = np.random.uniform(0, 10)
        verdict = 'MALICIOUS' if risk_score >= 6 else 'LEGITIMATE'
        confidence = np.random.uniform(75, 98)
        
        analysis = {
            'analysis_id': f'analysis_{i}',
            'filename': f'banking_app_{i}.apk',
            'timestamp': (datetime.now() - timedelta(days=np.random.randint(0, 30))).isoformat(),
            'prediction': verdict,
            'risk_score': round(risk_score, 2),
            'confidence': round(confidence, 1),
            'processing_time': round(np.random.uniform(5, 25), 1),
            'explanation': {
                'summary': f'APK classified as {verdict}',
                'key_indicators': ['Static analysis completed', 'Permission check done']
            },
            'forensic_report': {
                'report_id': f'report_{i}',
                'generated_at': datetime.now().isoformat()
            }
        }
        
        analyses.append(analysis)
    
    # Save to database file
    db_data = {
        'analyses': analyses,
        'metadata': {
            'created': datetime.now().isoformat(),
            'total_analyses': len(analyses)
        }
    }
    
    os.makedirs('data', exist_ok=True)
    with open('data/analysis_results.json', 'w') as f:
        json.dump(db_data, f, indent=2)
    
    print(f"✅ Generated {len(analyses)} analysis records")
    print("💾 Saved to: data/analysis_results.json")

def setup_demo_environment():
    """Set up complete demo environment"""
    print("🎬 Setting up demo environment...")
    
    # Generate demo dataset if real one not available
    if not os.path.exists('data/datasets/fullset_train.csv'):
        print("📊 Real dataset not found, generating demo dataset...")
        generate_demo_dataset()
    
    # Generate analysis history
    generate_analysis_history()
    
    print("✅ Demo environment ready!")

if __name__ == "__main__":
    setup_demo_environment()
