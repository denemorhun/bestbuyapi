from constants import BASE_URL, ENDPOINTS, PRODUCT_DATA
import requests, pytest, time, json

# return base url
@pytest.fixture
def base_url():
    return BASE_URL

# test the successful 200 status of GET from each URL
@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_request_status_code_equals_200(endpoint):
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200

# test response header content type to be application/json
@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_request_content_type_equals_app_json(endpoint):
    response = requests.get(BASE_URL + endpoint)
    assert "application/json" in response.headers["Content-Type"]

#  verify limiting the number of stores (0 should return none)
@pytest.mark.parametrize("limit", (0, 3, 5, 10))
def test_for_stores_with_limit(limit):
    uri = BASE_URL + "/stores"

    uri = f"{BASE_URL}/stores?$limit={limit}" 
    payload, headers = {}, {}

    response = requests.request("GET", uri, headers=headers, data = payload)
    response_body = response.json()

    assert len(response_body["data"]) == limit

# test filter by Minnetonka
def test_for_stores_with_limit():
    uri = BASE_URL + "/stores"

    payload = {}
    headers= {}

    response = requests.request("GET", uri, headers=headers, data = payload)
    response_body = response.json()

    assert response_body["data"][0]["name"] == "Minnetonka"


def test_posting_new_product_with_201_status():
    uri = BASE_URL + "/products"

    payload = {
    "name": "yamaha",
    "type": "keyboard",
    "description": "fullsize instrument",
    "model": "mo8",
    "upc": "1000$"
    }

    response = requests.request("POST", uri, json = payload)

    assert response.status_code == 201

# POST an item, verify 201, GET the Item, verify 200, DELETE the item, verify 200, Get the ITEM, verify 401

def test_product_post_delete_get_flow():
    uri = BASE_URL + "/products"

    # perform post of the test yamaha product
    response = requests.request("POST", uri, json = PRODUCT_DATA)
    assert response.status_code == 201

    # Get product ID 
    product = response.json()

    assert product["name"] == "yamaha"
    assert product["type"] == "keyboard"

    # get productID for deletion later
    productID = product["id"]
    print(productID)

    # perform GET on this product ID
    response = requests.request("GET", uri, params={"id":productID})
    assert response.status_code == 200

    # perform DELETE on this product ID
    response = requests.request("DELETE", uri, params={"id":productID})
    assert response.status_code == 200

    time.sleep(10)

    # reperform DELETE on this product ID
    response = requests.request("DELETE", uri, params={"id":productID})
    assert response.status_code == 400

    # reperform GET and expect 404 error
    response = requests.request("GET", uri, params={"id":productID})
    assert response.status_code == 404




test_product_post_delete_get_flow()


# Additional Tests

# verify skipping number of stores, products, being listed
# test filter by apple stores
# verify time stamp of post
# Select Item by ID etc etc