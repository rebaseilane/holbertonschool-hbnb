#!/usr/bin/env python3
"""
Places API blueprint.
"""

from flask import Blueprint

bp = Blueprint("places", __name__, url_prefix="/api/v1/places")