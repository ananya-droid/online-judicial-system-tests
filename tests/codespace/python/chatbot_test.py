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

    driver = webdriver.Chrome(options=options)
    driver.get(CHATBOT_URL)
    time.sleep(5)

    try:
        wake_btn = driver.find_element(By.XPATH, "//button[contains(., 'Yes, get this app back up')]")
        wake_btn.click()
        print("Clicked wake-up button.")
        time.sleep(3)
    except Exception:
        pass

    try:
        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        for b in all_buttons:
            txt = b.get_attribute("title") or b.text or ""
            if "chat" in txt.lower() or "assistant" in txt.lower():
                b.click()
                print("Clicked chatbot button:", txt)
                time.sleep(2)
                break
    except Exception:
        pass

    try:
        input_box = driver.find_element(By.TAG_NAME, "textarea")
    except Exception:
        print("Could not find textarea input. Trying other selectors...")
        try:
            input_box = driver.find_element(By.CSS_SELECTOR, "input")
        except Exception:
            print("No input element found. Exiting.")
            driver.quit()
            return

    query = "How do I file a consumer complaint?"
    input_box.send_keys(query)
    try:
        input_box.submit()
    except Exception:
        driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', {'key':'Enter'}));", input_box)

    start = time.time()
    time.sleep(4)

    response_text = ""
    try:
        response_text = driver.find_element(By.CLASS_NAME, "stMarkdown").text
    except Exception:
        try:
            response_text = driver.find_element(By.CSS_SELECTOR, "div").text
        except Exception:
            response_text = "Response not found."

    end = time.time()
    print("Query sent:", query)
    print("Chatbot response (snippet):", response_text[:400])
    print("Response time (s):", round(end - start, 2))

    driver.quit()

if __name__ == "__main__":
    main()
