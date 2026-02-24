import os

from requests import session
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context, scenario_name):

    ### MOBILE EMULATION ###
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver_path = ChromeDriverManager().install()
    service = ChromeService(driver_path)
    context.driver = webdriver.Chrome(service=service)
    ### BROWSER OPTIONS ###
    #context.driver = webdriver.Firefox()
    # context.driver = webdriver.Chrome()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #     options=options
    # )
    ### BROWSERSTACK ###
    bs_user = 'aaronwalden_mgQwhi'
    bs_key = '1Y9kdSFyKkyqgyBUhNQi'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = ChromeOptions()
    bstack_options = {
    "os" : "Windows",
    "osVersion" : "11",
    "browserVersion" : "latest",
    'browserName': 'Chrome',
    'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step:', step.name)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step.name)


def after_scenario(context, scenario):
    context.driver.quit()
