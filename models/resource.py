#!/usr/bin/python
""" holds class Resource"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, Text


class Resource(BaseModel, Base):
    """Representation of Resource"""
    __tablename__ = 'resources'
    title = Column(String(128), nullable=False)
    uploaded_date = Column(DateTime, nullable=False)
    content = Column(Text, nullable=True)
    course_id = Column(String(60),
                       ForeignKey('courses.id', onupdate='CASCADE',
                                  ondelete='CASCADE'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Resource"""
        super().__init__(*args, **kwargs)
