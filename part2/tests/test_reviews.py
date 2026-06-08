import pytest
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository


def test_create_review():
    repo = InMemoryRepository()
    facade = HBnBFacade(repo)

    review = facade.create_review({
        "rating": 5,
        "comment": "Great!",
        "user_id": "1",
        "place_id": "1"
    })

    assert review.rating == 5
    assert review.comment == "Great!"