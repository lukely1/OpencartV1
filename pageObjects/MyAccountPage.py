from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, TimeoutException


class MyAccountPage:
    lnk_logout_xpath = "//aside[@id='column-right']//a[normalize-space()='Logout']"
    lnk_edit_account_info_linktext = "Edit your account information"
    lnk_change_password_linktext = "Change your password"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()

    def clickEditAccountInfo(self):
        #self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        #return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        edit = wait.until(ec.presence_of_element_located((By.LINK_TEXT, self.lnk_edit_account_info_linktext)))
        edit.click()

    def clickChangePassword(self):
        #self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        #return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
        edit = wait.until(ec.presence_of_element_located((By.LINK_TEXT, self.lnk_change_password_linktext)))
        edit.click()
