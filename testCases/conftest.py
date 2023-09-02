import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print("ChromeDriverManager().install() :", ChromeDriverManager().install())

    return driver
