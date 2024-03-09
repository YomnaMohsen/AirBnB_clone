#!/usr/bin/python3
"""Defines Filestorage class"""

import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances

    class args:
    __file_path: string - path to the JSON file
     __objects: dictionary - empty but will store all objects
            by <class name>.id
    """
    __file_path = "file.json"
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
        FileStorage.__objects[name + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        """ we must create empty dict first then convert obj to dict and
        add to empty dict , so not modify __objects."""

        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.loads(file.read())
            for key, val in obj_dict.items():
                cls_obj = globals()[val['__class__']]
                FileStorage.__objects[key] = cls_obj(**obj_dict)
        except FileNotFoundError:
            pass
