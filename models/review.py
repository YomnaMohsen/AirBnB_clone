#!/usr/bin/python3
"""Defines Review class module """

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""

    place_id = None
    user_id = None
    text = None

    def __init__(self, *args, **kwargs):
        """Initializes user object
        """
        super().__init__(*args, **kwargs)
