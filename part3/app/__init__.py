#!/usr/bin/env python3
"""
Application factory for HBnB API.

Creates and configures the Flask application using
the Application Factory pattern.
"""

from flask import Flask
from app.api import users, places, reviews, amenities


def create_app(config_class=None):
    """
    Create and configure Flask application.

    Args:
        config_class (class): Configuration class to load into app.

    Returns:
        Flask: Configured Flask application instance.
    """

    app = Flask(__name__)

    # Default config fallback
    if config_class is None:
        from app.config import Config
        config_class = Config

    # Load configuration into Flask
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(users.bp)
    app.register_blueprint(places.bp)
    app.register_blueprint(reviews.bp)
    app.register_blueprint(amenities.bp)

    return app