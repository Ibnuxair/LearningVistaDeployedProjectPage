#!/usr/bin/python
""" holds class Student"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Table, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


# Association Table for student_course relationship
student_course = Table('student_course', Base.metadata,
                       Column('student_id', String(60),
                              ForeignKey('students.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True),
                       Column('course_id', String(60),
                              ForeignKey('courses.id', onupdate='CASCADE',
                                         ondelete='CASCADE'),
                              primary_key=True))

# New association table for student-assignment relationship
student_assignment = Table('student_assignment', Base.metadata,
                           Column('student_id', String(60),
                                  ForeignKey('students.id', onupdate='CASCADE',
                                             ondelete='CASCADE'),
                                  primary_key=True),
                           Column('assignment_id', String(60),
                                  ForeignKey('assignments.id',
                                             onupdate='CASCADE',
                                             ondelete='CASCADE'),
                                  primary_key=True))


class Student(BaseModel, Base):
    """Representation of Student"""
    __tablename__ = 'students'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    midle_name = Column(String(128))
    registration_number = Column(String(128), nullable=True, unique=True)
    date_of_birth = Column(DateTime)
    enrollment_date = Column(DateTime)
    department = relationship('Department', back_populates='students')
    courses_enrolled = relationship('Course', secondary=student_course,
                                    viewonly=False)
    assignments = relationship('Assignment', secondary=student_assignment,
                               viewonly=False)
    user_id = Column(String(60),
                     ForeignKey('users.id', onupdate='CASCADE',
                                ondelete='CASCADE'), nullable=False)
    department_id = Column(String(60),
                           ForeignKey('departments.id', onupdate='CASCADE',
                                      ondelete='CASCADE'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Student"""
        super().__init__(*args, **kwargs)
