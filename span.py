from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://app.percogo.com")
except Exception as e:
    print(f"Sayfa doğru açılamadı. Hata: {e}")
    driver.quit()
    exit()

def signup_butonunu_tikla(driver):
    try:
       
        wait = WebDriverWait(driver, 10)  
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-event="nav-topmenu-signup"]')))
        button.click()
    except Exception as e:
        print(f"'Sign Up' butonuna tıklanamadı. Hata: {e}")
        driver.quit()
        exit()

    try:
        
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.row.flex-center.register')))
        print("Butona başarıyla tıklandı ve sign up(kayıt ol) sayfası çalışıyor.")
    except Exception as e:
        print(f"Belirli div elementi görünür hale gelmedi. Hata: {e}")

signup_butonunu_tikla(driver)

# Tarayıcıyı kapat
driver.quit()
