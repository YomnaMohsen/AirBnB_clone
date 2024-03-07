#!/usr/bin/python3
"""Defines Filestorage class"""

class FileStorage:
    """serializes instances to a JSON file and 
    deserializes JSON file to instances
    
    class args:
    __file_path: string - path to the JSON file
     __objects: dictionary - empty but will store all objects 
            by <class name>.id
    """
    __file_path = " "
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
        pass
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        pass
    
    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists"""
        pass


