"""
User endpoints.
"""

from flask import Blueprint, request, jsonify
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository

bp = Blueprint("users", __name__, url_prefix="/api/v1/users")

repo = InMemoryRepository()
facade = HBnBFacade(repo)


@bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    user = facade.create_user(data)
    return jsonify(user.to_dict()), 201


@bp.route("/", methods=["GET"])
def get_users():
    users = facade.get_users()
    return jsonify([u.to_dict() for u in users]), 200


@bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = facade.get_user(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return jsonify(user.to_dict()), 200


@bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = facade.update_user(user_id, data)
    if not user:
        return {"error": "User not found"}, 404
    return jsonify(user.to_dict()), 200