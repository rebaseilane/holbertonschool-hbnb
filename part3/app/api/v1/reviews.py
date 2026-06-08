#!/usr/bin/env python3
"""
Review API endpoints with business rules.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import facade

bp = Blueprint("reviews", __name__, url_prefix="/api/v1/reviews")


@bp.route("/", methods=["POST"])
@jwt_required()
def create_review():
    """
    Create review with restrictions:
    - Cannot review own place
    - Cannot review same place twice
    """
    user_id = get_jwt_identity()
    data = request.get_json()

    place = facade.get_place(data["place_id"])

    if place.owner_id == user_id:
        return jsonify({"error": "Cannot review your own place"}), 400

    existing = facade.get_review_by_user_and_place(
        user_id,
        data["place_id"]
    )

    if existing:
        return jsonify({"error": "Already reviewed"}), 400

    data["user_id"] = user_id
    review = facade.create_review(data)

    return jsonify(review.to_dict()), 201


@bp.route("/<review_id>", methods=["PUT"])
@jwt_required()
def update_review(review_id):
    """
    Only review owner can update.
    """
    user_id = get_jwt_identity()
    review = facade.get_review(review_id)

    if review.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    data = request.get_json()
    updated = facade.update_review(review_id, data)

    return jsonify(updated.to_dict()), 200


@bp.route("/<review_id>", methods=["DELETE"])
@jwt_required()
def delete_review(review_id):
    """
    Only review owner can delete.
    """
    user_id = get_jwt_identity()
    review = facade.get_review(review_id)

    if review.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    facade.delete_review(review_id)

    return jsonify({"message": "Deleted"}), 200