import time

import allure
from base.base_test import BaseTest


@allure.feature("Test registration")
class TestMainPage(BaseTest):

    @allure.title("Check registration")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    def test_registration(self):
        self.main_page.open()
        self.main_page.is_opened()
        self.main_page.check_main_word()
        self.main_page.click_sign_up_link()
        self.main_page.input_user_name(self.data.LOGIN)
        self.main_page.input_password(self.data.PASSWORD)
        self.main_page.click_sign_up_button()
        self.main_page.click_close_button_sign_up()
        self.main_page.click_log_in_link()
        self.main_page.input_user_name_log_in(self.data.LOGIN)
        self.main_page.input_password_log_in(self.data.PASSWORD)
        self.main_page.click_log_in_button()
        self.main_page.click_close_button_log_in()

