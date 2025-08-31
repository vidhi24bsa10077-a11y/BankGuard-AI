# 📄 scripts/quick_start.sh - Quick Start Script
# ================================================================================

#!/bin/bash

echo "🚀 BankGuard AI - Quick Start Setup"
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Setup backend
echo ""
echo "📦 Setting up backend..."
cd backend/
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Create directories
python scripts/setup.py

# Train model if dataset available
if [ -f "data/datasets/fullset_train.csv" ]; then
    echo "🤖 Training model..."
    python scripts/train_model.py
else
    echo "⚠️ Dataset not found. Place fullset_train.csv in data/datasets/"
    echo "   System will run in demo mode"
fi

echo "✅ Backend setup completed!"

# Setup frontend
echo ""
echo "🎨 Setting up frontend..."
cd ../frontend/
npm install

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "🚀 To start the application:"
echo "   Backend:  cd backend && python app.py"
echo "   Frontend: cd frontend && npm start"
echo ""
echo "📱 Access the application at: http://localhost:3000"
echo "🔗 API documentation at: http://localhost:5000/api/health"
