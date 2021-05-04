# Base url running the BestBuy Api
BASE_URL = "http://localhost:3030"

# Endpoints
ENDPOINTS = ("/healthcheck", "/categories", "/products", "/stores", "/services", "/version")

# sample product for post
PRODUCT_DATA = {
    "name": "yamaha",
    "type": "keyboard",
    "description": "fullsize instrument",
    "model": "mo8",
    "upc": "1000$"
    }