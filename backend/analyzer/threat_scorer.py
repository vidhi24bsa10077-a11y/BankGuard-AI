# 📄 backend/analyzers/threat_scorer.py - Risk Scoring Engine
# ================================================================================

import numpy as np
import logging

logger = logging.getLogger(__name__)

class ThreatScorer:
    def __init__(self):
        """Initialize threat scoring engine"""
        self.risk_thresholds = {
            'LOW': (0, 3),
            'MEDIUM': (3, 6),
            'HIGH': (6, 8),
            'CRITICAL': (8, 10)
        }
        
        self.banking_risk_multipliers = {
            'sms_permissions': 2.0,     # SMS access doubles risk
            'overlay_capability': 2.5,  # Overlay attacks are critical
            'accessibility_abuse': 3.0, # Accessibility abuse is highest risk
            'phone_access': 1.8,        # Phone access increases risk
            'location_tracking': 1.2    # Location tracking moderate risk
        }
    
    def calculate_comprehensive_risk(self, permission_analysis, static_features=None):
        """Calculate comprehensive risk score"""
        try:
            base_risk = permission_analysis.get('risk_score', 0.0)
            
            # Apply banking-specific multipliers
            multiplier = 1.0
            
            # Check for SMS-related permissions
            sms_perms = ['SEND_SMS', 'READ_SMS', 'RECEIVE_SMS']
            sms_detected = any(
                pattern['permission'] in sms_perms 
                for pattern in permission_analysis.get('suspicious_patterns', [])
            )
            if sms_detected:
                multiplier *= self.banking_risk_multipliers['sms_permissions']
            
            # Check for overlay capabilities
            overlay_perms = ['SYSTEM_ALERT_WINDOW']
            overlay_detected = any(
                pattern['permission'] in overlay_perms 
                for pattern in permission_analysis.get('suspicious_patterns', [])
            )
            if overlay_detected:
                multiplier *= self.banking_risk_multipliers['overlay_capability']
            
            # Check for accessibility abuse
            accessibility_perms = ['BIND_ACCESSIBILITY_SERVICE']
            accessibility_detected = any(
                pattern['permission'] in accessibility_perms 
                for pattern in permission_analysis.get('suspicious_patterns', [])
            )
            if accessibility_detected:
                multiplier *= self.banking_risk_multipliers['accessibility_abuse']
            
            # Calculate final risk score
            final_risk = min(base_risk * multiplier, 10.0)
            threat_level = self._get_threat_level(final_risk)
            
            return {
                'base_risk_score': base_risk,
                'risk_multiplier': multiplier,
                'final_risk_score': round(final_risk, 2),
                'threat_level': threat_level,
                'risk_factors': self._identify_risk_factors(permission_analysis),
                'mitigation_recommendations': self._get_mitigation_recommendations(threat_level)
            }
            
        except Exception as e:
            logger.error(f"Risk calculation failed: {str(e)}")
            return {
                'base_risk_score': 0.0,
                'risk_multiplier': 1.0,
                'final_risk_score': 0.0,
                'threat_level': 'UNKNOWN',
                'risk_factors': [],
                'mitigation_recommendations': ['Unable to assess risk']
            }
    
    def _get_threat_level(self, risk_score):
        """Determine threat level based on risk score"""
        for level, (min_score, max_score) in self.risk_thresholds.items():
            if min_score <= risk_score < max_score:
                return level
        return 'CRITICAL'  # For scores >= 8
    
    def _identify_risk_factors(self, permission_analysis):
        """Identify specific risk factors"""
        risk_factors = []
        
        for pattern in permission_analysis.get('suspicious_patterns', []):
            if pattern.get('risk_level') in ['CRITICAL', 'HIGH']:
                risk_factors.append({
                    'factor': pattern['permission'],
                    'severity': pattern['risk_level'],
                    'description': pattern['explanation']
                })
        
        return risk_factors
    
    def _get_mitigation_recommendations(self, threat_level):
        """Get mitigation recommendations based on threat level"""
        recommendations = {
            'LOW': [
                'Continue routine monitoring',
                'Regular security updates recommended',
                'User education on app permissions'
            ],
            'MEDIUM': [
                'Enhanced monitoring required',
                'Review app permissions carefully',
                'Consider app usage restrictions',
                'Regular security assessments'
            ],
            'HIGH': [
                'Immediate investigation required',
                'Block app installation if possible',
                'Alert security team',
                'Preserve evidence for analysis',
                'User notification recommended'
            ],
            'CRITICAL': [
                'IMMEDIATE BLOCKING REQUIRED',
                'Quarantine app immediately',
                'Full forensic investigation',
                'Law enforcement notification',
                'User credential reset recommended',
                'System-wide security alert'
            ]
        }
        
        return recommendations.get(threat_level, ['Unknown threat level - manual review required'])
