from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, TimeoutException
import time


class LoginPage:
    # txt_email_xpath = "//input[@id='input-email']"
    txt_email_xpath = "//input[@name='email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//*[@id='form-login']/div[3]/button"  # //input[@value='Login'] //*[@id="form-login"]/div[3]/button
    msg_myaccount_xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        # #self.driver.implicitly_wait(10)
        #
        # wait = WebDriverWait(self.driver, 10)
        # # Store the ID of the original window
        # original_window = self.driver.current_window_handle
        # print(original_window)
        # # Check we don't have other windows open already
        # assert len(self.driver.window_handles) == 1
        #
        # # wait.until(ec.number_of_windows_to_be(2))
        # # Loop through until we find a new window handle
        # for window_handle in self.driver.window_handles:
        #     if window_handle == original_window:
        #         self.driver.switch_to.window(window_handle)
        #         print(window_handle)
        #         time.sleep(4)
        #         break
        # # self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)
        try:
            emailElement = WebDriverWait(self.driver, 25).until(ec.presence_of_element_located(
                (By.XPATH, self.txt_email_xpath)))
            emailElement.send_keys(email)

        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            print("Page loaded")

        # while True:
        #     try:
        #         emailElement = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
        #             (By.XPATH, self.txt_email_xpath)))
        #         emailElement.send_keys(email)
        #         break
        #     except TimeoutException:
        #         self.driver.refresh()
        #         continue
        # emailElement = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(
        #     (By.XPATH, self.txt_email_xpath)))
        # emailElement.send_keys(email)
        # self.driver.refresh()
        # try:
        #     # mywait = WebDriverWait(self.driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
        #     #                                                                               ElementNotVisibleException,
        #     #                                                                               ElementNotSelectableException,
        #     #                                                                               Exception])
        #     # emailElement = mywait.until(ec.presence_of_element_located((By.XPATH, self.txt_email_xpath)))
        #     # emailElement.send_keys(email)
        #
        #     emailElement = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
        #         (By.XPATH, self.txt_email_xpath)))
        #     emailElement.send_keys(email)
        #
        # except TimeoutException:
        #     print("Timed out waiting for page to load")
        # finally:
        #     print("Page loaded")

    def setPassword(self, pwd):
        try:
            # mywait = WebDriverWait(self.driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
            #                                                                               ElementNotVisibleException,
            #                                                                               ElementNotSelectableException,
            #                                                                               Exception])
            # pwdElement = mywait.until(ec.presence_of_element_located((By.XPATH, self.txt_password_xpath)))
            # pwdElement.send_keys(pwd)

            pwdElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
                (By.XPATH, self.txt_password_xpath)))
            pwdElement.send_keys(pwd)

        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            print("Page loaded")

    def clickLoginButton(self):
        mywait = WebDriverWait(self.driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                      ElementNotVisibleException,
                                                                                      ElementNotSelectableException,
                                                                                      Exception])
        btnloginElement = mywait.until(ec.presence_of_element_located((By.XPATH, self.btn_login_xpath)))
        btnloginElement.click()

    def isMyAccountPageExists(self):
        wait = WebDriverWait(self.driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                      ElementNotVisibleException,
                                                                                      ElementNotSelectableException,
                                                                                      Exception])
        try:
            #return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.msg_myaccount_xpath))).is_displayed()
        except:
            return False



