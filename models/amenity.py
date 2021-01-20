#!/usr/bin/python3
""" ----> State Module for HBNB project <----"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """---> Define class Amanity and map to amenities table in a DB <---"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        # back_populates="amenities",
        viewonly=False)
