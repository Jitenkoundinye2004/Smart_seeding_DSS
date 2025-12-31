import sys
import os

# Add ml-backend directory to the Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'ml-backend'))

# Import the Flask app from ml-backend/app.py
from app import app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
