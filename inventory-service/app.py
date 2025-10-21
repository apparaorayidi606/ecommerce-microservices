from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = {
    1: 10,  # product_id: quantity
    2: 25,
    3: 50
}

@app.route("/inventory/<int:product_id>", methods=["GET"])
def get_stock(product_id):
    stock = inventory.get(product_id, 0)
    return jsonify({"product_id": product_id, "stock": stock})

@app.route("/inventory/update", methods=["POST"])
def update_stock():
    data = request.json
    inventory[data["product_id"]] = data["quantity"]
    return jsonify({"message": "Stock updated"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
