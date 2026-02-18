import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context):
    """
    Initializes browser based on environment variables:
    BROWSER=chrome or firefox
    HEADLESS=true or false
    """

    browser = os.getenv("BROWSER", "firefox").lower()
    headless = os.getenv("HEADLESS", "true").lower() == "true"

    if browser == "chrome":
        chrome_options = ChromeOptions()

        if headless:
            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()

        if headless:
            firefox_options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=firefox_options)

    else:
        raise Exception(f"Browser '{browser}' is not supported.")

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step:', step.name)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step.name)


def after_scenario(context, scenario):
    context.driver.quit()
