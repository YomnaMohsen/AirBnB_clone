#!/usr/bin/python3
"""Defines Review class module """

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""

    place_id = " "
    user_id = " "
    text = " "

    def __init__(self, *args, **kwargs):
        """Initializes user object
        """
        super().__init__(*args, **kwargs)
