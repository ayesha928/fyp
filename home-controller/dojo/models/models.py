from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )

from . import DBSession, Base

#class Site(Base):
#    __tablename__ = 'site'
#    id = Column(Integer, primary_key=True)
#    name = Column(Unicode(200), unique=True)
#    value = Column(Integer)
#
#    def __init__(self, name, value):
#        self.name = name
#        self.value = value


class Section(Base):
    __tablename__ = 'sections'
    section_number = Column(Integer, primary_key=True, autoincrement=False)
    section_name = Column(Unicode(200), unique=True)


class Device(Base):
    __tablename__ = 'devices'

    device_number = Column(Integer, primary_key=True, autoincrement=False)
    device_name = Column(Unicode(200), unique=True)
    section_number = Column(Integer, ForeignKey(Section.section_number))

    section = relationship(Section, backref=backref('devices'))

