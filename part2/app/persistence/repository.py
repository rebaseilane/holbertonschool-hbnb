"""
Abstract repository interface.
Defines contract for persistence layer.
"""

from abc import ABC, abstractmethod


class Repository(ABC):
    """
    Repository interface (contract).
    """

    @abstractmethod
    def save(self, entity_type, obj):
        pass

    @abstractmethod
    def get(self, entity_type, obj_id):
        pass

    @abstractmethod
    def get_all(self, entity_type):
        pass

    @abstractmethod
    def update(self, entity_type, obj_id, data):
        pass

    @abstractmethod
    def delete(self, entity_type, obj_id):
        pass