#!/usr/bin/python3
"""Defines User class module """

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = None
    password = None
    first_name = None
    last_name = None

    def __init__(self, *args, **kwargs):
        """Initializes user object
        """
        super().__init__(*args, **kwargs)
