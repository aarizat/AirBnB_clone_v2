#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity
import models


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        "place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey(
            "places.id", ondelete="CASCADE", onupdate="CASCADE"),
            primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey(
            "amenities.id", ondelete="CASCADE", onupdate="CASCADE"),
            primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review", cascade="delete", backref="Place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """getter attribute cities"""
            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review.append(review)
            return review_list

        @property
        def amenities(self):
            """getter amenities id"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """setter attribute cities"""
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
