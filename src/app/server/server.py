from src.app.server.interface import *
from flask import Flask, jsonify, request

app = Flask(__name__)

iface = SystemInterface()

@app.route('/users', methods=['GET'])
def get_users():
    users = iface.get_users()
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    # Vantar að bæta við parameturum
    new_user = iface.add_user()
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)