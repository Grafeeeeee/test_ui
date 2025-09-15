from selenium.webdriver.common.by import By

add_quantity_loc = (By.CSS_SELECTOR, '.fa.fa-plus')
btn_add_cart_loc = (By.ID, 'add_to_cart')
quantity_loc = (By.NAME, 'add_qty')
cart_loc = (By.XPATH, '//sup[contains(@class, "my_cart_quantity")]')
order_text_loc = (By.TAG_NAME, 'h3')
order_total_quantity_loc = (By.XPATH, '//input[contains(@class,"js_quantity quantity")]')