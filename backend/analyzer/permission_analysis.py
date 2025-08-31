# 📄 backend/analyzers/permission_analyzer.py - Banking Permission Analysis
# ================================================================================

import logging

logger = logging.getLogger(__name__)

class PermissionAnalyzer:
    def __init__(self):
        """Initialize permission analyzer for banking apps"""
        self.banking_permission_weights = {
            'SEND_SMS': 9.0,           # Critical - SMS fraud
            'READ_SMS': 8.5,           # Critical - OTP theft
            'CALL_PHONE': 8.0,         # High - unusual for banking
            'READ_PHONE_STATE': 7.5,   # High - device identification
            'SYSTEM_ALERT_WINDOW': 9.5, # Critical - overlay attacks
            'BIND_ACCESSIBILITY_SERVICE': 9.8, # Critical - UI control
            'CAMERA': 6.5,             # Medium - privacy concern
            'RECORD_AUDIO': 8.0,       # High - privacy violation
            'ACCESS_FINE_LOCATION': 5.5, # Medium - tracking
            'WRITE_EXTERNAL_STORAGE': 6.0, # Medium - data access
            'READ_CONTACTS': 7.0,      # High - PII theft
            'CALL_PRIVILEGED': 8.5,    # High - system abuse
            'RECEIVE_SMS': 7.0,        # High - SMS interception
            'PROCESS_OUTGOING_CALLS': 8.0 # High - call manipulation
        }
    
    def analyze_permissions(self, permission_features):
        """Analyze permission patterns for banking malware indicators"""
        try:
            analysis_result = {
                'total_permissions': 0,
                'critical_permissions': 0,
                'risk_score': 0.0,
                'suspicious_patterns': [],
                'banking_relevance': 'LOW'
            }
            
            total_risk = 0.0
            critical_count = 0
            total_count = 0
            
            for feature_name, value in permission_features.items():
                if feature_name.startswith('permission_') and value == 1:
                    total_count += 1
                    perm_name = feature_name.replace('permission_', '')
                    
                    if perm_name in self.banking_permission_weights:
                        risk_weight = self.banking_permission_weights[perm_name]
                        total_risk += risk_weight
                        
                        if risk_weight >= 8.0:
                            critical_count += 1
                            analysis_result['suspicious_patterns'].append({
                                'permission': perm_name,
                                'risk_level': 'CRITICAL',
                                'weight': risk_weight,
                                'explanation': self._get_permission_explanation(perm_name)
                            })
                        elif risk_weight >= 6.0:
                            analysis_result['suspicious_patterns'].append({
                                'permission': perm_name,
                                'risk_level': 'HIGH',
                                'weight': risk_weight,
                                'explanation': self._get_permission_explanation(perm_name)
                            })
            
            analysis_result['total_permissions'] = total_count
            analysis_result['critical_permissions'] = critical_count
            analysis_result['risk_score'] = min(total_risk / 10.0, 10.0)  # Normalize to 0-10
            
            # Determine banking relevance
            if critical_count >= 3:
                analysis_result['banking_relevance'] = 'HIGH'
            elif critical_count >= 1:
                analysis_result['banking_relevance'] = 'MEDIUM'
            else:
                analysis_result['banking_relevance'] = 'LOW'
            
            return analysis_result
            
        except Exception as e:
            logger.error(f"Permission analysis failed: {str(e)}")
            return {
                'total_permissions': 0,
                'critical_permissions': 0,
                'risk_score': 0.0,
                'suspicious_patterns': [],
                'banking_relevance': 'UNKNOWN'
            }
    
    def _get_permission_explanation(self, permission):
        """Get detailed explanation for permission risks"""
        explanations = {
            'SEND_SMS': 'Can send SMS messages - enables premium SMS fraud and unauthorized charges',
            'READ_SMS': 'Can read SMS messages - allows theft of OTP codes and transaction confirmations',
            'CALL_PHONE': 'Can make phone calls - unusual for banking apps, potential for premium rate calls',
            'SYSTEM_ALERT_WINDOW': 'Can display overlay windows - enables fake login screen attacks',
            'BIND_ACCESSIBILITY_SERVICE': 'Accessibility service control - can automate malicious actions',
            'CAMERA': 'Camera access - potential for unauthorized recording of sensitive information',
            'RECORD_AUDIO': 'Audio recording - privacy violation and eavesdropping capability',
            'READ_PHONE_STATE': 'Device state access - enables device fingerprinting and tracking',
            'ACCESS_FINE_LOCATION': 'Precise location access - enables user tracking and profiling'
        }
        
        return explanations.get(permission, f'Permission {permission} requires security review')
