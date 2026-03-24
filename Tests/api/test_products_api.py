import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_api_products_list(api_client):
    response = api_client.get("products")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
