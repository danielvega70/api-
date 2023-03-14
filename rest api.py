from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Define a list to store recruiter data
recruiters = []

# Define a route for creating a new recruiter
@app.route('/recruiters', methods=['POST'])
def create_recruiter():
    # Get the recruiter data from the request
    data = request.get_json()

    # Add the recruiter to the list
    recruiters.append(data)

    # Return a success message
    return jsonify({'message': 'Recruiter created successfully!'}), 201

# Define a route for getting all recruiters
@app.route('/recruiters', methods=['GET'])
def get_recruiters():
    # Return the list of recruiters as JSON
    return jsonify({'recruiters': recruiters}), 200

if __name__ == '__main__':
    app.run(debug=True)
