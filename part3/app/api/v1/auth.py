#!/usr/bin/env python3
"""
Authentication endpoints.
"""

from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from app.services.facade import facade

@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    """
    Protected endpoint.
    """
    current_user = get_jwt_identity()

    return jsonify({
        "message": "Access granted",
        "user_id": current_user
    }), 200

bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/v1/auth"
)