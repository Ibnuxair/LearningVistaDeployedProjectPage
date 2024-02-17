#!/usr/bin/python
""" holds class Course"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Course(BaseModel, Base):
    """Representation of Course"""
    __tablename__ = 'courses'
    title = Column(String(128), nullable=False)
    code = Column(String(128), nullable=False)
    credit_unit = Column(Integer, nullable=False)
    description = Column(String(256), nullable=True)
    teacher_id = Column(String(60), ForeignKey('teachers.id'), nullable=False)
    student_id = Column(String(60), ForeignKey('students.id'), nullable=False)

    resources = relationship('Resource', backref='course',
                             cascade='all, delete, delete-orphan')
    results = relationship('Result', backref='course')

    def __init__(self, *args, **kwargs):
        """initializes Course"""
        super().__init__(*args, **kwargs)
