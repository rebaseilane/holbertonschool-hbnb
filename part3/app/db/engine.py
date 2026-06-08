#!/usr/bin/env python3
"""
SQLAlchemy engine configuration.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///hbnb.db", echo=False)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)