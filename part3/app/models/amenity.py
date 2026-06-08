#!/usr/bin/env python3
"""
Amenity model.
"""

from app.extensions import db
from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity entity.
    """

    __tablename__ = "amenities"

    name = db.Column(db.String(100), nullable=False)