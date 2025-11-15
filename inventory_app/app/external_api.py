# app/external_api.py
import requests

def fetch_product_data(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    if data.get("status") != 1:
        return None
    product = data["product"]
    return {
        "product_name": product.get("product_name"),
        "brands": product.get("brands"),
        "quantity": product.get("quantity"),
        "categories": product.get("categories"),
        "image_url": product.get("image_url")
    }
