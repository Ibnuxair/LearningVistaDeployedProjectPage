#!/usr/bin/python3
""" holds class Result"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Float, ForeignKey


class Result(BaseModel, Base):
    """Representation of Result"""
    __tablename__ = 'course_results'
    exam_date = Column(DateTime, nullable=False)
    marks_obtained = Column(Float, nullable=False)
    pass_marks = Column(Float, nullable=False)
    course_id = Column(String(60),
                       ForeignKey('courses.id'), primary_key=True)
    student_id = Column(String(60),
                        ForeignKey('students.id'), primary_key=True)

    def __init__(self, *args, **kwargs):
        """initializes Result"""
        super().__init__(*args, **kwargs)
