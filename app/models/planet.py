from app import db 

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    proximity = db.Column(db.String(250))
    description = db.Column(db.String(250))

def to_dict(self):
    return({
        "id": self.id,
        "name": self.name,
        "proximity": self.proximity,
        "description": self.description,
    })