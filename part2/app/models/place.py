"""
Place model
Represents property listings.
"""

from app.models.base_model import BaseModel


class Place(BaseModel):
    """
    Place entity.
    """

    def __init__(self, title, description, price, latitude, longitude, owner_id=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity_id):
        """
        Add an amenity to place.
        """
        if amenity_id not in self.amenities:
            self.amenities.append(amenity_id)

    def remove_amenity(self, amenity_id):
        """
        Remove an amenity.
        """
        if amenity_id in self.amenities:
            self.amenities.remove(amenity_id)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": self.amenities,
            "reviews": self.reviews,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }