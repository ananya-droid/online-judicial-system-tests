import requests
url = "https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/"
try:
    response = requests.get(url, timeout=10)
    print(f"Website status: {response.status_code}")
    print("Website is accessible")
except Exception as e:
    print(f"Website access error: {e}")
