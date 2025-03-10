import os
from datetime import datetime

import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.chrome.options import Options
# import undetected_chromedriver as uc
# from selenium_stealth import stealth
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        print("Launching Edge browser.........")
    # elif browser == 'firefox':
    #     options = webdriver.FirefoxOptions()
    #     options.add_argument("detach", True)
    #     driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #     print("Launching firefox browser.........")
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")  # by pass cloudfare processing
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_experimental_option('useAutomationExtension', False)
        # options.add_argument('--ignore-ssl-errors=yes')
        # options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("detach", True)
        options.add_argument('--log-level=1')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("ChromeDriverManager().install() :", ChromeDriverManager().install())
        print("Launching chrome browser.........")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Pavan'


# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "/reports/" + datetime.now().strftime(
   "%d-%m-%Y %H-%M-%S") + ".html"
