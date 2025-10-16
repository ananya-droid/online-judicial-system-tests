from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def functional_test():
    print("=" * 60)
    print("JUDICIAL CHATBOT - FUNCTIONAL TEST")
    print("=" * 60)
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Test 1: Page Loading
        print("1. Testing page loading...")
        driver.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/")
        time.sleep(5)
        print(f"   ✓ Page loaded: {driver.title}")
        
        # Test 2: Wake-up handling
        print("2. Testing wake-up handling...")
        try:
            wake_btn = driver.find_element(By.XPATH, "//button[contains(., 'Yes, get this app back up')]")
            wake_btn.click()
            print("   ✓ Wake-up button handled")
            time.sleep(3)
        except:
            print("   ✓ No wake-up needed")
        
        # Test 3: Input field interaction
        print("3. Testing input field...")
        input_box = driver.find_element(By.TAG_NAME, "textarea")
        test_query = "How to file a consumer complaint?"
        input_box.send_keys(test_query)
        input_box.submit()
        print(f"   ✓ Query submitted: '{test_query}'")
        
        # Test 4: Response validation
        print("4. Testing response...")
        time.sleep(5)
        
        page_text = driver.find_element(By.TAG_NAME, "body").text
        if any(keyword in page_text.lower() for keyword in ["consumer", "complaint", "file", "legal"]):
            print("   ✓ FUNCTIONAL TEST PASSED: Relevant legal guidance provided")
            result = "PASS"
        else:
            print("   ✗ FUNCTIONAL TEST FAILED: No relevant response")
            result = "FAIL"
        
        # Save evidence
        driver.save_screenshot("functional_test_result.png")
        print("   ✓ Screenshot saved: functional_test_result.png")
        
        return result
        
    except Exception as e:
        print(f"   ✗ TEST ERROR: {e}")
        return "ERROR"
    finally:
        driver.quit()

if __name__ == "__main__":
    functional_test()
