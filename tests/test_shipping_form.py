import pytest


def test_correct_making_order(driver, wait, faker, office_design_software, fill_address_form, order_overview):
    btn_to_cart = office_design_software
    btn_to_cart.open_page()
    btn_to_cart.button_adding_element()
    btn_to_cart.check_indicator_addition_to_cart(wait)
    checkout = order_overview
    checkout.click_button_checkout()
    fill_form = fill_address_form
    fill_form.fill_in_form_to_delivery(wait, faker)
    fill_form.check_text_to_confirm_order('Confirm order')


def test_correct_quantity_addition(driver, wait, office_design_software, order_overview):
    btn_to_cart = office_design_software
    btn_to_cart.open_page()
    btn_to_cart.add_limit_quantity(5, wait)
    quantity = btn_to_cart.get_quantity(wait)
    btn_to_cart.button_adding_element()
    btn_to_cart.go_to_cart(wait)
    order_view = order_overview  #
    # никак не смог передать данный класс через фикстуру для передачи quantity. PS : разобрался в чем было дело
    order_view.check_title_added_element('Order overview')
    order_view.check_quantity_added_element(quantity)


def test_correct_go_to_cart(driver, wait, office_design_software, order_overview):
    btn_to_cart = office_design_software
    btn_to_cart.open_page()
    product = btn_to_cart.get_element_text_before()
    order_view = order_overview
    btn_to_cart.button_adding_element()
    btn_to_cart.click_btn_view_to_cart(wait)
    order_view.check_get_added_element(product)


def test_correct_request_to_search_field(driver, wait, search_page):
    search = search_page
    search.open_page()
    search.enter_word_to_search_field('desk')
    search.check_all_found_words('desk')


def test_incorrect_get_product_by_using_category(driver, wait, search_page, category_desk):
    search = search_page
    search.open_page()
    search.choose_filter_by_category(wait)
    nav_category = category_desk
    nav_category.get_item_by_filter_category_desk()


def test_correct_validation_without_field_pass(driver, wait, faker, page_login_form, search_page):
    search = search_page
    search.open_page()
    search.sign_in()
    login_page = page_login_form
    login_page.validate_login_form_with_empty_pass_field(faker)


def test_correct_sorting_by_price_filter(driver, wait, category_desk):
    desk_category = category_desk
    desk_category.open_page()
    desk_category.get_prices_before()
    desk_category.click_price_filter(wait)
    desk_category.get_prices_after()
    desk_category.compare_received_values()


@pytest.mark.parametrize('test_value', [2000])
def test_correct_filtered_by_price(driver, test_value, wait, category_desk):
    sort_by_price_range = category_desk
    sort_by_price_range.open_page()
    sort_by_price_range.get_min_value(wait, test_value)
    sort_by_price_range.check_price_of_received_items(test_value)


def test_correct_adding_product_by_search(driver, wait, category_desk, order_overview):
    add_item_by_search = category_desk
    add_item_by_search.open_page()
    add_item_by_search.go_to_search_result(wait)
    add_item_by_search.switch_to_new_tab_and_get_text(wait)
    add_item_by_search.add_item_to_cart(wait)
    text = add_item_by_search.get_text_to_check()
    check_text = order_overview
    check_text.check_item_text(text)
