import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

link = "http://practice.automationtesting.in/"

try:
    path_to_extension = r'C:\Users\Tom\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.39.1_0'
    chrome_options = Options()
    chrome_options.add_argument('loadextension=' + path_to_extension)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.create_options()
    time.sleep(5)
    driver.maximize_window()
    driver.implicitly_wait(5)
    first_browser_tab = driver.window_handles[0]
    driver.switch_to.window(first_browser_tab)
    driver.get(link)

    #register
    # my_account = driver.find_element(By.XPATH, "//a[@href='http://practice.automationtesting.in/my-account/']").click()
    #
    # reg_email = driver.find_element(By.ID, "reg_email").send_keys("johndoe@test.com")
    # reg_password = driver.find_element(By.ID, "reg_password").send_keys("$87&6^asd)(@test")
    # submit = driver.find_element(By.NAME, "register").click()

    #login
    my_account = driver.find_element(By.XPATH, "//a[@href='http://practice.automationtesting.in/my-account/']").click()

    username = driver.find_element(By.ID, "username").send_keys("johndoe@testtest.com")
    password = driver.find_element(By.ID, "password").send_keys("$87&6^asd)(@test")
    submit = driver.find_element(By.NAME, "login").click()

    logout = WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://practice.automationtesting.in/my-account/customer-logout/']")))
    assert logout is not None, "No such element on login page"

    time.sleep(2)
finally:
    driver.quit()
