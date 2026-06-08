#!/usr/bin/env python3
"""
Generic SQLAlchemy repository.
"""

from app.db.engine import SessionLocal


class SQLAlchemyRepository:
    """
    Generic repository for SQLAlchemy operations.
    """

    def __init__(self, model):
        """
        Initialize repository.

        Args:
            model (class): SQLAlchemy model
        """
        self._model = model
        self._session = SessionLocal()

    def add(self, obj):
        """
        Add object to DB.
        """
        self._session.add(obj)
        self._session.commit()
        self._session.refresh(obj)
        return obj

    def get(self, obj_id):
        """
        Get object by ID.
        """
        return self._session.query(self._model).get(obj_id)

    def get_all(self):
        """
        Get all objects.
        """
        return self._session.query(self._model).all()

    def delete(self, obj):
        """
        Delete object.
        """
        self._session.delete(obj)
        self._session.commit()