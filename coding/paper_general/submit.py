#!/usr/bin/env python3
import requests
import json

URL = "http://94.237.120.119:35133/run"

# Read the solution code
with open('solution.py', 'r') as f:
    code = f.read()

# Submit the code
payload = {
    "code": code,
    "language": "python"
}

response = requests.post(URL, json=payload)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

# Try to parse as JSON
try:
    result = response.json()
    print(json.dumps(result, indent=2))
    
    if 'flag' in result:
        print(f"\n🎉 FLAG: {result['flag']}")
except:
    pass
