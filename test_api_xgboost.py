import requests
import json

# URL ของ API (รันในเครื่อง)
url = "http://127.0.0.1:10000/predict"

# ข้อมูลตัวอย่าง (Mock Data)
payload = {
    "gold": 2000.0,
    "oil": 80.0,
    "bond_yield": 4.5,
    "dxy": 105.0,
    "sp500": 4500.0,
    "set_index": 1400.0,
    "rsi": 50.0,
    "macd": 0.1,
    "pct_change": 0.001,
    "volatility_5": 0.2,
    "volatility_20": 0.3,
    "gold_oil_ratio": 25.0,
    "bond_dxy_ratio": 0.04,
    "dist_sma20": 0.5,
    "lag_1": 35.5,
    "lag_7": 35.2,
    "day_of_week": 2,
    "month": 11,
    "is_holiday_th": 0
}

try:
    print(f"🚀 Sending request to {url}...")
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("✅ Success!")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"❌ Failed with status code: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Hint: Make sure the API is running (uvicorn src.app:app --port 10000)")
