from selenium.webdriver.common.by import By
from selenium_example.pages.base_page import BasePage


class RegistrationFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.name_field_locator = By.ID, "signupName"
        self.last_name_field_locator = By.ID, "signupLastName"
        self.email_field_locator = By.ID, "signupEmail"
        self.password_field = lambda: self._driver.find_element(By.ID, "signupPassword")
        self.reenter_password_field = lambda: self._driver.find_element(By.ID, "signupRepeatPassword")
        self.register_button = lambda: self._driver.find_element(By.XPATH, "//button[text()='Register']")

    @property
    def name_field(self):
        return self._driver.find_element(*self.name_field_location)

    @property
    def last_name_field(self):
        return self.._driver.find_element(*self.last_name_field_locator)

    @property
    def email_field(self):
        return self._driver.find_element(*self.email_field_location)
reg_form = RegistrationFormPage(object)