#!/usr/bin/env python3
"""
Authentication utility functions for JWT protection.
"""

from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify


def jwt_required_user():
    """
    Validate JWT token and return user ID.

    Returns:
        int: user_id from token
    """
    verify_jwt_in_request()
    return get_jwt_identity()


def unauthorized():
    """
    Return unauthorized response.

    Returns:
        Response: JSON 401 error
    """
    return jsonify({"error": "Unauthorized"}), 401