from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import tempfile
import os

CHATBOT_URL = "https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/"

def main():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    
    # Explicitly set ChromeDriver path and use Service
    service = Service(executable_path='/usr/bin/chromedriver')
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        print("Loading chatbot page...")
        driver.get(CHATBOT_URL)
        time.sleep(5)

        print("Page title:", driver.title)
        print("Current URL:", driver.current_url)
        
        # Save initial screenshot
        driver.save_screenshot("initial_page.png")
        print("Initial screenshot saved: initial_page.png")

        # Try to find any input element
        print("Looking for input elements...")
        input_elements = driver.find_elements(By.TAG_NAME, "textarea")
        if not input_elements:
            input_elements = driver.find_elements(By.TAG_NAME, "input")
            print("Found input elements:", len(input_elements))
        
        if input_elements:
            input_box = input_elements[0]
            query = "Hello, how are you?"
            print(f"Sending query: {query}")
            input_box.send_keys(query)
            
            # Try to submit
            try:
                input_box.submit()
            except:
                from selenium.webdriver.common.keys import Keys
                input_box.send_keys(Keys.RETURN)
            
            time.sleep(3)
            driver.save_screenshot("after_query.png")
            print("Screenshot after query saved: after_query.png")
            
            # Get any response text
            all_text = driver.find_element(By.TAG_NAME, "body").text
            print("Page text (first 500 chars):", all_text[:500])
        else:
            print("No input elements found")
            print("Available elements on page:")
            elements = driver.find_elements(By.CSS_SELECTOR, "*")
            print(f"Total elements: {len(elements)}")

    except Exception as e:
        print(f"Error during test: {e}")
        driver.save_screenshot("error_state.png")
        print("Error screenshot saved: error_state.png")
        
    finally:
        driver.quit()
        print("Test completed")

if __name__ == "__main__":
    main()
