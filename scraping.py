from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# URL toko Tokopedia yang akan di-scrape
url = 'https://www.tokopedia.com/locknlock-id/locknlock-exclusive-macaron-water-bottle-680ml-hap693-blue/review'

# Konfigurasi Selenium
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)

# List untuk menyimpan data ulasan
data = []

# Loop untuk mengambil data dari beberapa halaman
for i in range(50):  # Ambil ulasan dari 50 halaman pertama
    # Tunggu sampai ulasan muncul
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article.css-15m2bcr"))
    )

    # Ambil source page setelah memastikan elemen sudah muncul
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.findAll('article', attrs={'class': 'css-15m2bcr'})

    # Loop untuk mengambil ulasan
    for container in containers:
        try:
            review = container.find('span', attrs={'data-testid': 'lblItemUlasan'}).text
            data.append(review)  # Perbaikan penulisan append
        except AttributeError:
            continue

    time.sleep(2)  # Tunggu agar halaman baru termuat

    # Coba klik tombol "Laman berikutnya" jika ada
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']"))
        )
        driver.execute_script("arguments[0].click();", next_button)  # Paksa klik dengan JavaScript
        time.sleep(3)  # Tunggu agar halaman berikutnya benar-benar dimuat
    except Exception as e:
        print(f"Tidak bisa berpindah halaman: {e}")
        break  # Keluar dari loop jika tombol tidak bisa diklik

# Tutup browser setelah scraping selesai
driver.quit()

# Simpan data ke CSV
df = pd.DataFrame(data, columns=["Ulasan"])
df.to_csv("Tokopedia24.csv", index=False)

print("Scraping selesai. Data tersimpan dalam Tokopedia.csv")
