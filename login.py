from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_login_button():
    result = "Login button works well"
    screenshot_path = None

    
    driver = webdriver.Chrome()

    try:
        driver.get("https://app.percogo.com")
    except Exception as e:
        driver.quit()
        return f"Page cant load correctly , Error!!! ", None

    wait = WebDriverWait(driver, 5)

    try:
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-event="nav-topmenu-login')))
        button.click()
    except Exception as e:
        screenshot_path = "login_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click Login Button Error!!!"
        return result, screenshot_path

    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.create-your-hub-description')))
    except Exception as e:
        screenshot_path = "login_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Login Button is working but wrong page is opening"
        return result, screenshot_path

    driver.quit()
    return result, None
