from app.server.interface import SystemInterface
from flask import Flask, session, jsonify, request, redirect, url_for

app = Flask(__name__)

app.secret_key = 'your_super_secret_key'

iface = SystemInterface()

@app.route('/')
def home_menu():
    """
    Route to display the home menu when the server starts.

    Returns:
    str: A redirect to the login page if the user is not logged in, otherwise a JSON response.
    """
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    iface.main_menu()
    return jsonify({"message": "Displayed the home menu"}), 200

@app.route('/login', methods=['POST'])
def login():
    """
    Route to log in a user.

    Returns:
    dict: A dictionary containing a message or an error.
    int: A status code.
    """
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Check if data is being received

        username = data.get('username')
        password = data.get('password')

        print(f"Username: {username}, Password: {password}")  # Verify the username and password are correctly extracted

        if iface.login_logic.verify_user(username, password):
            session['username'] = username
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        print(f"Error occurred: {e}")  # Print the actual error message
        return jsonify({"error": "Internal server error"}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Route to log out a user.

    Returns:
    dict: A dictionary containing a message.
    int: A status code.
    """
    # Clear the session data, logging out the user
    session.clear()
    
    return jsonify({"message": "Logout successful"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    """
    Route to get all users.

    Returns:
    list: A list of users.
    """
    users = iface.get_users()
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def add_user():
    """
    Route to add a new user.

    Returns:
    dict: A dictionary containing a message or an error.
    int: A status code.
    """
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    fullname = data.get('fullname')
    interests = data.get('interests', [])
    location = data.get('location', '')
    age = data.get('age', 0)
    bio = data.get('bio', '')

    new_user = iface.add_user(username, password, fullname, interests, location, age, bio)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
