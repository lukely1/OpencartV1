from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
import time


class HomePage:
    #lnk_myaccount_xpath = "//*[@id='top']/div[2]/div[2]/ul/li[2]/div/a/span" #//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span
    #lnk_myaccount_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/a/span" # //*[@id="top"]/div/div[2]/ul/li[2]/div/a,
    lnk_login_xpath = "//*[@id='navbar-collapse-header']/div/a[1]"  # "Login" //*[@id="navbar-collapse-header"]/div/a[1]
    lnk_demo_linktext = "Demo"
    lnk_feature_linktext = "Features"

    lnk_shopping = "//*[@id='top']/div/div[2]/ul/li[4]/a/span"
    lnk_wishlist = "//*[@id='wishlist-total']/span"

    dropdown_myaccount_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/a/i[1]"  # My Account dropdown on home page
    myacct_register_linktxt = "Register"
    myacct_login_linktxt = "Login"
    btn_back_xpath = "//*[@id='form-customer']/div/div[1]/a"

    # Desktop tab xpath elements
    dktop_dropdown_xpath = "//*[@id='narbar-menu']/ul/li[1]/a"  #  Desktop dropdown
    pc_xpath = "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[1]/a"  # select PC
    mac_xpath = "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[2]/a"  # select MAC
    show_all_xpath = "//*[@id='narbar-menu']/ul/li[1]/div/a"  # show all PC and MAC

    def __init__(self, driver):
        self.driver = driver

    def clickFeature(self):
        featureElement = WebDriverWait(self.driver, 25).until(ec.presence_of_element_located(
            (By.LINK_TEXT, self.lnk_feature_linktext)))
        featureElement.click()

    def clickDemo(self):
        #self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()
        demElement = WebDriverWait(self.driver, 25).until(ec.presence_of_element_located(
            (By.LINK_TEXT, self.lnk_demo_linktext)))
        demElement.click()

    def clickMyAccountRegister(self):
        #self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
        # self.driver.find_element(By.LINK_TEXT, self.lnk_myaccount_linktext).click()
        # element_wait = WebDriverWait(self.driver, 25, poll_frequency=1,
        #                         ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        time.sleep(3)
        element_wait = WebDriverWait(self.driver, 25).until(ec.presence_of_element_located(
            (By.XPATH, self.dropdown_myaccount_xpath)))
        element_wait.click()
        # select dropdown element in <li> option can't use Select()
        # use until(ec.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
        el = WebDriverWait(self.driver, 60).until(
            ec.element_to_be_clickable((By.LINK_TEXT, self.myacct_register_linktxt)))
        el.click()

        # actionChains = ActionChains(self.driver)
        # actionChains.click(el).perform()
        #
        # # Create the object for Select class
        # dd_options = Select(el)

        # # List the values in Drop Down
        # dd_v = dd_options.options
        # for dd_values in dd_v:
        #     print(dd_values.text)

        # Click by Index
        # dd_options.select_by_visible_text("Register")
        # time.sleep(2)

        # actionChains = ActionChains(self.driver)
        # actionChains.move_to_element(element).perform()
        # select = Select(element)
        # select.select_by_index(1))

    def clickMyAccountLogin(self):
        # self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
        # self.driver.find_element(By.LINK_TEXT, self.lnk_myaccount_linktext).click()
        # self.driver.refresh()
        time.sleep(3)
        element_wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        el = element_wait.until(ec.presence_of_element_located((By.XPATH, self.dropdown_myaccount_xpath)))
        el.click()  # //*[@id="top"]/div/div[2]/ul/li[2]/div/a/span
        # select dropdown element in <li> option can't use Select()
        # use until(ec.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
        el_ac = WebDriverWait(self.driver, 25).until(
            ec.element_to_be_clickable((By.LINK_TEXT, self.myacct_login_linktxt)))
        el_ac.click()

    # def clickRegister(self):
    #     self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktext).click()

    def clickLogin(self):
        #self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()
        # logElement = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located(
        #     (By.LINK_TEXT, self.lnk_login_linktext)))
        # logElement.click()

        logElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, self.lnk_login_xpath)))
        logElement.click()

    def clickShopping(self):
        logElement = WebDriverWait(self.driver, 25).until(ec.presence_of_element_located(
            (By.XPATH, self.lnk_shopping)))
        logElement.click()

    def clickWishlist(self):
        logElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, self.lnk_wishlist)))
        logElement.click()

    def clickButtonBack(self):
        logElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, self.btn_back_xpath)))
        logElement.click()

    def clickPC(self):
        # Find Desktop tab dropdown menu element and hover on Desktop tab
        element_wait = WebDriverWait(self.driver, 60, poll_frequency=1,
                                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        desk_menu = element_wait.until(ec.visibility_of_element_located((By.XPATH, self.dktop_dropdown_xpath)))
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(desk_menu).perform()

        # Select on PC submenu
        el_ac = WebDriverWait(self.driver, 25).until(ec.element_to_be_clickable((By.XPATH, self.pc_xpath)))
        el_ac.click()

    def clickMAC(self):
        # Find Desktop tab dropdown menu element and hover on Desktop tab
        element_wait = WebDriverWait(self.driver, 60, poll_frequency=1,
                                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        desk_menu = element_wait.until(ec.visibility_of_element_located((By.XPATH, self.dktop_dropdown_xpath)))
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(desk_menu).perform()

        # Select on MAC submenu
        el_ac = WebDriverWait(self.driver, 25).until(ec.element_to_be_clickable((By.XPATH, self.mac_xpath)))
        el_ac.click()

    def clickShowAll(self):
        # Find Desktop tab dropdown menu element and hover on Desktop tab
        element_wait = WebDriverWait(self.driver, 60, poll_frequency=1,
                                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        desk_menu = element_wait.until(ec.visibility_of_element_located((By.XPATH, self.dktop_dropdown_xpath)))
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(desk_menu).perform()

        # select on Show All submenu
        el_ac = WebDriverWait(self.driver, 25).until(ec.element_to_be_clickable((By.XPATH, self.mac_xpath)))
        el_ac.click()
