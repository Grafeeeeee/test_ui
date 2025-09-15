from selenium.webdriver.common.by import By

btn_add_cart_loc = (By.ID, 'add_to_cart')
cart_indicator_loc = (
            By.CSS_SELECTOR,
            ".my_cart_quantity.badge.text-bg-primary.position-absolute.top-0.end-0.mt-n1.me-n1.rounded-pill")
checkout_loc = (By.CSS_SELECTOR, '[name="website_sale_main_button"]')
fullname_loc = (By.CSS_SELECTOR, '[name="name"]')
email_loc = (By.CSS_SELECTOR, '[name="email"]')
phone_loc = (By.CSS_SELECTOR, '[name="phone"]')
company_name_loc = (By.CSS_SELECTOR, '[name="company_name"]')
vat_loc = (By.CSS_SELECTOR, '[name="vat"]')
street_loc = (By.CSS_SELECTOR, '[name="street"]')
street2_loc = (By.CSS_SELECTOR, '[name="street2"]')
city_loc = (By.CSS_SELECTOR, '[name="city"]')
zip_loc = (By.CSS_SELECTOR, '[name="zip"]')
select_element_loc = (By.CSS_SELECTOR, '[name="country_id"]')
btn_checkout_loc = (
            By.CSS_SELECTOR,
            '.a-submit.a-submit-disable.a-submit-loading.btn.btn-primary.w-100.w-md-auto.order-1.order-md-3')
confirm_order_loc = (By.XPATH, '//h3[text()="Confirm order"]')
state_loc = (By.CSS_SELECTOR, '[name="state_id"]')