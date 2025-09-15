import pytest
from pages.Add_limited_quantity_to_cart import AddToCart
from pages.add_item_by_search import AddItem
from pages.get_product_by_category import SortByCategory
from pages.go_to_cart_with_special_btn import ToCartWithBtn
from pages.order_execution import OrderExecution
from pages.request_to_search_field import SearchField
from pages.sorting_by_price import SortingByPrice
from pages.sorting_by_price_range import SortPriceRange
from pages.validation_for_login_form import ValidationLogin


def test_correct_making_order(driver, wait, faker):
    make_order = OrderExecution(driver, wait)
    make_order.open_page()
    make_order.add_product()
    make_order.check_indicator_addition_to_cart(wait)
    make_order.order_registration()
    make_order.fill_in_form_to_delivery(wait, faker)
    make_order.check_to_confirm_order('Confirm order')


def test_correct_quantity_addition(driver, wait):
    add_to_cart = AddToCart(driver, wait)
    add_to_cart.open_page()
    add_to_cart.add_limit_quantity()
    add_to_cart.get_quantity(wait)
    add_to_cart.add_cart()
    add_to_cart.go_to_cart(wait)
    add_to_cart.check_text_added_element('Order overview')


def test_correct_go_to_cart(driver, wait):
    btn_to_cart = ToCartWithBtn(driver, wait)
    btn_to_cart.open_page()
    btn_to_cart.adding_element()
    btn_to_cart.click_btn_to_cart(wait)
    btn_to_cart.check_get_added_element()


def test_correct_request_to_search_field(driver, wait):
    check_search_field = SearchField(driver, wait)
    check_search_field.open_page()
    check_search_field.enter_word_to_search_field('desk')
    check_search_field.check_all_found_words('desk')


def test_correct_get_product_by_using_category(driver,wait):
    get_product = SortByCategory(driver, wait)
    get_product.open_page()
    get_product.choose_filter_by_category(wait)
    get_product.get_element_for_checking()


def test_correct_validation_without_field_pass(driver, wait, faker):
    validation_login_form = ValidationLogin(driver, wait)
    validation_login_form.open_page()
    validation_login_form.sign_in()
    validation_login_form.login_form(faker)


def test_correct_sorting_by_price_filter(driver, wait):
    sorting_by_price_filter = SortingByPrice(driver, wait)
    sorting_by_price_filter.open_page()
    sorting_by_price_filter.get_prices_before()
    sorting_by_price_filter.click_price_filter(wait)
    sorting_by_price_filter.get_prices_after()
    sorting_by_price_filter.compare_received_values()


@pytest.mark.parametrize('test_value', [2000])
def test_correct_filtered_by_price(driver, test_value, wait):
    sort_by_price_range = SortPriceRange(driver, wait)
    sort_by_price_range.open_page()
    sort_by_price_range.get_min_value(wait, test_value)
    sort_by_price_range.check_price_of_received_items(test_value)


def test_correct_adding_product_by_search(driver, wait):
    add_item_by_search = AddItem(driver, wait)
    add_item_by_search.open_page()
    add_item_by_search.go_to_search_result(wait)
    add_item_by_search.switch_to_new_tab_and_get_text(wait)
    add_item_by_search.add_item_to_cart(wait)
    add_item_by_search.check_item_text()
