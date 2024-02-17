#!/usr/bin/python
""" holds class Assignment"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Float


class Assignment(BaseModel, Base):
    """Representation of Assignment"""
    __tablename__ = 'assignments'
    title = Column(String(128), nullable=False)
    description = Column(String(256))
    due_date = Column(DateTime, nullable=False)
    submission_date = Column(DateTime, nullable=False)
    marks_obtained = Column(Float)
    student_id = Column(String(60),
                        ForeignKey('students.id', onupdate='CASCADE',
                                   ondelete='CASCADE'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes Assignment"""
        super().__init__(*args, **kwargs)
