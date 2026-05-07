import pytest

from Services.cart_page import CartPage
from Services.product_details_page import ProductDetailsPage
from Services.products_page import OpenProductsPage
from Services.signin_to_account import Customer_Account


@pytest.mark.ui
@pytest.mark.regression
def test_add_to_cart_flow(driver, settings):
    products = OpenProductsPage(driver, settings)
    products.open_products_page()

    account = Customer_Account(driver, settings)
    account.open_account_page()
    account.enter_login_credentials(settings.test_user_email, settings.test_user_password)
    assert account.is_logged_in() is True

    products.open_products_page()
    products.search_products("Semi-Automatic Espresso Machine")
    products.wait_for_products_loaded()

    product_name = products.click_first_product()
    assert product_name is not None and product_name.strip() != ""

    details = ProductDetailsPage(driver, settings)
    details.add_to_cart()
    details.view_cart()

    cart = CartPage(driver, settings)
    assert cart.is_cart_page()
    cart.wait_for_line_items()
    assert cart.get_line_items_count() > 0
