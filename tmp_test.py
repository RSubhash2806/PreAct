import requests
import json

payload = {"query": "What is the weather in Paris? Please calculate 5 times that temperature."}
try:
    res = requests.post("http://localhost:8000/chat", json=payload)
    print(json.dumps(res.json(), indent=2))
except Exception as e:
    print(f"Failed to connect: {e}")
