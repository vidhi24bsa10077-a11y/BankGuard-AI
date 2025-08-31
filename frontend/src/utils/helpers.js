export const generateDashboardStats = () => {
  return {
    appsProtected: Math.floor(Math.random() * 1000) + 2500,
    successRate: Math.floor(Math.random() * 5) + 95,
    threatsToday: Math.floor(Math.random() * 30) + 15,
    appsAnalyzed: Math.floor(Math.random() * 50) + 120,
    breaches: 0,
    neuralActivity: Math.floor(Math.random() * 20) + 70
  };
};

export const generateThreatIntelligence = () => {
  const threatTypes = ['Banking Trojan', 'UI Spoofing', 'Permission Abuse', 'Credential Stealer', 'SMS Interceptor'];
  const threatNames = [
    'Fake Wells Fargo App', 'Chase Phishing Clone', 'Suspicious BankApp', 
    'HDFC Banking Fake', 'SBI Mobile Clone', 'Axis Bank Impostor',
    'ICICI Phishing App', 'Kotak Banking Fake', 'PNB Mobile Clone'
  ];
  
  const severities = ['CRITICAL', 'SUSPICIOUS'];
  const timeAgo = ['2 mins ago', '15 mins ago', '1 hour ago', '3 hours ago', '6 hours ago'];
  
  return Array.from({ length: 6 }, (_, i) => ({
    id: `threat_${Date.now()}_${i}`,
    name: threatNames[Math.floor(Math.random() * threatNames.length)],
    type: threatTypes[Math.floor(Math.random() * threatTypes.length)],
    severity: severities[Math.floor(Math.random() * severities.length)],
    timeAgo: timeAgo[Math.floor(Math.random() * timeAgo.length)]
  }));
};

export const generateReportsData = () => {
  const filenames = [
    'sbi_mobile_banking.apk', 'hdfc_bank_app.apk', 'icici_imobile.apk',
    'axis_mobile_banking.apk', 'fake_banking_app.apk', 'suspicious_bank.apk',
    'kotak_mobile.apk', 'pnb_banking.apk', 'union_bank_mobile.apk'
  ];
  
  const verdicts = ['SAFE', 'MALICIOUS', 'SUSPICIOUS'];
  
  return Array.from({ length: 25 }, (_, i) => ({
    id: `report_${i}`,
    filename: filenames[Math.floor(Math.random() * filenames.length)],
    verdict: verdicts[Math.floor(Math.random() * verdicts.length)],
    riskScore: Math.floor(Math.random() * 10) + 1,
    confidence: Math.floor(Math.random() * 30) + 70,
    timestamp: new Date(Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000).toLocaleDateString(),
    analysisTime: (Math.random() * 20 + 5).toFixed(1),
    threats: Math.floor(Math.random() * 5)
  }));
};

export const simulateAnalysis = (filename) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const riskScore = Math.floor(Math.random() * 10) + 1;
      const confidence = Math.floor(Math.random() * 30) + 70;
      
      resolve({
        filename,
        verdict: riskScore >= 6 ? 'MALICIOUS' : 'SAFE',
        riskScore,
        confidence,
        threats: riskScore >= 6 ? Math.floor(Math.random() * 5) + 1 : 0,
        analysisTime: (Math.random() * 20 + 10).toFixed(1),
        timestamp: new Date().toISOString()
      });
    }, 3000);
  });
};

export const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

export const getStatusColor = (verdict) => {
  switch (verdict.toLowerCase()) {
    case 'safe': case 'legitimate': return 'text-green-400';
    case 'malicious': case 'dangerous': return 'text-red-400';
    case 'suspicious': return 'text-yellow-400';
    default: return 'text-gray-400';
  }
};

export const getRiskLevelText = (score) => {
  if (score <= 3) return 'LOW RISK';
  if (score <= 6) return 'MEDIUM RISK';
  return 'HIGH RISK';
};
