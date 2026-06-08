import pytest
from app.api.facade import HBnBFacade
from app.persistence.memory_repository import InMemoryRepository


def test_create_user():
    repo = InMemoryRepository()
    facade = HBnBFacade(repo)

    user = facade.create_user({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@test.com",
        "password": "123456"
    })

    assert user.first_name == "John"
    assert user.email == "john@test.com"