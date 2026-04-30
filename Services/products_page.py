from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Locators.locators import ProductsPageLocators
from Services.basepage import BasePage


class OpenProductsPage(BasePage):
    def OpenProductPage(self):
        self.open("/products")

    def open_products_page(self):
        self.open("/products")

    def get_page_title(self):
        return self.get_title()

    def get_product_list(self):
        return self.driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)

    def _wait_for_any_product(self, timeout=10):
        def _has_products(driver):
            elements = driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)
            return elements if elements else False

        return WebDriverWait(self.driver, timeout).until(_has_products)

    def wait_for_products_loaded(self, timeout=10):
        return self._wait_for_any_product(timeout=timeout)

    def click_first_product(self):
        product_links = self._wait_for_any_product()
        if product_links:
            product_name = product_links[0].text
            product_links[0].click()
            return product_name
        return None

    def search_products(self, product_name):
        search_box = self.driver.find_element(*ProductsPageLocators.SEARCH_INPUT)
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.BACKSPACE)
        search_box.send_keys(product_name)

    def add_first_product_to_wishlist(self, the_variantid):
        wishlist_buttons = self.driver.find_elements(*ProductsPageLocators.wishlist_button(the_variantid))
        if wishlist_buttons:
            wishlist_buttons[0].click()
