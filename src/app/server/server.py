from src.app.server.interface import *

from flask import Flask, jsonify, request


# This is our Flask application. In this project, we will keep this file relatively empty
#  and move logic to the interface class or other classes
app = Flask(__name__)

# This is an example data structure that is returned as a part of the /incomes GET call
#   and appended to as a part of the POST operation
incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

# This is the actual interface class in which we will write Flask-independent code
iface = SystemInterface()

# A basic example for returning data as json
@app.route('/incomes', methods=['GET'])
def get_incomes():
    return jsonify(incomes)

# A basic example for appending data to a data structure (NOTE: There are no checks at all here, that's insecure!)
@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 201

# This route actually calls an operation in our interface object.
@app.route('/none', methods=['GET'])
def get_none():
    return jsonify(iface.an_operation_without_params())