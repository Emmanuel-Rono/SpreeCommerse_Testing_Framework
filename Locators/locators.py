from selenium.webdriver.common.by import By


class ProductsPageLocators:

    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-component")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".product-component a")

    SEARCH_INPUT = (By.ID, "keywords")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    WISHLIST_BUTTON = (By.CSS_SELECTOR,"div[data-wished-item-variant-id-value='2125'] button[aria-label='Add to wishlist']" )

    @staticmethod
    def wishlist_Button(variant_id):
        return(
            By.CSS_SELECTOR,
            f"div[data-wished-item-variant-id-value='{variant_id}'] button[aria-label='Add to wishlist']"
        )