# app/models/amenity.py
''' Amenity Class represents an amenity, inheriting from BaseModel'''

from app.models.base_model import BaseModel
from app import db


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    #id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    '''Represents an amenity with attributes and restrictions'''
    def __init__(self, name):
        '''Initialize a new Amenity instance with restrictions'''
        super().__init__()
        if not isinstance(name, str):
            raise TypeError("Amenity name must be a string of characters.")
        if not name or len(name) > 50:
            raise ValueError("Amenity name must be a string of 1 to 50 characters.")
        self.name = name

    def to_dict(self):
        """Convert the Amenity object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name
        }
