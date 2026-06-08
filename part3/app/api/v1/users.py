#!/usr/bin/env python3
"""
User endpoints.
"""

from flask import Blueprint
from flask import request
from flask import jsonify

from app.services.facade import facade

bp = Blueprint(
    "users",
    __name__,
    url_prefix="/api/v1/users"
)


@bp.route("/", methods=["POST"])
def create_user():
    """
    Register a new user.
    """
    data = request.get_json()

    required_fields = [
        "first_name",
        "last_name",
        "email",
        "password"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    user = facade.create_user(data)

    return jsonify(
        user.to_dict()
    ), 201


@bp.route("/", methods=["GET"])
def get_users():
    """
    Get all users.
    """
    users = [
        user.to_dict()
        for user in facade.get_all_users()
    ]

    return jsonify(users), 200

@bp.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and generate JWT.
    """
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email and password required"
        }), 400

    user = facade.get_user_by_email(email)

    if user is None:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    if not user.verify_password(password):
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    token = create_access_token(
        identity=user.id,
        additional_claims={
            "email": user.email,
            "is_admin": user.is_admin
        }
    )

    return jsonify({
        "access_token": token
    }), 200


@bp.route("/<user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    """
    Update user profile (no email/password changes allowed).
    """
    current_user = get_jwt_identity()

    if current_user != user_id:
        return jsonify({"error": "Forbidden"}), 403

    data = request.get_json()

    # block sensitive updates
    data.pop("email", None)
    data.pop("password", None)

    user = facade.update_user(user_id, data)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200