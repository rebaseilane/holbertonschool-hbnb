"""
Review model
Represents user reviews on places.
"""

from app.models.base_model import BaseModel


class Review(BaseModel):
    """
    Review entity.
    """

    def __init__(self, rating, comment, user_id, place_id):
        super().__init__()
        self.rating = rating
        self.comment = comment
        self.user_id = user_id
        self.place_id = place_id

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "comment": self.comment,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }