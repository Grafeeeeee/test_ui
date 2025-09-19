from selenium.webdriver.common.by import By

checkout_loc = (By.CSS_SELECTOR, '[name="website_sale_main_button"]')
adding_element_after_loc = (By.XPATH, '//h6[text()="Office Design Software"]')
order_text_loc = (By.TAG_NAME, 'h3')
order_total_quantity_loc = (By.XPATH, '//input[contains(@class,"js_quantity quantity")]')
check_text_loc = (By.XPATH, '//span[@class="d-block"]')