import time

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.DesktopsTabPage import DesktopPage
from pageObjects.basepage import ButtonPage

import os
import pytest


class Test_004_Destop:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # txt_email = "//input[@id='input-email']"

    @pytest.mark.sanity
    def test_desktop_products(self, setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        time.sleep(2)
        self.hp.clickMAC()
        self.ma = DesktopPage(self.driver)

        # after login Verify My Account page existing
        self.targetpage = self.ma.isPCPageExists()
        if self.targetpage == True:
            #self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
            #self.driver.close()
            assert False

        self.cart_btn = ButtonPage(self.driver)
        self.cart_btn.clickCartButton()

