"""
Amenity model
Represents place amenities.
"""

from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity entity.
    """

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }