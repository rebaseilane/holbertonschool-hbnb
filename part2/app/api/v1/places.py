"""
Place endpoints.
"""

from flask import Blueprint, request, jsonify
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository

bp = Blueprint("places", __name__, url_prefix="/api/v1/places")

repo = InMemoryRepository()
facade = HBnBFacade(repo)


@bp.route("/", methods=["POST"])
def create_place():
    data = request.json

    if data.get("price", 0) <= 0:
        return {"error": "Invalid price"}, 400

    if not (-90 <= data.get("latitude", 0) <= 90):
        return {"error": "Invalid latitude"}, 400

    if not (-180 <= data.get("longitude", 0) <= 180):
        return {"error": "Invalid longitude"}, 400

    place = facade.create_place(data)
    return jsonify(place.to_dict()), 201


@bp.route("/", methods=["GET"])
def get_places():
    places = facade.get_places()
    return jsonify([p.to_dict() for p in places]), 200


@bp.route("/<place_id>", methods=["GET"])
def get_place(place_id):
    place = facade.get_place(place_id)
    if not place:
        return {"error": "Not found"}, 404
    return jsonify(place.to_dict()), 200


@bp.route("/<place_id>", methods=["PUT"])
def update_place(place_id):
    data = request.json
    place = facade.update_place(place_id, data)
    if not place:
        return {"error": "Not found"}, 404
    return jsonify(place.to_dict()), 200