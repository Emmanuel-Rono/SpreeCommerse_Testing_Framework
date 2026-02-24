# Tests/test_load_products_page.py
def test_load_products_page(driver):
    driver.get("https://demo.spreecommerce.org/products")
    assert "Products" in driver.title