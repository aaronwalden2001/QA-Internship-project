import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context, scenario):
    driver_path = ChromeDriverManager().install()
    service = ChromeService(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Chrome()
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
    bs_user = '******'
    bs_key = '*****'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = ChromeOptions()
    bstack_options = {
    "os" : "Windows",
    "osVersion" : "11",
    "browserVersion" : "latest",
    'browserName': 'Chrome',
    'sessionName': scenario,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

