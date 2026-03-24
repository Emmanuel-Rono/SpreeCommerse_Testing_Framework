from selenium.webdriver.common.by import By

from Core.waits import wait_for_clickable
from Services.basepage import BasePage


class CartPage(BasePage):
    CART_LINK_CANDIDATES = [
        (By.CSS_SELECTOR, "a[href*='/cart']"),
        (By.CSS_SELECTOR, "a[href*='cart']"),
        (By.CSS_SELECTOR, "a[aria-label*='Cart']"),
    ]

    CART_ITEM_CANDIDATES = [
        (By.CSS_SELECTOR, ".cart-item"),
        (By.CSS_SELECTOR, "#line_items .line-item"),
        (By.CSS_SELECTOR, "[data-hook='cart_items'] .cart-item"),
    ]

    def open_cart(self, timeout=10):
        for locator in self.CART_LINK_CANDIDATES:
            try:
                link = wait_for_clickable(self.driver, locator, timeout=timeout)
                link.click()
                return
            except Exception:
                continue
        raise AssertionError("Could not find cart link/icon to open cart")

    def is_cart_page(self):
        url = self.driver.current_url.lower()
        title = self.driver.title.lower()
        return "/cart" in url or "cart" in title

    def get_line_items_count(self):
        for locator in self.CART_ITEM_CANDIDATES:
            items = self.driver.find_elements(*locator)
            if items:
                return len(items)
        return 0
