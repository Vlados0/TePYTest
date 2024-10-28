import pytest
from selenium import webdriver
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.fixture(params=[(1920, 1080), (360, 740), (750, 1000)])
def driver(request):
    width, height = request.param
    download_folder = os.path.join(os.getcwd(), "Prog")

    logging.info(f"Запуск теста с разрешением экрана: {width}x{height}")

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(width, height)

    yield driver

    logging.info(f"Завершение теста с разрешением экрана: {width}x{height}")

    driver.quit()