from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://legal-advisor-ai-kmmtuczo7ltm2rihj5actd.streamlit.app/")
    time.sleep(5)
    
    print("PAGE TITLE:", driver.title)
    print("CURRENT URL:", driver.current_url)
    
    # Take screenshot to see what's there
    driver.save_screenshot("debug_page.png")
    print("Screenshot saved: debug_page.png")
    
    # Find all interactive elements
    print("\n=== ALL INPUT ELEMENTS ===")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, inp in enumerate(inputs):
        print(f"Input {i}: type='{inp.get_attribute('type')}', placeholder='{inp.get_attribute('placeholder')}'")
    
    print("\n=== ALL BUTTONS ===")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for i, btn in enumerate(buttons):
        print(f"Button {i}: text='{btn.text}'")
    
    print("\n=== ALL TEXTAREAS ===")
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    for i, ta in enumerate(textareas):
        print(f"Textarea {i}: placeholder='{ta.get_attribute('placeholder')}'")
    
    print("\n=== ALL DIVS WITH INTERACTIVE CLASSES ===")
    divs = driver.find_elements(By.CSS_SELECTOR, "div[class*='input'], div[class*='text'], div[class*='chat']")
    for i, div in enumerate(divs[:10]):  # First 10 only
        print(f"Div {i}: class='{div.get_attribute('class')}', text='{div.text[:50]}'")
        
finally:
    driver.quit()
