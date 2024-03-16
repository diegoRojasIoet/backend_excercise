from http import HTTPStatus

from fastapi.testclient import TestClient


def test__should_return_a_list_of_products(api_client: TestClient):
    # Take a look at this test, what do you think could be improved?
    response = api_client.get("/products/")
    products = response.json().get("products")

    assert response.status_code == HTTPStatus.OK
    assert products
