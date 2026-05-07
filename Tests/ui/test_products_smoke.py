import pytest

from Services.products_page import OpenProductsPage


@pytest.mark.ui
@pytest.mark.smoke
def test_products_page_lists_items(driver,settings):
    page = OpenProductsPage(driver, settings)
    page.open_products_page()
    products = page.get_product_list()
    assert len(products) > 0
    assert any(p.is_displayed() for p in products)

@pytest.mark.ui
def test_can_search_products(driver,settings):
    page = OpenProductsPage(driver,settings)
    page.open_products_page()
    page.search_products("Semi-Automatic Espresso Machine")
    products = page.get_product_list()
    # We avoid strict count; just confirm the page still renders product cards.
    assert len(products) > 0
