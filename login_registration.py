# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(2)
# email = driver.find_element_by_id("reg_email")
# email.send_keys("gug@gmail.com")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Gugara@90876")
# driver.find_element_by_css_selector(".woocomerce-FormRow .woocommerce-Button").click()
# driver.quit()

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
driver.find_element_by_link_text("My Account").click()
time.sleep(2)
username = driver.find_element_by_id("username")
username.send_keys("gug@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Gugara@90876")
driver.find_element_by_xpath('//input[@value="Login"]').click()
time.sleep(2)
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))
driver.quit()