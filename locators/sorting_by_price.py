from selenium.webdriver.common.by import By

get_price_for_each_card_loc = (By.XPATH, '//span[@class="oe_currency_value"]')
filter_price_loc = (By.XPATH, '(//a[@class="dropdown-toggle btn btn-light"])[2]')
filter_low_to_high_loc = (By.XPATH, '//a[span[contains(text(), "Price - Low to High")]]')
get_price_after_filtered_loc = (By.XPATH, '//span[@class="oe_currency_value"]')