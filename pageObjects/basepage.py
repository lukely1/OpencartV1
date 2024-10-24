import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, TimeoutException
from selenium.webdriver import ActionChains


class ButtonPage:
    cart_xpath = "//*[@id='product-list']/div/div/div[2]/form/div/button[1]" # //*[@id="product-list"]/div/div/div[2]/form/div/button[1]
    wish_list_xpath = "//*[@id='product-list']/div/div/div[2]/form/div/button[2]" # //*[@id="product-list"]/div/div/div[2]/form/div/button[2]
    compare_product_xpath = "//*[@id='product-list']/div/div/div[2]/form/div/button[3]"

    def __init__(self, driver):
        self.driver = driver

    def clickCartButton(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])

        add_cart = wait.until(ec.visibility_of_element_located((By.XPATH, self.cart_xpath)))
        actionChains = ActionChains(self.driver)
        time.sleep(2)
        actionChains.move_to_element(add_cart).click().perform()


    def clickWishlistButton(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        edit = wait.until(ec.presence_of_element_located((By.XPATH, self.wish_list_xpath)))
        edit.click()

    def clickCompareProductButton(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException,
                                                                                    Exception])
        edit = wait.until(ec.presence_of_element_located((By.XPATH, self.compare_product_xpath)))
        edit.click()