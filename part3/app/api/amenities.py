#!/usr/bin/env python3
"""
Amenities API blueprint.
"""

from flask import Blueprint

bp = Blueprint("amenities", __name__, url_prefix="/api/v1/amenities")