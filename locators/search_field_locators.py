from selenium.webdriver.common.by import By

search_field_loc = (
        By.XPATH, '//input[@class="search-query form-control oe_search_box border-0 bg-light None"]'
)
all_elements_loc = (By.XPATH, '//div[contains(@class, "h6 fw-bold")]')