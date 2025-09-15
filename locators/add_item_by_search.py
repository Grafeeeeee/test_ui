from selenium.webdriver.common.by import By

all_cards_loc = (By.XPATH, '//div[@class="oe_product_image position-relative h-100 flex-grow-0 overflow-hidden"]')
search_field_loc = (By.XPATH, '(//input[@type="search"])[2]')
inner_info_loc = (By.XPATH, '//a[@class="oe_product_image_link d-block h-100 position-relative"]')
text_loc = (By.XPATH, '//p[@class="text-muted my-2"]')
element_loc = (By.XPATH, '//span[@class="fa fa-shopping-cart"]')
btn_go_to_cart_loc = (By.XPATH, '//a[@class="w-100 btn btn-primary"]')
check_text_loc = (By.XPATH, '//span[@class="d-block"]')