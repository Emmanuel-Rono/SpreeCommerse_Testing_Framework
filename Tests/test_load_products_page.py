# Tests/test_load_products_page.py
from selenium.webdriver.common.by import By

from Locators.locators import ProductsPageLocators
from Services.products_page import OpenProductsPage


def test_load_products_page(driver):
    driver.get("https://demo.spreecommerce.org/products")
    assert "Products" in driver.title

 #tets click first product

def test_get_product_list(driver):
    page = OpenProductsPage(driver)
    page.OpenProductPage()
    products = page.get_product_list()
    #check presence
    assert len(products) > 0
    #check if displayed
    for product in products:
        assert product.is_displayed()



