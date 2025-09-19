from selenium.webdriver.common.by import By

btn_add_cart_loc = (By.ID, 'add_to_cart')
add_quantity_loc = (By.CSS_SELECTOR, '.fa.fa-plus')
quantity_loc = (By.NAME, 'add_qty')
cart_indicator_loc = (
            By.CSS_SELECTOR,
            ".my_cart_quantity.badge.text-bg-primary.position-absolute.top-0.end-0.mt-n1.me-n1.rounded-pill")
cart_loc = (By.XPATH, '//sup[contains(@class, "my_cart_quantity")]')
adding_element_before_loc = (By.XPATH, '//h1[text()="Office Design Software"]')
btn_view_cart_loc = (By.XPATH, '//a[@class="w-100 btn btn-primary"]')