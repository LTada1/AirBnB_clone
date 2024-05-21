#!/usr/bin/python3
"""
A basemodel for creating objects
BaseModel(): Base Class
id: id attribute
created_at: time of creation
updated_at:updated time
to_dict(): create dict representation of object

"""
import uuid
from datetime import datetime


class BaseModel():
    """public instance attributes"""
    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "create_at" or key == "update_st":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
                if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ return string """
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """ Update date and time """
        self.update_at = datetime.now()
        "Import here to avoid circular import"
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Creat a dict repof an object """
        return {
                "__class__": self.__class__.__name__,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
                }
    @classmethod
    def re_creaate(cls, in_dict):
        """ Recreate object from a dict reprsentation """
        return cls(in_dict)
