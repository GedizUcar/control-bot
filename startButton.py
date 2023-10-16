from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_google_button():
    result = "Google button works well"
    screenshot_path = None
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver')

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
        google_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="google"]')))
        google_register.click()
    except Exception as e:
        screenshot_path = "google_register_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click Google Register Button Error!!!"
        return result, screenshot_path

    
    try:
        expected_div_selector = 'div[jsname="f2d3ae"][role="presentation"]'
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, expected_div_selector)))
    except Exception as e:
        screenshot_path = "google_result_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Google Register Button is working but wrong page is opening"
        return result, screenshot_path

    driver.quit()
    return result, None


