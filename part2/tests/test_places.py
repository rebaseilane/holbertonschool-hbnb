import pytest
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository


def test_create_place():
    repo = InMemoryRepository()
    facade = HBnBFacade(repo)

    place = facade.create_place({
        "title": "Villa",
        "description": "Nice place",
        "price": 100,
        "latitude": 10,
        "longitude": 20
    })

    assert place.title == "Villa"
    assert place.price == 100