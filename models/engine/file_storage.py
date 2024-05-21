#!/usr/bin/python3
"""
A basemodel for creating objects
BaseModel(): Base Class
id: id attribute
created_at: time of creation
updated_at:updated time
to_dict(): create dict representation of object

"""

import json
import BaseModel

class FileStorage:
    __file_path
    __objects = {}

    def __init__(self):
        self.__file_path = __file_path
        self.__objects = __objects
    def all(self):
        "returns the dictionary __objects"
        return
                {
                "__class": self.__class__.__name__.id
                }
    def new(self, obj):
    def save(self):
        "serializes __objects to the JSON file"
        self.__file_path = json.dumps(__objects)
    def reload(self):
        "deserializes the JSON file to __objects"
        with open("self.__file_path", 'r') as self.__ojects:
            if not self.__objects:
                pass
            except FileNotFoundError:
                pass
            try:
                self.__objects = json.reloads(self.__file_path):wq!

