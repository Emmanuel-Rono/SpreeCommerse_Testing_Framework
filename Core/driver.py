import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Core.config import Settings


def _apply_common_options(options, settings: Settings):
    if settings.headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")


def get_driver(settings: Settings):
    if settings.remote_url:
        # Remote driver for Selenium Grid / Selenoid.
        return webdriver.Remote(command_executor=settings.remote_url, options=ChromeOptions())

    browser = settings.browser
    if browser == "firefox":
        options = FirefoxOptions()
        _apply_common_options(options, settings)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        options = EdgeOptions()
        _apply_common_options(options, settings)
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        options = ChromeOptions()
        _apply_common_options(options, settings)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.implicitly_wait(settings.implicit_wait)
    return driver
