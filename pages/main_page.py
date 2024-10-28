from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://sbis.ru/")

    def go_contacts_page(self):
        screen_width = self.driver.execute_script("return window.innerWidth;")
        if screen_width < 617:
            mobile_pop = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(4) > h4 > svg")))
            mobile_pop.click()
        contacts_link = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(4) > ul > li:nth-child(1) > a")))
        contacts_link.click()

    def go_download_page(self):
        screen_width = self.driver.execute_script("return window.innerWidth;")
        if screen_width < 617:
            mobile_pop2 = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,"div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(3) > h4 > svg")))
            mobile_pop2.click()
        download_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,"div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(3) > ul > li:nth-child(8) > a")))
        download_button.click()

