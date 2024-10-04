import pytest

from config.data import Data
from pages.main_page import MainPage


class BaseTest:

    data: Data

    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.main_page = MainPage(driver)