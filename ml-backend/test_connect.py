import requests
import os
from dotenv import load_dotenv

load_dotenv()
port = os.getenv('PORT', '5001')

try:
    print(f"Attempting to connect to http://localhost:{port}/dropdowns...")
    response = requests.get(f"http://localhost:{port}/dropdowns", timeout=5)
    with open('response.txt', 'w', encoding='utf-8') as f:
        f.write(f"Status Code: {response.status_code}\n")
        f.write(f"Response:\n{response.text}")
    print("Done")
except Exception as e:
    print(f"Connection failed: {e}")
