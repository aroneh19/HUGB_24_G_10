from app.server.interface import SystemInterface
from flask import Flask, jsonify, request

app = Flask(__name__)

iface = SystemInterface()

@app.route('/')
def home_menu():
    """Route to display the home menu when the server starts."""
    iface.main_menu()
    return jsonify({"message": "Displayed the home menu"}), 200


@app.route('/users', methods=['GET'])
def get_users():
    users = iface.get_users()
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    bio = data.get('bio', '')
    interests = data.get('interests', [])
    location = data.get('location', '')

    new_user = iface.add_user(username, password, name, bio, interests, location)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)