#!/usr/bin/env python3
"""
Application factory.
"""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from app.config import Config

bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class=Config):
    """
    Create Flask application.
    """
    app = Flask(__name__)

    app.config.from_object(config_class)

    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.api.v1.users import bp as users_bp
    from app.api.v1.auth import bp as auth_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)

    return app