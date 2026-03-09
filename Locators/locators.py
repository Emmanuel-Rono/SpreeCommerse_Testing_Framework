from selenium.webdriver.common.by import By


class ProductsPageLocators:

    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-component")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".product-component a")

    SEARCH_INPUT = (By.ID, "keywords")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".add-to-wishlist")