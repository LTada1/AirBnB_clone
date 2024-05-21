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
from models.base_model import BaseModel

class FileStorage:
    "Private class attributes"
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        "returns the dictionary __objects"
        return FileStorage.__objects
    def new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    def save(self):
        "serializes __objects to the JSON file"
        json_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(json_objects, json_file)
    def reload(self):
        "deserializes the JSON file to __objects"
        try:
            with open('FileStorage.__file_patth', 'r') as json_file:
                json_objects = json.loads(json_file)
                "BaseModel is imported here to avoid circular import"
                from models.base_model import BaseModel
                for key, value in json_objects.items():
                    obj = BaseModel(**values)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

