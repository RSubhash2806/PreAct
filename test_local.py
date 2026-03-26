from dotenv import load_dotenv
load_dotenv()
from app.orchestrator import orchestrator
import json

print("\n--- Starting Isolated Local DAG Test ---")
try:
    result = orchestrator.run_loop("Plan a trip to Goa considering weather and budget. Calculate a budget and check weather.")
    print("\n[SUCCESS] Final Output:")
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"\n[ERROR] CRASHED: {e}")
