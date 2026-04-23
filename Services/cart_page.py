from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Core.waits import wait_for_clickable
from Services.basepage import BasePage


class CartPage(BasePage):
    TO_CART_BUTTON = (By.XPATH,"/html/body/header/div[1]/div/div/div[3]/button[2]")

    CART_ITEMS = ( By.XPATH, "//ul/li[.//a[contains(@href,'/products/')]]")


    def open_cart(self, timeout=10):
        
            try:
                link = wait_for_clickable(self.driver, timeout=timeout)
                link.click()
                return
            except Exception:
                raise AssertionError("Could not find cart link/icon to open cart")

    def is_cart_page(self):
        url = self.driver.current_url.lower()
        title = self.driver.title.lower()
        return "/cart" in url or "cart" in title

    def get_line_items_count(self):
        for locator in self.TO_CART_BUTTON:
            items = self.driver.find_elements(*locator)
            if items:
                return len(items)
        return 0

    def wait_for_line_items(self, timeout=10):
        def _has_items(driver):
           
                items = driver.find_elements(*self.CART_ITEMS)
                if items:
                    return items
           

        return WebDriverWait(self.driver, timeout).until(_has_items)
