import time
import pytest


@pytest.mark.perf
def test_api_products_response_time(api_client):
    start = time.perf_counter()
    response = api_client.get("products")
    elapsed_ms = (time.perf_counter() - start) * 1000
    assert response.status_code == 200
    assert elapsed_ms < 1500, f"Response too slow: {elapsed_ms:.0f}ms"
