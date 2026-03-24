import os
from datetime import datetime

import pytest

from API.client import ApiClient
from Core.config import load_settings
from Core.driver import get_driver
from Core.logger import configure_logging
from Core.paths import ensure_dir


@pytest.fixture(scope="session", autouse=True)
def _configure_logging():
    configure_logging()


@pytest.fixture(scope="session")
def settings():
    return load_settings()


@pytest.fixture(scope="session")
def base_url(settings):
    return settings.base_url


@pytest.fixture(scope="session")
def api_client(settings):
    return ApiClient(settings)


@pytest.fixture
def driver(settings):
    driver_instance = get_driver(settings)
    yield driver_instance
    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            settings = item.funcargs.get("settings") or load_settings()
            screenshots_dir = ensure_dir(settings.screenshots_dir)
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            driver.save_screenshot(str(screenshots_dir / filename))
