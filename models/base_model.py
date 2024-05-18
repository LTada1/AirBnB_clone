class BaseModel():
    def __init__(self, uuid, created_at, updated_at):
        self.id = uuid
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
    def to_dict(self):
    def __str__:
