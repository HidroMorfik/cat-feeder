import os
import subprocess
import time
os.chdir("/home/zesma/Desktop/project/")


def wifi_connected(host="8.8.8.8", port=53, timeout=3):
    try:
        subprocess.check_output(["ping", "-c", "1", host], timeout=timeout)
        return True
    except subprocess.CalledProcessError:
        pass
    return False

if __name__ == "__main__":
    # WiFi bağlantısı kontrol et
    while not wifi_connected():
        print("WiFi bağlantısı bekleniyor...")
        time.sleep(5)  # 5 saniye aralıklarla kontrol et

    print("WiFi bağlantısı sağlandı. Telegram bot başlatılıyor...")

    # telegram.py dosyasını çalıştır
    os.system("python3 telegram.py")