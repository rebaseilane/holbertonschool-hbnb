import pytest
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository


def test_create_amenity():
    repo = InMemoryRepository()
    facade = HBnBFacade(repo)

    amenity = facade.create_amenity({
        "name": "WiFi",
        "description": "Fast internet"
    })

    assert amenity.name == "WiFi"