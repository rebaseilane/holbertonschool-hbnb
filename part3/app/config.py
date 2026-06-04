#!/usr/bin/env python3
"""
Configuration module for HBnB application.
Defines application settings for different environments.
"""


class Config:
    """
    Base configuration class.
    """

    DEBUG = True
    TESTING = False
    SECRET_KEY = "hbnb_secret_key"