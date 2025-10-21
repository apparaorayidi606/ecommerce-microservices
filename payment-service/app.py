from flask import Flask, jsonify, request

app = Flask(__name__)

payments = []

@app.route("/pay", methods=["POST"])
def make_payment():
    data = request.json
    payment = {"order_id": data["order_id"], "amount": data["amount"], "status": "success"}
    payments.append(payment)
    return jsonify(payment), 201

@app.route("/payments", methods=["GET"])
def get_payments():
    return jsonify(payments)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
