import requests
import json

payload = {"query": "Plan a trip to Goa considering weather and budget. Calculate a budget and check weather."}
try:
    print("Sending request to backend... (this might take 10-20 seconds to compile DAG and execute)")
    res = requests.post("http://localhost:8000/chat", json=payload)
    data = res.json()
    
    print("\n" + "="*50)
    print(f"Goal: {data.get('query')}")
    print(f"Progress: {data.get('progress') * 100}%")
    print(f"Steps taken: {data.get('steps_taken')}")
    print("Final Output:\n")
    print(data.get('final_answer'))
    print("="*50 + "\n")
except Exception as e:
    print(f"Failed to connect: {e}")
