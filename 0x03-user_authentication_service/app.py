#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Register a user"""
    if request and request.is_json:
        data = request.json()

        email = data.get('email')
        password = data.get('password')

        try:
            user = AUTH.register_user(email, password)
            return jsonify({
                "email": "{}".format(user.email),
                "message": "user created"}
                ), 201
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
