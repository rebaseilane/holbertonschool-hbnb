#!/usr/bin/env python3
"""
Base class for all SQLAlchemy models.
"""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid


class Base(DeclarativeBase):
    """
    Base declarative class.
    """
    pass


class BaseModel(Base):
    """
    Base model with common fields.
    """

    __abstract__ = True

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)