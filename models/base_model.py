#!/usr/bin/python3
"""Defines Base_model class """

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all subclasses"""

    def __init__(self, *args, **kwargs):
        """Initializes Basemodel class
        Args:
        args(unused): tuple of variables
        kwargs: (dict) key/val pairs of attributes
       """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if (key != '__class__'):
                    if (key != 'updated_at' and key != 'created_at'):
                        setattr(self, key, val)
                    else:
                        setattr(self, key, datetime.fromisoformat(val))
                else:
                    continue

    def __str__(self):
        """custom __str__ fn"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
         of __dict__ of the instance"""
        dict = {}
        for key, val in self.__dict__.items():
            if (key != 'updated_at' and key != 'created_at'):
                dict[key] = val
            else:
                dict[key] = val.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
