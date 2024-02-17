#!/usr/bin/python3
""" holds class Department"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Department(BaseModel, Base):
    """Representation of Department"""
    __tablename__ = 'departments'
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))

    teachers = relationship('Teacher', back_populates='department')
    students = relationship('Student', back_populates='department')

    def __init__(self, *args, **kwargs):
        """initializes Department"""
        super().__init__(*args, **kwargs)
