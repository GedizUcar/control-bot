import requests
import socket
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_site():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    screenshot_path = None

    def siteControl(url):
        hata_kelimeleri = ["Hata", "Error", "Failed", "Unavailable"]

        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return False, f"HTTP Durum Kodu: {response.status_code}"

            for kelime in hata_kelimeleri:
                if kelime in response.text:
                    return False, "Contain Error Word."

            return True, "WebSite is working well."
        except requests.RequestException as e:
            return False, f"RequestException: {e}"

    def portControl(host, port_list):
        for port in port_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
        return False

    siteSituation, siteMessage = siteControl("https://app.percogo.com")
    portSituation = portControl("app.percogo.com", [80, 443])

    if not siteSituation:
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)  # Ekran görüntüsü alın

    driver.quit()

    if screenshot_path:
        return f"WebSite is not responding or contains error Message! ({siteMessage})", screenshot_path
    return "WebSite is working well", None
