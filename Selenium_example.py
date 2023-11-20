# from selenium import webdriver
# from selenium.webdriver.common.by.import By
# # //button[text()='Sign up']
# driver = webdriver.Chrome()
# # driver.get("https://google.com")
# driver.get("https://quest:welcome2qauto@qauto2.forstudy.space/")
# sing_up_button = driver.find_element(By.XPATH,"//button[text()='Sign up']")
# sing_up_button.click()
# a = 0

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


#//button[text()='Sign up']
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")
chrome_options = Options()
# chrome_options.add_argument("--window-size=100,100")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
sign_up_button.click()
name_field = driver.find_element(By.ID, "signupName")
name_field.send_keys("test123")


a = 0