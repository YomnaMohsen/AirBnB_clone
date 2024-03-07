#!/usr/bin/python3
"""Defines Base_model class """

import uuid
from datetime import datetime

class BaseModel:
    """Base class for all subclasses"""

    def __init__(self, *args, **kwargs):
        """Initializes Basemodel class
        Args:
        args(unused): tuple of variables
        kwargs: (dict) key/val pairs of attributes
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, val in kwargs.items():
                if (key != "__class__"):
                    if (key != 'updated_at' and key != 'created_at'):
                        self.__dict__[key] = val
                    else:
                        self.__dict__[key] = datetime.fromisoformat(val)    


    def __str__(self):
        """custom __str__ fn"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute 
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
         of __dict__ of the instance""" 
        dict = {}
        for key, val in self.__dict__.items():
            if (key != 'updated_at' and key != 'created_at'):
                dict[key] = val
            else:
                dict[key] = val.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
