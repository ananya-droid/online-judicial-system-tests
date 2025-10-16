from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests

def basic_functional_test():
    print("=" * 60)
    print("JUDICIAL SYSTEM - BASIC FUNCTIONAL TEST")
    print("=" * 60)
    
    # Test 1: Website Accessibility
    print("1. Testing website accessibility...")
    try:
        response = requests.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/", timeout=10)
        if response.status_code == 200:
            print("   ✓ Website is accessible (HTTP 200)")
            accessibility = "PASS"
        else:
            print(f"   ⚠ Website returned status: {response.status_code}")
            accessibility = "WARNING"
    except Exception as e:
        print(f"   ✗ Website access failed: {e}")
        accessibility = "FAIL"
        return
    
    # Test 2: Selenium Page Loading
    print("2. Testing page loading with Selenium...")
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        start_time = time.time()
        driver.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/")
        load_time = time.time() - start_time
        
        print(f"   ✓ Page loaded in {load_time:.2f} seconds")
        print(f"   ✓ Page title: {driver.title}")
        print(f"   ✓ Current URL: {driver.current_url}")
        
        # Test 3: Basic Content Verification
        print("3. Testing basic content...")
        body_text = driver.find_element(By.TAG_NAME, "body").text
        
        if "Streamlit" in driver.title:
            print("   ✓ Streamlit framework detected")
            framework = "PASS"
        else:
            print("   ⚠ Unexpected page title")
            framework = "WARNING"
        
        if len(body_text) > 50:
            print("   ✓ Page has substantial content")
            content = "PASS"
        else:
            print("   ⚠ Limited page content")
            content = "WARNING"
        
        # Save evidence
        driver.save_screenshot("basic_functional_test.png")
        print("   ✓ Screenshot saved: basic_functional_test.png")
        
        print("=" * 60)
        print("BASIC FUNCTIONAL TEST SUMMARY:")
        print(f"Website Accessibility: {accessibility}")
        print(f"Framework Detection: {framework}")
        print(f"Content Verification: {content}")
        print("=" * 60)
        
    except Exception as e:
        print(f"   ✗ Selenium test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    basic_functional_test()
