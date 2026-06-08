#!/usr/bin/env python3
"""
Facade service layer.
"""

from app.models.user import User


class HBnBFacade:
    """
    Facade class.
    """

    def __init__(self):
        """
        Initialize facade.
        """
        self.users = {}

    def create_user(self, data):
        """
        Create user.
        """
        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=data["password"]
        )

        self.users[user.id] = user
        return user
    
    def get_user_by_email(self, email):
        """
        Find user by email.
        """
        for user in self.users.values():
            if user.email == email:
                return user
            
            return None

    def get_user(self, user_id):
        """
        Retrieve user.
        """
        return self.users.get(user_id)

    def get_all_users(self):
        """
        Retrieve all users.
        """
        return list(self.users.values())
    
    


facade = HBnBFacade()