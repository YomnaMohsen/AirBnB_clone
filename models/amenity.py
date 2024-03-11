#!/usr/bin/python3
"""Defines Amenity class module """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""

    name = None

    def __init__(self, *args, **kwargs):
        """Initializes user object
        """
        super().__init__(*args, **kwargs)
