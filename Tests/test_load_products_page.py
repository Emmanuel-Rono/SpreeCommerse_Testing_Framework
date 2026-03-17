# Tests/test_load_products_page.py
from Locators.locators import ProductsPageLocators
from Services.products_page import OpenProductsPage


def test_load_products_page(driver):
    driver.get("https://demo.spreecommerce.org/products")
    assert "Products" in driver.title

def test_click_first_product(driver):
    assert ProductsPageLocators.PRODUCT_ITEMS[0].is_displayed()
    assert ProductsPageLocators.PRODUCT_ITEMS[1].is_displayed()

def test_get_product_list(driver):
    page = OpenProductsPage(driver)
    page.OpenProductPage()
    products = page.get_product_list()
    #check presence
    assert len(products) > 0
    for product in products:
        assert product.is_displayed()


