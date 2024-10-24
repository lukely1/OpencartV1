from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, TimeoutException


class DesktopPage:
    # dk_xpath = "//*[@id='content']/h2" #  Desktop page
    pc_page_xpath = "//*[@id='content']/h2" # select PC
    mac_page_xpath = "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[2]/a"  # select MAC
    all_page_xpath = "//*[@id='narbar-menu']/ul/li[1]/div/a"  # show all PC and MAC


    def __init__(self, driver):
        self.driver = driver

    def isPCPageExists(self):
        wait = WebDriverWait(self.driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        try:
            # return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.pc_page_xpath))).is_displayed()
        except:
            return False

    def isMacPageExists(self):
        wait = WebDriverWait(self.driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        try:
            # return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.all_page_xpath))).is_displayed()
        except:
            return False

    def ShowAllPageExists(self):
        wait = WebDriverWait(self.driver, 60, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        try:
            # return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.msg_myaccount_xpath))).is_displayed()
        except:
            return False