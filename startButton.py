from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_google_button():
    result = "Google button works well"
    screenshot_path = None

    driver = webdriver.Chrome()

    try:
        driver.get("https://app.percogo.com")
    except Exception as e:
        driver.quit()
        return f"Page can't load correctly, Error!!!", None

    wait = WebDriverWait(driver, 10)

    # First Button Click
    try:
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.b-blue')))
        button.click()
    except Exception as e:
        screenshot_path = "first_button_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click First Button Error!!!"
        return result, screenshot_path

    # Google Register Button Click
    try:
        google_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="google"]')))
        google_register.click()
    except Exception as e:
        screenshot_path = "google_register_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click Google Register Button Error!!!"
        return result, screenshot_path

    # Check for Google Register Result
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


