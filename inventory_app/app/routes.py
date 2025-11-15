# app/routes.py
from flask import Flask, jsonify, request
from app.models import InventoryItem
from app.external_api import fetch_product_data

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def list_inventory():
    return jsonify(InventoryItem.list_items()), 200

@app.route("/inventory/<item_id>", methods=["GET"])
def get_inventory(item_id):
    item = InventoryItem.get_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

@app.route("/inventory", methods=["POST"])
def add_inventory():
    data = request.get_json()
    item = InventoryItem.add_item(
        item_id=data["id"],
        name=data["name"],
        quantity=data["quantity"],
        price=data["price"]
    )
    return jsonify(item), 201

@app.route("/inventory/<item_id>", methods=["PUT"])
def update_inventory(item_id):
    data = request.get_json()
    item = InventoryItem.update_item(item_id, **data)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

@app.route("/inventory/<item_id>", methods=["DELETE"])
def delete_inventory(item_id):
    item = InventoryItem.delete_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Deleted"}), 200

@app.route("/product/<barcode>", methods=["GET"])
def get_product(barcode):
    product = fetch_product_data(barcode)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200
