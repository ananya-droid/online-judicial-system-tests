import subprocess
import requests

# Test if the website is accessible
url = "https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/"
try:
    response = requests.get(url, timeout=10)
    print(f"Website status: {response.status_code}")
    print("Website is accessible")
except Exception as e:
    print(f"Website access error: {e}")

# Test ChromeDriver
try:
    result = subprocess.run(['chromedriver', '--version'], capture_output=True, text=True)
    print(f"ChromeDriver: {result.stdout}")
except Exception as e:
    print(f"ChromeDriver error: {e}")

# Test Chromium
try:
    result = subprocess.run(['chromium-browser', '--version'], capture_output=True, text=True)
    print(f"Chromium: {result.stdout}")
except Exception as e:
    print(f"Chromium error: {e}")
