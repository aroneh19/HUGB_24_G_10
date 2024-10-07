from app.server.interface import SystemInterface
from flask import Flask, session, jsonify, request, redirect, url_for

app = Flask(__name__)

iface = SystemInterface()

@app.route('/')
def home_menu():
    """Route to display the home menu when the server starts."""
    iface.main_menu()
    return jsonify({"message": "Displayed the home menu"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if iface.verify_user(username, password):
        return jsonify({"message": "Login successful"}), 200
    else: 
        return jsonify({"error": "invalid username or password"}), 401
    
def login_user(self, post_data):
        """Helper method to log in a user via a POST request."""
        return self.app.post("/login", json=post_data)

@app.route('/logout')
def logout():
    # Clear the session data, logging out the user
    session.clear()
    
    return redirect(url_for('login'))

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