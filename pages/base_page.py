from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, element):
        self.wait.until(EC.element_to_be_clickable(element)).click()

    def input_text(self, element, text):
        self.wait.until(EC.element_to_be_clickable(element)).send_keys(text)

    def is_element_present(self, element):
        return self.wait.until(EC.presence_of_element_located(element))

    def get_url(self):
        return self.driver.current_url