from pages.base_page import BasePage
from locators import fill_in_address_form as loc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class FillAddressForm(BasePage):

    page_url = '/shop/address'

    def __init__(self, driver, wait, faker):
        super().__init__(driver)

    def fill_in_form_to_delivery(self, wait, faker):
        fullname = self.find(loc.fullname_loc)
        fullname.send_keys(faker.name())
        email = self.find(loc.email_loc)
        email.send_keys(faker.email())
        phone = self.find(loc.phone_loc)
        phone.send_keys(faker.basic_phone_number())
        company_name = self.find(loc.company_name_loc)
        company_name.send_keys(faker.company())
        vat = self.find(loc.vat_loc)
        vat.send_keys('12521512')
        street = self.find(loc.street_loc)
        street.send_keys(faker.street_address())
        street2 = self.find(loc.street2_loc)
        street2.send_keys('None')
        city = self.find(loc.city_loc)
        city.send_keys(faker.city())
        zip = self.find(loc.zip_loc)
        zip.send_keys(faker.zipcode())
        select_element = self.find(loc.select_element_loc)
        select = Select(select_element)
        select.select_by_value('190')
        state = wait.until(EC.visibility_of_element_located(loc.state_loc))
        select_state = Select(state)
        select_state.select_by_value('108')
        btn_checkout = self.find(loc.btn_checkout_loc)
        btn_checkout.click()

    def check_text_to_confirm_order(self, text):
        assert self.find(loc.confirm_order_loc).text == text