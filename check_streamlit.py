from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
# Remove headless to see what's happening
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

try:
    print("Loading page (visible mode)...")
    driver.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/")
    
    for i in range(1, 11):
        print(f"Waiting... {i}0 seconds")
        time.sleep(10)
        
        # Check for common Streamlit elements
        selectors_to_check = [
            "[data-testid='stAppViewContainer']",
            ".stApp",
            "[class*='stChat']",
            "[class*='streamlit']",
            "div[role*='main']"
        ]
        
        print(f"=== Check at {i}0 seconds ===")
        for selector in selectors_to_check:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    print(f"  ✓ Found: {selector} ({len(elements)} elements)")
            except:
                pass
        
        # Check for loading indicators
        loading_indicators = [
            "//*[contains(text(), 'Loading')]",
            "//*[contains(text(), 'Please wait')]",
            "//*[contains(text(), 'Initializing')]"
        ]
        
        for indicator in loading_indicators:
            try:
                elements = driver.find_elements(By.XPATH, indicator)
                if elements:
                    print(f"  ⚠ Loading: {elements[0].text[:50]}")
            except:
                pass
        
        if i >= 3:  # After 30 seconds, take screenshot
            driver.save_screenshot(f"streamlit_check_{i}0s.png")
            print(f"  Screenshot saved: streamlit_check_{i}0s.png")
    
finally:
    driver.quit()
    print("Debug completed")
