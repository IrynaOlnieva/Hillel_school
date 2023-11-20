from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_registration_test(self):

        # self.driver.implicitly_wait(3)
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        sign_up_button = self.driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        name_field = self.driver.find_element(By.ID, "signupName")
        name_field.send_keys("Jon")
        last_name_field = self.driver.find_element(By.ID, "signupLastName")
        last_name_field.send_keys("Duo")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        email_field.send_keys("55555aaa@test.com")
        password_field = self.driver.find_element(By.ID, "signupPassword")
        password_field.send_keys("Qwerty12345")
        repeat_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_field.send_keys("Qwerty12345")
        register_button = self.driver.find_element(By.XPATH, '//button[text()="Register"]')
        register_button.click()
        empty_garage = self.driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
        assert len(empty_garage) != 0

    def teardown_class(self):
        self.driver.quit()
a = 0