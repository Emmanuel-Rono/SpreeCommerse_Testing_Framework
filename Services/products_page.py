from selenium.webdriver.common.by import By

from Configuration.settings import PRODUCTS_PAGE
from Core.waits import wait_for_visible, wait_for_clickable
from Locators.locators import ProductsPageLocators
from Services.basepage import BasePage


class OpenProductsPage(BasePage):
    def OpenProductPage(self):
        self.open(PRODUCTS_PAGE)

    # New preferred naming style
    def open_products_page(self):
        self.open(PRODUCTS_PAGE)

    def get_page_title(self):
        return self.get_title()

    def get_product_list(self):
        return self.driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)

    def click_first_product(self):
        self.open(PRODUCTS_PAGE)
        product_links = self.driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)

        if product_links:
            product_name = product_links[0].text
            product_links[0].click()
            return product_name
        return None

    def _find_first(self, locators, timeout=10):
        last_error = None
        for locator in locators:
            try:
                return wait_for_visible(self.driver, locator, timeout=timeout)
            except Exception as exc:
                last_error = exc
        if last_error:
            raise last_error
        raise AssertionError("No locator candidates provided")

    def search_products(self, product_name):
        search_input_candidates = [
            ProductsPageLocators.SEARCH_INPUT,
            (By.CSS_SELECTOR, "input[type='search']"),
            (By.NAME, "q"),
            (By.CSS_SELECTOR, "input[name*='query']"),
        ]
        search_button_candidates = [
            ProductsPageLocators.SEARCH_BUTTON,
            (By.CSS_SELECTOR, "button[type='submit']"),
            (By.CSS_SELECTOR, "input[type='submit']"),
        ]

        search_box = self._find_first(search_input_candidates)
        search_box.clear()
        search_box.send_keys(product_name)

        try:
            search_button = self._find_first(search_button_candidates)
            wait_for_clickable(self.driver, search_button_candidates[0], timeout=5)
            search_button.click()
        except Exception:
            # Some sites auto-search on input; ignore if submit not found.
            pass

    def add_first_product_to_wishlist(self, the_variantid):
        wishlist_buttons = self.driver.find_elements(*ProductsPageLocators.wishlist_button(the_variantid))
        if wishlist_buttons:
            wishlist_buttons[0].click()
