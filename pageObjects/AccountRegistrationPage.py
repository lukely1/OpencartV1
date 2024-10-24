from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telphone_name = "telephone"
    txt_password_name = "password" # "//*[@id='form-register']/div/div/div/input" # password
    txt_confpassword_name = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath = "//*[@id='form-register']/div/button" #"//input[@value='Continue']" # //*[@id="form-register"]/div/div/button
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        # self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)
        fnElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.NAME, self.txt_firstname_name)))
        fnElement.send_keys(fname)

    def setLastName(self, lname):
        #self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)
        lnElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.NAME, self.txt_lastname_name)))
        lnElement.send_keys(lname)

    def setEmail(self, email):
        emElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.NAME, self.txt_email_name)))
        emElement.send_keys(email)

    def setTelephone(self, tel):
        self.driver.find_element(By.NAME, self.txt_telphone_name).send_keys(tel)

    def setPassword(self, pwd):
        # self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)
        pwdElement = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.NAME, self.txt_password_name)))
        pwdElement.send_keys(pwd)

    def setConfirmPassword(self, cnfpwd):
        #self.driver.find_element(By.NAME, self.txt_confpassword_name).send_keys(cnfpwd)
        cnfpwdele = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.LINK_TEXT, self.txt_confpassword_name)))
        cnfpwdele.send_keys(cnfpwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()

    def clickContinue(self):
        #self.driver.find_element(By.NAME, self.btn_cont_xpath).click()
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, self.btn_cont_xpath))).click()


    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None
