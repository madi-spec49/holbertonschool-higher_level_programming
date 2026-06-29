#!/usr/bin/python3
"""Simple API using Flask with in-memory storage"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/')
def home():
    """Handle root URL"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return API status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user object for given username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the API"""
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is present
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to storage
    users[username] = data

    # Return confirmation
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=False
