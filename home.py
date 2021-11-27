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
    
    driver.execute_script("window.scrollBy(0, 600);")

    btn_click = driver.find_element(By.CSS_SELECTOR, ".woocommerce-LoopProduct-link").click()

    tab_reviews = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//a[@href ='#tab-reviews']")))
    tab_reviews.click()
    btn_stars = driver.find_element(By.CSS_SELECTOR, ".stars > span > .star-5").click()
    # driver.execute_script("return arguments[0].scrollIntoView( true);", btn_stars)
    # btn_stars.click()

    driver.execute_script("window.scrollBy(0, 500);")
    review_textarea = driver.find_element(By.ID, "comment").send_keys("Nice book!")
    name_input = driver.find_element(By.ID, "author").send_keys("johndoe")
    email_input = driver.find_element(By.ID, "email").send_keys("johndoe@text.com")

    submit = driver.find_element(By.ID, "submit").click()

    time.sleep(5)
finally:
    driver.quit()
