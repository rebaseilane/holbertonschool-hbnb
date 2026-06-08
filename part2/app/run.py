"""
Entry point for HBnB API.
"""

from flask import Flask
from app.api.v1.users import bp as users_bp
from app.api.v1.places import bp as places_bp
from app.api.v1.reviews import bp as reviews_bp
from app.api.v1.amenities import bp as amenities_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(amenities_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)