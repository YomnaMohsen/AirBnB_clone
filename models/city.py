#!/usr/bin/python3
"""Defines City class module """

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id = " "
    name = " "

    def __init__(self, *args, **kwargs):
        """Initializes user object
        """
        super().__init__(*args, **kwargs)
