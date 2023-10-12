from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import time 
import threading
from queue import Queue
def start_chrome_with_permissions():
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    
    driver = webdriver.Chrome(options=chrome_options,executable_path='/opt/homebrew/bin/chromedriver')
    return driver

def selenium_task(q,function,*args,**kwargs):
    result =function(*args,**kwargs)
    q.put(result)

def selenium_test_demo_button():
    result = "Demo , mic and camera buttons are works well"
    screenshot_path = None

    driver = start_chrome_with_permissions()

    try:
        driver.get("https://app.percogo.com")
        
    except Exception as e:
        driver.quit()
        return f"Page can't load correctly, Error!!!", None

    wait = WebDriverWait(driver, 10)

   
    try:
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.b-purple')))
        button.click()
    except Exception as e:
        screenshot_path = "first_button_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click First Button Error!!!"
        return result, screenshot_path

    
    try:
        new_window_handle = [handle for handle in driver.window_handles if handle != driver.current_window_handle][0]
        driver.switch_to.window(new_window_handle)
    except Exception as e:
        screenshot_path = "switch_window_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot switch to the new window Error!!!"
        return result, screenshot_path

   
    try:
        mic_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="mic icon"]')))
        mic_button.click()
        camera_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="camera icon"]')))
        camera_button.click()
    except Exception as e:
        screenshot_path = "mic_camera_button_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click Mic or Camera Button Error!!!"
        return result, screenshot_path

    
    try:
        join_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.perculus-button-container')))
        join_button.click()

        # Click the introjs-skipbutton
        try:
            skip_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.introjs-skipbutton')))
            skip_button.click()

            # Check for Leave button
            try:
                leave_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.btn-primary.leave')))
            except Exception as e:
                screenshot_path = "leave_button_screenshot.png"
                driver.save_screenshot(screenshot_path)
                driver.quit()
                result = f"Leave button not found Error!!!"
                return result, screenshot_path

        except Exception as e:
            screenshot_path = "skip_button_screenshot.png"
            driver.save_screenshot(screenshot_path)
            driver.quit()
            result = f"Cannot click Skip Button Error!!!"
            return result, screenshot_path

    except Exception as e:
        screenshot_path = "final_button_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        result = f"Cannot click Final Button Error!!!"
        return result, screenshot_path


    driver.quit()
    return result, None

async def test_demo_button():
    q = Queue()
    t = threading.Thread(target=selenium_task, args=(q, selenium_test_demo_button))
    t.start()
    t.join()
    return q.get()





