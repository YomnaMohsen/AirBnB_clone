#!/usr/bin/python3
"""Defines Filestorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances

    class args:
    __file_path: string - path to the JSON file
     __objects: dictionary - empty but will store all objects
            by <class name>.id
    """
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id

        Args:
        obj: user defined object
        """
        name = obj.__class__.__name__
        FileStorage.__objects[name + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        """ we must create empty dict first then convert obj to dict and
        add to empty dict , so not modify __objects."""
        FileStorage.__file_path = "file.json"
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict = {key: val.to_dict() for key, val
                    in FileStorage.__objects.items()}
            json.dump(dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        obj_dictionary = {}
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dictionary = json.load(file)
            for key, val in obj_dictionary.items():
                cls_name = val["__class__"]
                cls_obj = eval(cls_name)(**obj_dictionary)
                FileStorage.__objects[key] = cls_obj
        except FileNotFoundError:
            pass
