class BasePage:
    def __init__(self, driver, settings):
        self.driver = driver
        self.settings = settings

    def open(self, path=""):
        url = f"{self.settings.base_url}{path}"
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
