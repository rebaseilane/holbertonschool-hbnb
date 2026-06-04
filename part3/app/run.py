#!/usr/bin/env python3
"""
Entry point for HBnB API.
"""

from app import create_app
from app.config import Config


if __name__ == "__main__":
    app = create_app(Config)
    app.run(debug=True)