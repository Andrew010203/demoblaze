

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = Links.MAIN_PAGE

    MAIN_WORD = ("xpath", '//a[text()="CATEGORIES"]')
    SIGN_UP_LINK = ("xpath", '//a[@id="signin2"]')
    USER_NAME_FIELD = ("xpath", '//input[@id="sign-username"]')
    PASSWORD_FIELD = ("xpath", '//input[@id="sign-password"]')
    SIGN_UP_BUTTON = ("xpath", '//button[text()="Sign up"]')
    CLOSE_SIGN_UP_BUTTON = ("xpath", '(//button[text()="Close"])[2]')
    LOG_IN_LINK = ("xpath", '//a[@id="login2"]')
    USER_NAME_FIELD_LOG_IN = ("xpath", '//input[@id="loginusername"]')
    PASSWORD_FIELD_LOG_IN = ("xpath", '//input[@id="loginpassword"]')
    LOG_IN_BUTTON = ("xpath", '//button[text()="Log in"]')
    CLOSE_LOG_IN_BUTTON = ("xpath", '(//button[text()="Close"])[3]')

    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'CATEGORIES')), "Текст не совпадает"

    def click_sign_up_link(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_UP_LINK)).click()

    def input_user_name(self, user_name):
        self.wait.until(EC.element_to_be_clickable(self.USER_NAME_FIELD)).send_keys(user_name)

    def input_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_sign_up_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_UP_BUTTON)).click()
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        alert.accept()

    def click_close_button_sign_up(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_SIGN_UP_BUTTON)).click()

    def click_log_in_link(self):
        self.wait.until(EC.element_to_be_clickable(self.LOG_IN_LINK)).click()

    def input_user_name_log_in(self, user_name):
        self.wait.until(EC.element_to_be_clickable(self.USER_NAME_FIELD_LOG_IN)).send_keys(user_name)

    def input_password_log_in(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD_LOG_IN)).send_keys(password)

    def click_log_in_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOG_IN_BUTTON)).click()
        alert = self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert
        alert.accept()

    def click_close_button_log_in(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_LOG_IN_BUTTON)).click()