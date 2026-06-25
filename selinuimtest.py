
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login")
driver.maximize_window()
# Explicit wait setup
wait=WebDriverWait(driver, 10)
# Use a stable locator (partial match on ID)

username_locator=(By.ID, "usernameField")
password_locator=(By.ID, "passwordField")

username_field =wait.until(EC.visibility_of_element_located(username_locator))
password_field =wait.until(EC.visibility_of_element_located(password_locator))

username_field.send_keys("nagavani0809@gmail.com")
password_field.send_keys("Pa123456#")


submit_btn_locator = (By.XPATH, "//button[@type='submit']")
# Wait until button is clickable
submit_button=wait.until(EC.element_to_be_clickable(submit_btn_locator))

clicked=False
attempts=0
while attempts<5 and clicked==False:
    try:
        submit_button.click()
        clicked=True
    except StaleElementReferenceException:
        submit_button=wait.until(EC.element_to_be_clickable(submit_btn_locator))
    attempts+=1

time.sleep(5)
driver.quit()







