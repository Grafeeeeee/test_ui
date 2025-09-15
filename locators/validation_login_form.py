from selenium.webdriver.common.by import By

sign_in_btn_loc = (By.XPATH, '//a[@class="btn btn-outline-secondary"]')
email_field_loc = (By.CSS_SELECTOR, '[id="login"]')
pass_field_loc = (By.XPATH, '//input[@name="password"]')