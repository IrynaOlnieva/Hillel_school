from selenium_example.pages.garage_page import GaragePage
from selenium_example.pages.main_page import MainPage
from selenium_example.pages.registration_form_page import RegistrationFormPage


class BaseFacade:
    def __init__(self, driver):
        self._driver = driver
        self._main_page = MainPage(self._driver)
        self._registration_form_page = RegistrationFormPage(self._driver)
        self._garage_page = GaragePage(self._driver)