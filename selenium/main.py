from selenium import webdriver
import time

chrome_path = '/usr/bin/chromium-browser'  # Шлях до бінарного файлу Chromium
options = webdriver.ChromeOptions()
options.binary_location = chrome_path

# try:
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com.ua/")
driver.maximize_window()
    # Затримка на 60 секунд
time.sleep(1000)

# except Exception as e:
#     print(f"An exception occurred: {e}")

# finally:
#     # Закриваємо вікно браузера, якщо воно вдалося відкрити
#     if 'driver' in locals():
#         driver.quit()
#         driver.get("https://www.python.org")

#         time.sleep(50)

#         ############### BUGGGGGG
        
