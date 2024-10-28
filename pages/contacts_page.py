from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_tensor_banner(self):
        tensor_banner = WebDriverWait(self.driver, 3).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR,"div.s-Grid-col.s-Grid-col--4.s-Grid-col--xm12 > div > a")))
        tensor_banner.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_region_text(self):
        region_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span"))
        )
        return region_element.text

    def get_partners(self):
        partners_elements = self.driver.find_elements(By.CSS_SELECTOR, ".controls-ListView__itemV-relative.controls-ListView__itemV.controls-ListView__item_default.controls-ListView__item_contentWrapper.js-controls-ListView__editingTarget.controls-ListView__itemV_cursor-pointer.controls-ListView__item_showActions.js-controls-ListView__measurableContainer.controls-ListView__item__unmarked_default.controls-ListView__item_highlightOnHover.controls-hover-background-default.controls-Tree__item")
        return [element.text for element in partners_elements if element.text.strip()] 

    def select_region(self):
      region_selector = WebDriverWait(self.driver, 2).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span"))
      )
      region_selector.click()
      WebDriverWait(self.driver, 3).until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, "#popup"))
      )
      new_region = WebDriverWait(self.driver, 2).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "div.sbis_ru-Region-Panel.sbis_ru-Region-Panel-l > div > ul > li:nth-child(43) > span"))
      )
      new_region.click()
      WebDriverWait(self.driver, 5).until(
          EC.url_contains("41-kamchatskij-kraj")
      )

    def get_current_url(self):
        print("Current URL:", self.driver.current_url)
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title
    