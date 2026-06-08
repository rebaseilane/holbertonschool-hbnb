#!/usr/bin/env python3
"""
User model.
"""

import uuid
from app import bcrypt


class User:
    """
    Represents a user.
    """

    def __init__(
        self,
        first_name,
        last_name,
        email,
        password,
        is_admin=False
    ):
        """
        Initialize user.
        """
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        self.hash_password(password)

    def hash_password(self, password):
        """
        Hash password before storing.
        """
        self.password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

    def verify_password(self, password):
        """
        Verify password against hash.
        """
        return bcrypt.check_password_hash(
            self.password,
            password
        )

    def to_dict(self):
        """
        Serialize user without password.
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }