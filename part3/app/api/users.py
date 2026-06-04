#!/usr/bin/env python3
"""
Users API blueprint.
"""

from flask import Blueprint

bp = Blueprint("users", __name__, url_prefix="/api/v1/users")