# 📄 backend/analyzers/static_analyzer.py - Feature Extraction
# ================================================================================

import os
import zipfile
import numpy as np
import logging

logger = logging.getLogger(__name__)

class StaticAnalyzer:
    def __init__(self):
        """Initialize static analyzer for APK files"""
        # DroidRL dataset feature mapping
        self.droidrl_permissions = [
            'ACCESS_CHECKIN_PROPERTIES', 'ACCESS_COARSE_LOCATION', 'ACCESS_FINE_LOCATION',
            'ACCESS_LOCATION_EXTRA_COMMANDS', 'ACCESS_MOCK_LOCATION', 'ACCESS_NETWORK_STATE',
            'ACCESS_SURFACE_FLINGER', 'ACCESS_WIFI_STATE', 'ACCOUNT_MANAGER', 'ADD_VOICEMAIL',
            'BATTERY_STATS', 'BIND_ACCESSIBILITY_SERVICE', 'BIND_APPWIDGET', 'BIND_DEVICE_ADMIN',
            'BIND_INPUT_METHOD', 'BIND_REMOTEVIEWS', 'BIND_TEXT_SERVICE', 'BIND_VPN_SERVICE',
            'BIND_WALLPAPER', 'BLUETOOTH', 'BLUETOOTH_ADMIN', 'BLUETOOTH_PRIVILEGED',
            'BRICK', 'BROADCAST_PACKAGE_REMOVED', 'BROADCAST_SMS', 'BROADCAST_STICKY',
            'BROADCAST_WAP_PUSH', 'CALL_PHONE', 'CALL_PRIVILEGED', 'CAMERA',
            'CAPTURE_AUDIO_OUTPUT', 'CAPTURE_SECURE_VIDEO_OUTPUT', 'CAPTURE_VIDEO_OUTPUT',
            'CHANGE_COMPONENT_ENABLED_STATE', 'CHANGE_CONFIGURATION', 'CHANGE_NETWORK_STATE',
            'CHANGE_WIFI_MULTICAST_STATE', 'CHANGE_WIFI_STATE', 'CLEAR_APP_CACHE',
            'CLEAR_APP_USER_DATA', 'CONTROL_LOCATION_UPDATES', 'DELETE_CACHE_FILES',
            'DELETE_PACKAGES', 'DEVICE_POWER', 'DIAGNOSTIC', 'DISABLE_KEYGUARD',
            'DUMP', 'EXPAND_STATUS_BAR', 'FACTORY_TEST', 'FLASHLIGHT', 'FORCE_BACK',
            'GET_ACCOUNTS', 'GET_PACKAGE_SIZE', 'GET_TASKS', 'GET_TOP_ACTIVITY_INFO',
            'GLOBAL_SEARCH', 'HARDWARE_TEST', 'INJECT_EVENTS', 'INSTALL_LOCATION_PROVIDER',
            'INSTALL_PACKAGES', 'INTERNAL_SYSTEM_WINDOW', 'INTERNET', 'KILL_BACKGROUND_PROCESSES',
            'LOCATION_HARDWARE', 'MANAGE_ACCOUNTS', 'MANAGE_APP_TOKENS', 'MANAGE_DOCUMENTS',
            'MASTER_CLEAR', 'MODIFY_AUDIO_SETTINGS', 'MODIFY_PHONE_STATE', 'MOUNT_FORMAT_FILESYSTEMS',
            'MOUNT_UNMOUNT_FILESYSTEMS', 'NFC', 'PERSISTENT_ACTIVITY', 'PROCESS_OUTGOING_CALLS',
            'READ_CALENDAR', 'READ_CALL_LOG', 'READ_CONTACTS', 'READ_EXTERNAL_STORAGE',
            'READ_FRAME_BUFFER', 'READ_HISTORY_BOOKMARKS', 'READ_INPUT_STATE', 'READ_LOGS',
            'READ_PHONE_STATE', 'READ_PROFILE', 'READ_SMS', 'READ_SOCIAL_STREAM',
            'READ_SYNC_SETTINGS', 'READ_SYNC_STATS', 'READ_USER_DICTIONARY', 'REBOOT',
            'RECEIVE_BOOT_COMPLETED', 'RECEIVE_MMS', 'RECEIVE_SMS', 'RECEIVE_WAP_PUSH',
            'RECORD_AUDIO', 'REORDER_TASKS', 'RESTART_PACKAGES', 'SEND_RESPOND_VIA_MESSAGE',
            'SEND_SMS', 'SET_ACTIVITY_WATCHER', 'SET_ALARM', 'SET_ALWAYS_FINISH',
            'SET_ANIMATION_SCALE', 'SET_DEBUG_APP', 'SET_ORIENTATION', 'SET_POINTER_SPEED',
            'SET_PREFERRED_APPLICATIONS', 'SET_PROCESS_LIMIT', 'SET_TIME', 'SET_TIME_ZONE',
            'SET_WALLPAPER', 'SET_WALLPAPER_HINTS', 'SIGNAL_PERSISTENT_PROCESSES',
            'STATUS_BAR', 'SUBSCRIBED_FEEDS_READ', 'SUBSCRIBED_FEEDS_WRITE', 'SYSTEM_ALERT_WINDOW',
            'UPDATE_DEVICE_STATS', 'USE_CREDENTIALS', 'USE_SIP', 'VIBRATE', 'WAKE_LOCK',
            'WRITE_APN_SETTINGS', 'WRITE_CALENDAR', 'WRITE_CALL_LOG', 'WRITE_CONTACTS',
            'WRITE_EXTERNAL_STORAGE', 'WRITE_GSERVICES', 'WRITE_HISTORY_BOOKMARKS',
            'WRITE_PROFILE', 'WRITE_SECURE_SETTINGS', 'WRITE_SETTINGS', 'WRITE_SMS',
            'WRITE_SOCIAL_STREAM', 'WRITE_SYNC_SETTINGS', 'WRITE_USER_DICTIONARY'
        ]
        
        # Banking-specific critical permissions
        self.banking_critical = [
            'SEND_SMS', 'READ_SMS', 'CALL_PHONE', 'READ_PHONE_STATE',
            'SYSTEM_ALERT_WINDOW', 'BIND_ACCESSIBILITY_SERVICE', 'CAMERA',
            'RECORD_AUDIO', 'ACCESS_FINE_LOCATION'
        ]
    
    def extract_features(self, apk_path):
        """Extract features from APK file (simplified for demo)"""
        try:
            logger.info(f"🔍 Extracting features from: {apk_path}")
            
            # For demo purposes, generate realistic feature vector
            # In production, you'd use androguard or similar tools
            features = {}
            
            # Initialize all permission features to 0
            for perm in self.droidrl_permissions:
                features[f'permission_{perm}'] = 0
            
      
             # Simulate some realistic permission detection
            # Banking apps typically have these permissions
            common_banking_perms = [
                'INTERNET', 'ACCESS_NETWORK_STATE', 'ACCESS_WIFI_STATE', 'CAMERA',
                'READ_PHONE_STATE', 'VIBRATE', 'WAKE_LOCK'
            ]
            
            # Randomly assign some permissions (simulation)
            for perm in common_banking_perms:
                if perm in self.droidrl_permissions:
                    features[f'permission_{perm}'] = np.random.choice([0, 1], p=[0.3, 0.7])
            
            # Add some suspicious permissions randomly
            suspicious_perms = ['SEND_SMS', 'READ_SMS', 'CALL_PHONE', 'SYSTEM_ALERT_WINDOW']
            for perm in suspicious_perms:
                if perm in self.droidrl_permissions:
                    features[f'permission_{perm}'] = np.random.choice([0, 1], p=[0.7, 0.3])
            
            logger.info(f"✅ Extracted {len(features)} features")
            return features
            
        except Exception as e:
            logger.error(f"❌ Feature extraction failed: {str(e)}")
            return self._get_default_features()
    
    def features_to_vector(self, features_dict):
        """Convert features dict to ML-compatible vector"""
        # Create feature vector matching DroidRL dataset structure
        feature_vector = []
        
        for perm in self.droidrl_permissions:
            feature_key = f'permission_{perm}'
            feature_vector.append(features_dict.get(feature_key, 0))
        
        return np.array(feature_vector)
    
    def _get_default_features(self):
        """Return default features if extraction fails"""
        features = {}
        for perm in self.droidrl_permissions:
            features[f'permission_{perm}'] = 0
        return features
