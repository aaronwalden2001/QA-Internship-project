from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SettingsPage(BasePage):

    SETTINGS_BUTTON = (By.XPATH, "//a[contains(@href,'settings')]")
    CHANGE_PASSWORD_OPTION = (By.XPATH, "//a[@href='/set-new-password']")

    def open_settings(self):
        self.click_element(self.SETTINGS_BUTTON)

    def open_change_password(self):
        self.click_element(self.CHANGE_PASSWORD_OPTION)
