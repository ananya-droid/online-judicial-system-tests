
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests

def performance_test():
    print("=" * 60)
    print("JUDICIAL CHATBOT - PERFORMANCE TEST")
    print("=" * 60)
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Test 1: Page Load Time
        print("1. Testing page load performance...")
        start_time = time.time()
        driver.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/")
        load_time = time.time() - start_time
        print(f"   ✓ Page load time: {load_time:.2f} seconds")
        
        if load_time < 8:
            print("   ✓ PERFORMANCE PASSED: Fast loading (< 8 seconds)")
            load_result = "PASS"
        else:
            print("   ⚠ PERFORMANCE WARNING: Slow loading (> 8 seconds)")
            load_result = "WARNING"
        
        time.sleep(3)
        
        # Test 2: UI Responsiveness
        print("2. Testing UI responsiveness...")
        start_time = time.time()
        input_box = driver.find_element(By.TAG_NAME, "textarea")
        responsiveness_time = time.time() - start_time
        print(f"   ✓ UI response time: {responsiveness_time:.2f} seconds")
        
        if responsiveness_time < 2:
            print("   ✓ RESPONSIVENESS PASSED: Quick UI response (< 2 seconds)")
            response_result = "PASS"
        else:
            print("   ⚠ RESPONSIVENESS WARNING: Slow UI response")
            response_result = "WARNING"
        
        # Test 3: Website Availability
        print("3. Testing website availability...")
        try:
            response = requests.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/", timeout=10)
            if response.status_code == 200:
                print("   ✓ AVAILABILITY PASSED: Website is accessible")
                availability_result = "PASS"
            else:
                print(f"   ⚠ AVAILABILITY WARNING: Status code {response.status_code}")
                availability_result = "WARNING"
        except Exception as e:
            print(f"   ✗ AVAILABILITY FAILED: {e}")
            availability_result = "FAIL"
        
        # Save evidence
        driver.save_screenshot("performance_test_result.png")
        print("   ✓ Screenshot saved: performance_test_result.png")
        
        print("=" * 60)
        print("PERFORMANCE TEST SUMMARY:")
        print(f"Page Load: {load_result}")
        print(f"UI Responsiveness: {response_result}")
        print(f"Availability: {availability_result}")
        print("=" * 60)
        
    except Exception as e:
        print(f"   ✗ PERFORMANCE TEST ERROR: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    performance_test()
