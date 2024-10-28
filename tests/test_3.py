import logging
import os
from pages.main_page import MainPage
from pages.download_page import DownloadPage

logging.basicConfig(level=logging.INFO)

def test_download_app(driver):
    logging.info("Указание пути для загрузки файла")
    download_folder = os.path.join(os.getcwd(), "Prog")
    os.makedirs(download_folder, exist_ok=True)
    file_path = os.path.join(download_folder, "app_name.exe")

    main_page = MainPage(driver)
    download_page = DownloadPage(driver)

    logging.info("Открытие главной страницы и переход на страницу загрузки")
    main_page.open()
    main_page.go_download_page()

    logging.info("Начало загрузки приложения")
    download_page.download_app()

    logging.info("Проверка, что файл скачан и имеет нужный размер")
    assert download_page.app_downloaded(download_folder), (
        "Приложение не было скачано или его размер не соответствует (ожидалось 11.48 МБ)."
    )
    download_page.remove_downloaded_file(download_folder)