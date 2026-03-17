
from Configuration.settings import PRODUCTS_PAGE
from Locators.locators import ProductsPageLocators
from Services.basepage import BasePage

class OpenProductsPage(BasePage):
    def OpenProductPage(self):
        self.open(PRODUCTS_PAGE)

    def get_page_title(self):
        self.get_title()

    def get_product_list(self):
        return self.driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)

    def click_first_product(self):
        self.open(PRODUCTS_PAGE)
        productlinks=self.driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)
        if productlinks:
            productlinks[0].click()


    def  search_products(self,product_name):
        search_box = self.driver.find_element(*ProductsPageLocators.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(product_name)
        self.driver.find_element(*ProductsPageLocators.SEARCH_BUTTON).click()


    def add_first_product_to_wishlist(self,the_variantid):
        wishlist_buttons = self.driver.find_elements(*ProductsPageLocators.wishlist_button(the_variantid))
        if wishlist_buttons:
            wishlist_buttons[0].click()



