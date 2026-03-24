import pytest

from Services.products_page import OpenProductsPage


@pytest.mark.ui
@pytest.mark.smoke
def test_products_page_lists_items(driver):
    page = OpenProductsPage(driver)
    page.open_products_page()
    products = page.get_product_list()
    assert len(products) > 0
    assert all(p.is_displayed() for p in products)


@pytest.mark.ui
def test_can_search_products(driver):
    page = OpenProductsPage(driver)
    page.open_products_page()
    page.search_products("shirt")
    products = page.get_product_list()
    # We avoid strict count; just confirm the page still renders product cards.
    assert len(products) > 0
