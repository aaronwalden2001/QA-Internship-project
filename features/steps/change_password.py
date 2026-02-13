from behave import given, when, then
from selenium import webdriver

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.change_password_page import ChangePasswordPage
from pages.settings_page import SettingsPage

@given('User opens the main page')
def open_main_page(context):
  context.login_page = LoginPage(context.driver)
  context.login_page.open()

@when('User logs in with valid credentials')
def login(context):
  context.login_page.login('awalcodes@gmail.com','Aaloves2001!')

@when('User clicks on the settings option')
def click_settings(context):
  context.settings_page = SettingsPage(context.driver)
  context.settings_page.open_settings()

@when('User clicks on Change password')
def click_change_password(context):
  context.settings_page.open_change_password()

@then('Change password page should open')
def step_verify_page(context):
  context.change_password_page = ChangePasswordPage(context.driver)
  context.change_password_page.verify_change_password_page_opened()

@then('User fills in new password fields')
def fill_fields(context):
  context.change_password_page.fill_password_fields('*****','*****')

@then('Change password button should be visible')
def verify_change_password_button_is_visible(context):
  context.change_password_page.is_change_button_available()