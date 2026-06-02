"""
BaseModel module
Provides common attributes for all entities.
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel defines shared attributes for all models.
    """

    def __init__(self):
        """
        Initialize base attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Update timestamp when saving.
        """
        self.updated_at = datetime.utcnow()

    def update(self, data):
        """
        Update object attributes dynamically.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()