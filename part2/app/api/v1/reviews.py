"""
Review endpoints.
"""

from flask import Blueprint, request, jsonify
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository

bp = Blueprint("reviews", __name__, url_prefix="/api/v1/reviews")

repo = InMemoryRepository()
facade = HBnBFacade(repo)


@bp.route("/", methods=["POST"])
def create_review():
    data = request.json

    if not (1 <= data.get("rating", 0) <= 5):
        return {"error": "Invalid rating"}, 400

    review = facade.create_review(data)
    return jsonify(review.to_dict()), 201


@bp.route("/", methods=["GET"])
def get_reviews():
    reviews = facade.get_reviews()
    return jsonify([r.to_dict() for r in reviews]), 200


@bp.route("/place/<place_id>", methods=["GET"])
def get_reviews_by_place(place_id):
    reviews = facade.get_reviews_by_place(place_id)
    return jsonify([r.to_dict() for r in reviews]), 200


@bp.route("/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    deleted = facade.delete_review(review_id)
    if not deleted:
        return {"error": "Not found"}, 404
    return {"message": "Deleted"}, 200