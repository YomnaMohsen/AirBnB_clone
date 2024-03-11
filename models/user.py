#!/usr/bin/python3
"""Defines User class module """

from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that inherits from BaseModel
    Args:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    
    email = None
    password = None
    first_name = None
    last_name = None
