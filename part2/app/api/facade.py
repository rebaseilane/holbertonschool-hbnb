"""
Facade pattern implementation
Acts as single entry point between API and business logic.
"""

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    """
    Facade managing all business operations.
    """

    def __init__(self, repository):
        self.repo = repository

    # ---------------- USERS ----------------
    def create_user(self, data):
        user = User(**data)
        return self.repo.save("users", user)

    def get_users(self):
        return self.repo.get_all("users")

    def get_user(self, user_id):
        return self.repo.get("users", user_id)

    def update_user(self, user_id, data):
        return self.repo.update("users", user_id, data)

    # ---------------- PLACES ----------------
    def create_place(self, data):
        place = Place(**data)
        return self.repo.save("places", place)

    def get_places(self):
        return self.repo.get_all("places")

    def get_place(self, place_id):
        return self.repo.get("places", place_id)

    def update_place(self, place_id, data):
        return self.repo.update("places", place_id, data)

    # ---------------- REVIEWS ----------------
    def create_review(self, data):
        review = Review(**data)
        return self.repo.save("reviews", review)

    def get_reviews(self):
        return self.repo.get_all("reviews")

    def get_reviews_by_place(self, place_id):
        reviews = self.repo.get_all("reviews")
        return [r for r in reviews if r.place_id == place_id]

    def delete_review(self, review_id):
        return self.repo.delete("reviews", review_id)

    # ---------------- AMENITIES ----------------
    def create_amenity(self, data):
        amenity = Amenity(**data)
        return self.repo.save("amenities", amenity)

    def get_amenities(self):
        return self.repo.get_all("amenities")

    def get_amenity(self, amenity_id):
        return self.repo.get("amenities", amenity_id)

    def update_amenity(self, amenity_id, data):
        return self.repo.update("amenities", amenity_id, data)