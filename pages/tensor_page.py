from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def verify_block(self):
        block = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg .tensor_ru-Index__card-title")))
        return block.is_displayed() and "Сила в людях" in block.text

    def more_info(self):
        more_info_link = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,  "div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p:nth-child(4) > a")))
        more_info_link.click()

    def verify_page_opened(self):
        return "about" in self.driver.current_url


    def images_size(self):
        images = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR,  ".tensor_ru-About__block3-image")))
        first_img_size = images[0].size
        return all(img.size == first_img_size for img in images)
    
