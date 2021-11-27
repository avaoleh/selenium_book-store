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
    # driver.implicitly_wait(5)
    first_browser_tab = driver.window_handles[0]
    driver.switch_to.window(first_browser_tab)

    # 1 Откройте http://practice.automationtesting.in/
    driver.get(link)

    # 2 Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
    shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a").click()
    driver.execute_script("window.scrollBy(0, 600);")
    # time.sleep(2)

    # 3 Добавьте в корзину книгу "HTML5 WebApp Development"
    add_book_btn = driver.find_element(By.XPATH, "//a[@href='/shop/?add-to-cart=182']")
    add_book_btn.click()

    # 4 Перейдите в корзину
    cart_btn = driver.find_element(By.ID, "wpmenucartli").click()

    #5 Нажмите "PROCEED TO CHECKOUT"
    driver.execute_script("window.scrollBy(0, 600);")
    procced_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.wc-proceed-to-checkout > a.checkout-button.button.alt.wc-forward")))

    # 6 Заполните все обязательные поля
    first_name = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.ID, "billing_first_name")))
    if first_name:
        driver.find_element(By.ID, "billing_first_name").sendKeys("John")
    last_name = driver.find_element(By.ID, "billing_last_name").sendKeys("Doe")
    email = driver.find_element(By.ID, "billing_email").sendKeys("johndoe@test.com")
    tel = driver.find_element(By.ID, "billing_phone").sendKeys("+79000000000")

    driver.execute_script("window.scrollBy(0, 400);")
    county = driver.find_element(By.ID, "s2id_billing_country").click()
    county_input = driver.find_element(By.ID, "s2id_autogen1_search").sendKeys("Russia")
    county_match = driver.find_element(By.CSS_SELECTOR, "span.select2-match").sendKeys("Russia")

    adress = driver.find_element(By.ID, "billing_address_1").sendKeys("Moscow 100500")
    city = driver.find_element(By.ID, "billing_city").sendKeys("Moscow")
    postcode = driver.find_element(By.ID, "billing_postcode").sendKeys("Moscow")

    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(5)

    # 7. Выберите способ оплаты "Check Payments"
    payment_method_cheque = driver.find_element(By.ID, "payment_method_cheque").click()

    # 8. Нажмите PLACE ORDER
    place_order = driver.find_element(By.ID, "place_order").click()

    # 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
    confirm_order = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "div.page-content entry-content > div.woocommerce > p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

    #10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
    payment_method_cheque_txt = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "ul.woocommerce-thankyou-order-details.order_details > li.method > strong"), "Check Payments"))

    time.sleep(2)

finally:
    driver.quit()
