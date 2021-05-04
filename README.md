# bestbuy api playground
pytest framework for rest api

# Task 3 - Automate Best Buy API playground 
Endpoints to be tested:
	/products
	/stores
	/services
	/categories
	/version
	/healthcheck

Successful Tests
- Return each successfully with Status code 200
- Item Scheme is valid
- Item data is available
- Default page limit is correct
- Default skip is correct
- Verify CRUD operations
- Deleted Item cannot be found (404)
- Verify the flow of create an item, get, delete. 

# To run
0. Configure best-buy playground and start server at port 3030.
1. Create virtual env:
	python3 -m venv rest

	REQUIREMENTS:
	attrs==20.3.0
	certifi==2020.12.5
	chardet==4.0.0
	idna==2.10
	iniconfig==1.1.1
	packaging==20.9
	pluggy==0.13.1
	py==1.10.0
	pyparsing==2.4.7
	pytest==6.2.3
	requests==2.25.1
	toml==0.10.2
	urllib3==1.26.4
2. source rest/bin/activate
3. run by command:
	pytest

4. Sample output:

================================================================ 15 passed in 11.82s =================================================================
(rest) Denems-MacbookAir:rest dorhun$ pytest -v
================================================================ test session starts =================================================================
platform darwin -- Python 3.9.0, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /Users/dorhun/Documents/GitHub/bestbuyapi/rest/bin/python3
cachedir: .pytest_cache
rootdir: /Users/dorhun/Documents/GitHub/bestbuyapi/rest
collected 15 items                                                                                                                                   

test_restapi.py::test_request_status_code_equals_200[/healthcheck] PASSED                                                                      [  6%]
test_restapi.py::test_request_status_code_equals_200[/categories] PASSED                                                                       [ 13%]
test_restapi.py::test_request_status_code_equals_200[/products] PASSED                                                                         [ 20%]
test_restapi.py::test_request_status_code_equals_200[/stores] PASSED                                                                           [ 26%]
test_restapi.py::test_request_status_code_equals_200[/services] PASSED                                                                         [ 33%]
test_restapi.py::test_request_status_code_equals_200[/version] PASSED                                                                          [ 40%]
test_restapi.py::test_request_content_type_equals_app_json[/healthcheck] PASSED                                                                [ 46%]
test_restapi.py::test_request_content_type_equals_app_json[/categories] PASSED                                                                 [ 53%]
test_restapi.py::test_request_content_type_equals_app_json[/products] PASSED                                                                   [ 60%]
test_restapi.py::test_request_content_type_equals_app_json[/stores] PASSED                                                                     [ 66%]
test_restapi.py::test_request_content_type_equals_app_json[/services] PASSED                                                                   [ 73%]
test_restapi.py::test_request_content_type_equals_app_json[/version] PASSED                                                                    [ 80%]
test_restapi.py::test_for_stores_with_limit PASSED                                                                                             [ 86%]
test_restapi.py::test_posting_new_product_with_201_status PASSED                                                                               [ 93%]
test_restapi.py::test_product_post_delete_get_flow PASSED                                                                                      [100%]

================================================================= 15 passed in 1.63s =================================================================