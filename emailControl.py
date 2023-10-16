from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import threading
from queue import Queue


def selenium_task(q, function, *args, **kwargs):
    result = function(*args, **kwargs)
    q.put(result)
def selenium_test_email():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    result = "Email button works well"
    screenshot_path = None

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    try:
        driver.get("https://app.percogo.com")
    except Exception as e:
        driver.quit()
        return f"Page can't load correctly, Error!!!", None

    wait = WebDriverWait(driver, 10)

    
    try:
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.b-blue')))
        button.click()
    except Exception as e:
        screenshot_path = "first_button_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click First Button Error!!!"
        return result, screenshot_path

    
    try:
        email_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-toggle="collapse"]')))
        email_register.click()
    except Exception as e:
        screenshot_path = "email_register_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click Email Register Button Error!!!"
        return result, screenshot_path

   
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.jsx-544dc49cb436bf91')))
    except Exception as e:
        screenshot_path = "email_result_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Email Register Button is working but wrong page is opening"
        return result, screenshot_path

    driver.quit()
    return result, None

async def test_email():
    q = Queue()
    t = threading.Thread(target=selenium_task, args=(q, selenium_test_email))
    t.start()
    t.join()
    return q.get()
