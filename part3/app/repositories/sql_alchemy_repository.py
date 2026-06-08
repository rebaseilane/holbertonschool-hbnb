#!/usr/bin/env python3
"""
SQLAlchemy Repository Module.

This module provides a generic repository for database
operations using SQLAlchemy ORM.
"""

from app.extensions import db


class SQLAlchemyRepository:
    """
    Generic repository class for CRUD operations.
    """

    def __init__(self, model):
        """
        Initialize repository with a model.

        Args:
            model (db.Model): SQLAlchemy model.
        """
        self._model = model

    def add(self, entity):
        """
        Add entity to database.
        """
        db.session.add(entity)
        db.session.commit()
        return entity

    def get(self, entity_id):
        """
        Get entity by ID.
        """
        return self._model.query.get(entity_id)

    def get_all(self):
        """
        Get all entities.
        """
        return self._model.query.all()

    def update(self):
        """
        Commit updates.
        """
        db.session.commit()

    def delete(self, entity):
        """
        Delete entity.
        """
        db.session.delete(entity)
        db.session.commit()