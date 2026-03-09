from Configuration.settings import PRODUCTS_PAGE
from Services.basepage import BasePage


class OpenProductsPage(BasePage):
    def OpenProductPage(self):
        self.open(PRODUCTS_PAGE)

    def