#!/usr/bin/env python3
"""
User repository using SQLAlchemy.
"""

from app.repositories.sql_repository import SQLAlchemyRepository
from app.models.user import User


class UserRepository(SQLAlchemyRepository):
    """
    User-specific repository.
    """

    def __init__(self):
        """
        Initialize user repository.
        """
        super().__init__(User)

    def get_by_email(self, email):
        """
        Find user by email.
        """
        return self._session.query(User).filter_by(email=email).first()