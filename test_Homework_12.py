import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()

    # def teardown_method(self):
    #     self._driver.close()

class TestRegistration(TestBase):

    def setup_class(self):
        # self.session = requests.session()
        self.user_email = "5556y3556644fffррр6ffhhhm55py5544ff4ttttk5@test.com"
        self.user_password = "Qwerty12345"

        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_method(self, driver_close):
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json = self.user_to_login)
        self._session.delete(url="https://gauto2.forstudy.spase/api/users")
        driver_close(self._driver)


    def test_registration_test(self,driver_close):
        # driver = webdriver.Chrome()
        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        sign_up_button = self.driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        name_field = self.driver.find_element(By.ID, "signupName")
        name_field.send_keys("John")
        last_name_field = self.driver.find_element(By.ID, "signupLastName")
        last_name_field.send_keys("Duo")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        email_field.send_keys(self.user_email)
        password_field = self.driver.find_element(By.ID, "signupPassword")
        password_field.send_keys(self.user_password)
        repeat_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_field.send_keys(self.user_password)
        register_button = self.driver.find_element(By.XPATH, '//button[text()="Register"]')
        register_button.click()

        garage_world = self.driver.find_elements(By.XPATH, "//p[text()='You don't have any cars in your garage']")
        assert len(garage_world) != 0
    #
    #     a = 0
    # def test_registration_1_test(self):
    #     self._driver.implicitly_wait(3)
    #     self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    #     sign_up_button = self._driver.find_element(By.XPATH, "//button[text()='Sign up']")
    #     sign_up_button.click()
    #     name_field = self._driver.find_element(By.ID, "signupName")
    #     name_field.send_keys("test")
    #     last_name_field = self._driver.find_element(By.ID, "signupLastName")
    #     last_name_field.send_keys("lastnametest")
    #     email_field = self._driver.find_element(By.ID, "signupEmail")
    #     email_field.send_keys(self.user_email)
    #     password_field = self._driver.find_element(By.ID, "signupPassword")
    #     password_field.send_keys(self.user_password)
    #     repeat_password_field = self._driver.find_element(By.ID, "signupRepeatPassword")
    #     repeat_password_field.send_keys(self.user_password)
    #     register_button = self._driver.find_element(By.XPATH, '//button[text()="Register"]')
    #     register_button.click()
    #     empty_garage = self._driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
    #     assert len(empty_garage) != 0