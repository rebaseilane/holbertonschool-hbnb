#!/usr/bin/env python3
"""
Reviews API blueprint.
"""

from flask import Blueprint

bp = Blueprint("reviews", __name__, url_prefix="/api/v1/reviews")