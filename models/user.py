#!/usr/bin/python3
"""Defines User class module """

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = " "
    password = " "
    first_name = " "
    last_name = " "

    def __init__(self, *args, **kwargs):
        """Initializes user object
        """
        super().__init__(*args, **kwargs)
