from selenium.webdriver.common.by import By


class ProductsPageLocators:
    PRODUCT_ITEMS = (By.CSS_SELECTOR, "#products a[id^='product-']")
    PRODUCT_LINKS = (By.CSS_SELECTOR, "#products a[id^='product-']")
    SEARCH_INPUT = (By.ID, "keywords")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    @staticmethod
    def wishlist_button(variant_id):
        return(
            By.CSS_SELECTOR,
            f"div[data-wished-item-variant-id-value='{variant_id}'] button[aria-label='Add to wishlist']"
        )

    @staticmethod
    def products_button(product_id):
        return (
            By.CSS_SELECTOR,
            f"div['mb-3 relative w-full product-card-featured-image'] id='{product_id}']"
        )
