"""
Amenity endpoints.
"""

from flask import Blueprint, request, jsonify
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository

bp = Blueprint("amenities", __name__, url_prefix="/api/v1/amenities")

repo = InMemoryRepository()
facade = HBnBFacade(repo)


@bp.route("/", methods=["POST"])
def create_amenity():
    data = request.json
    amenity = facade.create_amenity(data)
    return jsonify(amenity.to_dict()), 201


@bp.route("/", methods=["GET"])
def get_amenities():
    amenities = facade.get_amenities()
    return jsonify([a.to_dict() for a in amenities]), 200


@bp.route("/<amenity_id>", methods=["GET"])
def get_amenity(amenity_id):
    amenity = facade.get_amenity(amenity_id)
    if not amenity:
        return {"error": "Not found"}, 404
    return jsonify(amenity.to_dict()), 200


@bp.route("/<amenity_id>", methods=["PUT"])
def update_amenity(amenity_id):
    data = request.json
    amenity = facade.update_amenity(amenity_id, data)
    if not amenity:
        return {"error": "Not found"}, 404
    return jsonify(amenity.to_dict()), 200