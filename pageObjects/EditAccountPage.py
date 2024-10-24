from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, TimeoutException


class EditAccountPageInfo():
    lnk_account_info_xpath = "//*[@id='content']/h1"  # My Account Information
    fname_xpath = "//*[@id='input-firstname']"
    lname_xpath = "//*[@id='input-lastname']"
    email_xpath = "//*[@id='input-email']"

    def __init__(self, driver):
        self.driver = driver

    def isMyEditAccountPageExists(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        try:
            #return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.lnk_account_info_xpath))).is_displayed()
        except:
            return False

    def getFirstname(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        try:
            #return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.fname_xpath))).get_attribute('value')

        except:
            return False

    def getLastname(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        try:
            #return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.lname_xpath))).get_attribute('value')
        except:
            return False

    def getEmail(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        try:
            # return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.email_xpath))).get_attribute('value')
        except:
            return False
