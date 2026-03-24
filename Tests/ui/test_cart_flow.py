import pytest

from Services.cart_page import CartPage
from Services.product_details_page import ProductDetailsPage
from Services.products_page import OpenProductsPage


@pytest.mark.ui
@pytest.mark.regression
def test_add_to_cart_flow(driver):
    products = OpenProductsPage(driver)
    products.open_products_page()
    products.search_products("shirt")

    product_name = products.click_first_product()
    assert product_name is not None

    details = ProductDetailsPage(driver)
    details.add_to_cart()

    cart = CartPage(driver)
    if not cart.is_cart_page():
        cart.open_cart()

    assert cart.is_cart_page()
    assert cart.get_line_items_count() > 0
