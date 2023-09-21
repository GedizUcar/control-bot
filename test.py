import requests
import time
import socket

def site_kontrol(url):
    hata_kelimeleri = ["Hata", "Error", "Failed", "Unavailable"]

    try:
        response = requests.get(url, timeout=10)
        
        # HTTP Durum Kodu Kontrolü
        if response.status_code != 200:
            return False, f"HTTP Durum Kodu: {response.status_code}"
        
        for kelime in hata_kelimeleri:
            if kelime in response.text:
                return False, "Hata kelimesi içeriyor"
        
        return True, "Web sitesi çalışıyor"
    except requests.RequestException as e:
        return False, f"RequestException: {e}"

def port_tarama(host, port_list):
    for port in port_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
    return False

while True:
    site_durumu, site_mesaj = site_kontrol("https://app.percogo.com")
    port_durumu = port_tarama("app.percogo.com", [80, 443])
    
    if site_durumu and port_durumu:
        print("Web sitesi şu anda çalışıyor.")
    else:
        if not site_durumu:
            print(f"Web sitesi yanıt vermiyor veya hata mesajı içeriyor! ({site_mesaj})")
        if not port_durumu:
            print("Web sitesinin portları kapalı!")
    
    time.sleep(1800)
