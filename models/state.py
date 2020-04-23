#!/usr/bin/python3
"""This is the state class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import os
from models.city import City


class State(BaseModel, Base):
    """This is the class for State.
    Attributes:
        name: input name.
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """Return cities."""
            all_cities = models.storage.all(City)
            all_cities_state = []
            for key, value in all_cities.items():
                if self.id == value.state_id:
                    all_cities_state.append(value)
            return all_cities_state
