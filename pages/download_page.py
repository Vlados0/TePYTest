from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import os

class DownloadPage:
    def __init__(self, driver):
        self.driver = driver

    def download_app(self):
        print("Current URL:", self.driver.current_url)
        try:
            download_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".sbis_ru-DownloadNew-flex__child--width-1 > div > a"))
            )
            download_link.click()
            logging.info("Скачивание приложения началось.")
            time.sleep(10)
        except Exception as e:
            logging.error(f"Ошибка при попытке скачать приложение: {e}")

    def app_downloaded(self, download_folder):
        file_path = os.path.join(download_folder, "sbisplugin-setup-web.exe")
        file_exists = os.path.isfile(file_path)
        
        if file_exists:
            file_size = os.path.getsize(file_path) / (1024 * 1024)
            logging.info(f"Файл существует: {file_exists}, Размер файла: {file_size:.2f} МБ")
            print(file_size)
            return abs(file_size - 11.48) < 0.01
        else:
            logging.info("Файл не найден в папке загрузки.")
            return False

    def remove_downloaded_file(self, download_folder):
            file_path = os.path.join(download_folder, "sbisplugin-setup-web.exe")
            
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    logging.info("Файл был успешно удален.")
                except Exception as e:
                    logging.error(f"Ошибка при удалении файла: {e}")
            else:
                logging.info("Файл для удаления не найден.")