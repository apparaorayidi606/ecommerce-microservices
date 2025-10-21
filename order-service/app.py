from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

orders = []

@app.route("/orders", methods=["POST"])
def create_order():
    order = request.json
    product_resp = requests.get(f"http://product-service:5001/products/{order['product_id']}")
    if product_resp.status_code != 200:
        return jsonify({"error": "Invalid product"}), 400
    product = product_resp.json()
    total = product["price"] * order["quantity"]
    order["total"] = total
    orders.append(order)
    return jsonify(order), 201

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
