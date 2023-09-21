from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()

def buton_kontrol(driver, data_event_value, beklenen_element):
    try:
        wait = WebDriverWait(driver, 20)
        buton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[data-event='{data_event_value}']")))
        buton.click()
        
       
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, beklenen_element)))
        
        print(f"'{data_event_value}' data-event değerine sahip buton çalışıyor ve doğru sayfa açıldı.")
    except NoSuchElementException:
        print(f"'{data_event_value}' data-event değerine sahip buton bulunamadı veya tıklanamadı.")
    except Exception as e:
        print(f"'{data_event_value}' data-event değerine sahip buton çalışıyor ama yanlış sayfa açıldı. Hata: {e}")


driver_path = '/opt/homebrew/bin/chromedriver'
s = Service(driver_path)
driver = webdriver.Chrome(service=s, options=chrome_options)


driver.get('https://app.percogo.com')


buton_kontrol(driver, 'nav-topmenu-pricing', 'label.form-switch')
buton_kontrol(driver, 'nav-topmenu-login', 'div.create-your-hub-description')


driver.quit()
