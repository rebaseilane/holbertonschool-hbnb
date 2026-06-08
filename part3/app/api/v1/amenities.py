#!/usr/bin/env python3
"""
Amenity API endpoints (admin only for write operations).
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.roles import admin_required
from app.services.facade import facade

bp = Blueprint("amenities", __name__, url_prefix="/api/v1/amenities")


@bp.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_amenity():
    """
    Admin only: create amenity.
    """
    data = request.get_json()
    amenity = facade.create_amenity(data)

    return jsonify(amenity.to_dict()), 201


@bp.route("/<amenity_id>", methods=["PUT"])
@jwt_required()
@admin_required
def update_amenity(amenity_id):
    """
    Admin only: update amenity.
    """
    data = request.get_json()
    updated = facade.update_amenity(amenity_id, data)

    return jsonify(updated.to_dict()), 200