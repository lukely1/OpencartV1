from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.EditAccountPage import EditAccountPageInfo
from pageObjects.ChangeYourPassWordPage import PasswordChange
import os
import pytest
import time
from selenium.webdriver.common.by import By


class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    # txt_email = "//input[@id='input-email']"

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickShopping()
        self.hp.clickMyAccountLogin()

        self.ma = MyAccountPage(self.driver)
        # self.hp.clickDemo()
        #wait.until(ec.title_is('OpenCart - Account Login'))
        # time.sleep(10)

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        # after login Verify My Account page existing
        self.targetpage = self.lp.isMyAccountPageExists()
        if self.targetpage == True:
            #self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
            #self.driver.close()
            assert False

        self.ma.clickEditAccountInfo()  #click on edit account info
        # Verify My Account Information page existing
        self.ed = EditAccountPageInfo(self.driver)

        self.targetpage = self.ed.isMyEditAccountPageExists()
        if self.targetpage == True:
            # self.driver.close()
            self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
            # self.driver.close()
            assert False

        # verify fname, lname, email registered with account
        expect_fn = "Luke"
        expect_ln = "Ly"
        expect_email = "lukely71@gmail.com"

        act_fn = self.ed.getFirstname()
        assert act_fn == expect_fn
        act_ln = self.ed.getLastname()
        assert act_ln == expect_ln
        act_email = self.ed.getEmail()
        assert act_email == expect_email


        # # go back home login page
        # self.hp.clickButtonBack()
        # self.ma.clickChangePassword()  # click on edit account info
        #
        # # navigate to change password page
        # self.pc = PasswordChange(self.driver)
        #
        # self.targetpage = self.pc.isPasswordChangePageExists()
        # if self.targetpage == True:
        #     # self.driver.close()
        #     self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
        #     assert True
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
        #     # self.driver.close()
        #     assert False
        #
        #
        # # self.driver.close()
        # self.logger.info("******* End of test_002_login **********")


    # @pytest.mark.sanity
    # def test_edit_account_information(self, setup):
    #     self.logger.info("******* Starting test_002_login **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #
    #     self.hp = HomePage(self.driver)
    #     self.hp.clickShopping()
    #     self.hp.clickMyAccountLogin()
    #
    #     self.ma = MyAccountPage(self.driver)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setEmail(self.user)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLoginButton()
    #
    #     self.ma.editAccountInfo()  # click on edit account info
    #
    #     self.ed = EditAccountPageInfo(self.driver)
    #
    #     self.targetpage = self.ed.isMyEditAccountPageExists()
    #     if self.targetpage == True:
    #         # self.driver.close()
    #         self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
    #         assert True
    #     else:
    #         self.driver.save_screenshot(os.path.abspath(os.curdir) + '//screenshots//' + 'test_login.png')
    #         # self.driver.close()
    #         assert False
    #
    #     # self.driver.close()
    #     self.logger.info("******* End of test_002_login **********")
