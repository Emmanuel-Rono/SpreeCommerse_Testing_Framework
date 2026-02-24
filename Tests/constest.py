import pytest
from Configuration.driver_factory import get_driver

@pytest.fixture
def driver():
    driver_instance = get_driver()
    yield driver_instance
    driver_instance.quit()