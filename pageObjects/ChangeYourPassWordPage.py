from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, TimeoutException


class PasswordChange():
    pwd_change_xpath = "//*[@id='content']/h1" # Change Password


    def __init__(self, driver):
        self.driver = driver

    def isPasswordChangePageExists(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                      ElementNotVisibleException,
                                                                                      ElementNotSelectableException,
                                                                                      Exception])
        try:
            #return self.driver.find_element(By.XPATH, self.msg_myaccount_xpath).is_displayed()
            return wait.until(ec.presence_of_element_located((By.XPATH, self.pwd_change_xpath))).is_displayed()
        except:
            return False

