#!/usr/bin/env python3
"""
Place API endpoints with ownership protection.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import facade

bp = Blueprint("places", __name__, url_prefix="/api/v1/places")


@bp.route("/", methods=["POST"])
@jwt_required()
def create_place():
    """
    Create a new place (authenticated users only).
    """
    data = request.get_json()
    data["owner_id"] = get_jwt_identity()

    place = facade.create_place(data)
    return jsonify(place.to_dict()), 201


@bp.route("/<place_id>", methods=["PUT"])
@jwt_required()
def update_place(place_id):
    """
    Update place (only owner allowed).
    """
    user_id = get_jwt_identity()
    place = facade.get_place(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404

    if place.owner_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    data = request.get_json()
    updated = facade.update_place(place_id, data)

    return jsonify(updated.to_dict()), 200




@bp.route("/<place_id>", methods=["DELETE"])
@jwt_required()
def delete_place(place_id):
    """
    Delete place (only owner allowed).
    """
    user_id = get_jwt_identity()
    place = facade.get_place(place_id)

    if not place:
        return jsonify({"error": "Place not found"}), 404

    if place.owner_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    facade.delete_place(place_id)

    return jsonify({"message": "Deleted"}), 200