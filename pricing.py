from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_pricing_button():
    result = "Pricing button works well"
    screenshot_path = None

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    try:
        driver.get("https://app.percogo.com")
    except Exception as e:
        driver.quit()
        return f"Page cant load correctly , Error!!! ", None

    wait = WebDriverWait(driver, 5)

    try:
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-event="nav-topmenu-pricing"]')))
        button.click()
    except Exception as e:
        screenshot_path = "pricing_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click Pricing Button Error!!!"
        return result, screenshot_path

    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label.form-switch')))
    except Exception as e:
        screenshot_path = "signup_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Pricing Button is working but wrong page is opening"
        return result, screenshot_path

    driver.quit()
    return result, None
