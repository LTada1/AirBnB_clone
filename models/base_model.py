import uuid
from datetime import datetime


class BaseModel():
    """public instance attributes"""
    id = None
    created_at = None
    updated_at = None

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        return {
                "__class__": self.__class__.__name__,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
                }
