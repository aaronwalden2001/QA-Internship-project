from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChangePasswordPage(BasePage):

    NEW_PASSWORD = (By.XPATH, "//input[@name='Enter-new-password']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@placeholder='Repeat password']")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//a[@class='submit-button-2 w-button']")

    def verify_change_password_page_opened(self):
        assert "set-new-password" in self.get_url()

    def fill_password_fields(self, new, confirm):
        self.input_text(self.NEW_PASSWORD, new)
        self.input_text(self.CONFIRM_PASSWORD, confirm)

    def is_change_button_available(self):
        return self.is_element_present(self.CHANGE_PASSWORD_BUTTON)
