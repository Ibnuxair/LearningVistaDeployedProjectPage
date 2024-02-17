#!/usr/bin/python3
""" holds class Teacher"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


# Association Table
teacher_course = Table('teacher_course', Base.metadata,
                       Column('teacher_id', String(60),
                              ForeignKey('teachers.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column('course_id', String(60),
                              ForeignKey('courses.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))


class Teacher(BaseModel, Base):
    """Representation of Teacher"""
    __tablename__ = 'teachers'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    subject_specialization = Column(String(128), nullable=True)
    department = relationship('Department', back_populates='teachers')
    courses_taking = relationship('Course', secondary=teacher_course,
                                  viewonly=False)
    user_id = Column(String(60),
                     ForeignKey('users.id', onupdate='CASCADE',
                                ondelete='CASCADE'), nullable=False)
    department_id = Column(String(60),
                           ForeignKey('departments.id', onupdate='CASCADE',
                                      ondelete='CASCADE'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Teacher"""
        super().__init__(*args, **kwargs)
