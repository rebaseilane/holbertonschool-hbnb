#!/usr/bin/env python3
"""
Base model for all entities.
"""

from datetime import datetime
from app.extensions import db


class BaseModel(db.Model):
    """
    Base model with id and timestamps.
    """

    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )