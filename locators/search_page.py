from selenium.webdriver.common.by import By

search_field_loc = (
        By.XPATH, '//input[@class="search-query form-control oe_search_box border-0 bg-light None"]'
)
nav_menu_loc = (By.CSS_SELECTOR, 'a.nav-link.dropdown-toggle')
desks_category_loc = (By.XPATH, '//a[@class="dropdown-item "]')
all_elements_loc = (By.XPATH, '//div[contains(@class, "h6 fw-bold")]')
sign_in_btn_loc = (By.XPATH, '//a[@class="btn btn-outline-secondary"]')