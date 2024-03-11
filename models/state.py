#!/usr/bin/python3
"""Defines state class module """

from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel"""

    name = None

    def __init__(self, *args, **kwargs):
        """Initializes user object
        """
        super().__init__(*args, **kwargs)
