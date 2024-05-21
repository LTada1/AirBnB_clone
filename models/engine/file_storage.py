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
        return BaseModel.__objects
    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        key = f"{obj.__class__.__name__.{obj.id}"
        BaseModel.__objects[key] = obj
    def save(self):
        "serializes __objects to the JSON file"
        with open("BaseModel.__file_path", "w") as file_json:
            json_objects = {key:obj.__dict__ for key, obj in BaseModel.__objects.items()}
        json.dumps(json_file, file_json)
    def reload(self):
        "deserializes the JSON file to __objects"
            try:
                with open('BaseModel.__file_patth', 'r') as json_file:
                    json_objects = json.loads(json_file)
                    for key, value in json_objects.items():
                        obj = BaseModel(**values)
                        BaseModel.__objects[key] = obj
            except FileNotFoundError:
            pass

