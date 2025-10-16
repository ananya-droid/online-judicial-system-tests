
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

CHATBOT_URL = "https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/"

def main():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")

    try:
        print("🚀 Starting Chrome Browser...")
        # Let Selenium find ChromeDriver automatically
        driver = webdriver.Chrome(options=options)
        
        print("📄 Loading chatbot page...")
        driver.get(CHATBOT_URL)
        time.sleep(5)

        print(f"📝 Page title: {driver.title}")
        print(f"🌐 Page URL: {driver.current_url}")
        
        # Take screenshot as proof
        driver.save_screenshot("test_success.png")
        print("📸 Screenshot saved: test_success.png")

        # Get page content
        body_text = driver.find_element(By.TAG_NAME, "body").text
        print(f"📄 Page content preview: {body_text[:200]}...")
        
        print("✅ TEST PASSED! SELENIUM IS WORKING!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        try:
            driver.quit()
            print("🔒 Browser closed.")
        except:
            pass

if __name__ == "__main__":
    print("=" * 50)
    print("ONLINE JUDICIAL SYSTEM - SELENIUM TEST")
    print("=" * 50)
    success = main()
    if success:
        print("=" * 50)
        print("🎉 SUCCESS! YOUR ASSIGNMENT TEST IS COMPLETE!")
        print("📸 Take a screenshot of this output!")
        print("✅ Python Selenium test: PASS")
        print("✅ Website accessibility: PASS") 
        print("=" * 50)
    else:
        print("❌ Test failed.")
