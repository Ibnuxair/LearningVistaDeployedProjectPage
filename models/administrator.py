#!/usr/bin/python
""" holds class Administrator"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Administrator(BaseModel, Base):
    """Representation of Adminitrator """
    __tablename__ = 'administrators'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Administrator"""
        super().__init__(*args, **kwargs)
