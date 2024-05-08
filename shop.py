# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(2)
# username = driver.find_element_by_id("username")
# username.send_keys("gug@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gugara@90876")
# driver.find_element_by_xpath('//input[@value="Login"]').click()
# time.sleep(2)
# driver.find_element_by_link_text("Shop").click()
# time.sleep(2)
# driver.find_element_by_css_selector(".post-181 .woocommerce-LoopProduct-link").click()
# time.sleep(2)
# element = driver.find_element_by_css_selector(".entry-summary .product_title")
# element_get_text = element.text
# assert "HTML5 Forms" in element_get_text
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(2)
# username = driver.find_element_by_id("username")
# username.send_keys("gug@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gugara@90876")
# driver.find_element_by_xpath('//input[@value="Login"]').click()
# time.sleep(2)
# driver.find_element_by_link_text("Shop").click()
# time.sleep(2)
# driver.find_element_by_css_selector(".cat-item-19>a").click()
# time.sleep(2)
# items_count = driver.find_elements_by_class_name("type-product")
# if len(items_count) == 3:
#     print("3 товара")
# else:
#     print("товаров больше")
# driver.quit()

# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(2)
# username = driver.find_element_by_id("username")
# username.send_keys("gug@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gugara@90876")
# driver.find_element_by_xpath('//input[@value="Login"]').click()
# time.sleep(2)
# driver.find_element_by_link_text("Shop").click()
# time.sleep(2)
# sort=driver.find_element_by_xpath('//option[@value ="menu_order"]')
# sort_by=sort.get_attribute("selected")
# if sort_by is not None:
#     print("Статус: по умолчанию")
# else:
#     print("Статус: не по умолчанию")
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# time.sleep(2)
# sort2=driver.find_element_by_xpath('//option[@value ="price-desc"]')
# sort_by2=sort2.get_attribute("selected")
# if sort_by2 is not None:
#     print("Статус: От большего к меньшему")
# else:
#     print("Статус: не от большего к меньшему")
# driver.quit()

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(2)
# username = driver.find_element_by_id("username")
# username.send_keys("gug@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Gugara@90876")
# driver.find_element_by_xpath('//input[@value="Login"]').click()
# time.sleep(2)
# driver.find_element_by_link_text("Shop").click()
# time.sleep(2)
# driver.find_element_by_class_name("product_tag-android").click()
# time.sleep(2)
# price1 = driver.find_element_by_css_selector("del .woocommerce-Price-amount")
# price1_price = price1.text
# assert "₹600.00" in price1_price
# price2 = driver.find_element_by_css_selector("ins .woocommerce-Price-amount")
# price2_price = price2.text
# assert "₹450.00" in price2_price
# driver.find_element_by_class_name("woocommerce-main-image").click()
# WebDriverWait(driver, 10).until(
# EC. visibility_of_element_located((By.ID, "fullResImage")))
# WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# driver.find_element_by_class_name("pp_close").click()
# driver.quit()

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("Shop").click()
# time.sleep(2)
# driver.find_element_by_css_selector(".post-182 .ajax_add_to_cart").click()
# time.sleep(3)
# item = driver.find_element_by_class_name("cartcontents")
# item_num = item.text
# assert "1 Item" in item_num
# price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# item_price = price.text
# assert "₹180.00" in item_price
# driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(2)
# subtotal= WebDriverWait(driver, 10).until(
# EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount")))
# total= WebDriverWait(driver, 10).until(
# EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount")))
# driver.quit()

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("Shop").click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector(".post-182 .ajax_add_to_cart").click()
# time.sleep(3)
# driver.find_element_by_css_selector(".post-180 .ajax_add_to_cart").click()
# time.sleep(1)
# driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(3)
# driver.find_element_by_css_selector(".cart_item:nth-child(1) .product-remove .remove").click()
# time.sleep(2)
# driver.find_element_by_link_text("Undo?").click()
# time.sleep(2)
# quant = driver.find_element_by_css_selector(".cart_item:nth-child(1) .product-quantity .quantity .input-text")
# quant.clear()
# quant.send_keys(3)
# time.sleep(2)
# driver.find_element_by_xpath('//input[@value="Update Basket"]').click()
# time.sleep(3)
# quant1 = driver.find_element_by_css_selector(".cart_item:nth-child(1) .product-quantity .quantity .input-text")
# quant_check = quant1.get_attribute("value")
# assert quant_check == "3"
# driver.find_element_by_xpath('//input[@value="Apply Coupon"]').click()
# time.sleep(2)
# WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error li"), "Please enter a coupon code."))
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
driver.find_element_by_link_text("Shop").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector(".post-182 .ajax_add_to_cart").click()
time.sleep(3)
driver.find_element_by_class_name("wpmenucart-contents").click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "wc-forward")))
driver.find_element_by_class_name("wc-forward").click()
time.sleep(3)
WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.ID, "billing_first_name_field"), "First Name"))
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Guga")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Gugarovski")
email = driver.find_element_by_id("billing_email")
email.send_keys("gug@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+87655648117")
driver.find_element_by_id("s2id_billing_country").click()
time.sleep(1)
country = driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Ivory Coast")
time.sleep(1)
driver.find_element_by_class_name("select2-result-label").click()
street = driver.find_element_by_id("billing_address_1")
street.send_keys("Gugara Street")
city = driver.find_element_by_id("billing_city")
city.send_keys("Gugargrad")
state = driver.find_element_by_id("billing_state")
state.send_keys("GUGARA")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("189765")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_id("payment_method_cheque").click()
time.sleep(2)
driver.find_element_by_css_selector(".place-order .button").click()
time.sleep(2)
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3)>td"), "Check Payments"))
driver.quit()