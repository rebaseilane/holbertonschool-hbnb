#!/usr/bin/env python3
"""
Place model.
"""

from app.extensions import db
from app.models.base_model import BaseModel


class Place(BaseModel):
    """
    Place entity.
    """

    __tablename__ = "places"

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)