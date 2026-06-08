#!/usr/bin/env python3
"""
Role-based access control utilities.
"""

from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def admin_required(fn):
    """
    Restrict endpoint to admin users only.

    Args:
        fn (function): Route function

    Returns:
        function: wrapped function
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()

        claims = get_jwt()

        if not claims.get("is_admin"):
            return {"error": "Admin access required"}, 403

        return fn(*args, **kwargs)

    return wrapper