from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Core.waits import wait_for_clickable
from Services.basepage import BasePage


class CartPage(BasePage):
    CART_LINK_CANDIDATES = By.Xpath,"/html/body/header/div[1]/div/div/div[3]/button[2]"

    CART_ITEM_CANDIDATES =By.Xpath, "//*[@id="radix-_R_snpffb_"]/div[2]/ul/li"

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

    def wait_for_line_items(self, timeout=10):
        def _has_items(driver):
            for locator in self.CART_ITEM_CANDIDATES:
                items = driver.find_elements(*locator)
                if items:
                    return items
            return False

        return WebDriverWait(self.driver, timeout).until(_has_items)
