from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_signup_button():
    result = "Sign Up button works well"
    screenshot_path = None
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')


    try:
        driver.get("https://app.percogo.com")
    except Exception as e:
        driver.quit()
        return f"Page cant load correctly , Error!!! ", None

    wait = WebDriverWait(driver, 10)

    try:
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-event="nav-topmenu-signup"]')))
        button.click()
    except Exception as e:
        screenshot_path = "signup_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click SignUp Button Error!!!"
        return result, screenshot_path

    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.row.flex-center.register')))
    except Exception as e:
        screenshot_path = "signup_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Sign Up Button is working but wrong page is opening"
        return result, screenshot_path

    driver.quit()
    return result, None
