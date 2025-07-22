# app/models/review.py
from app.models.base_model import BaseModel
from app import db

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'),
                        nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'),
                         nullable=False)

    def __init__(self, text, rating, user, place):
        super().__init__()
        if not text:
            raise ValueError("Review text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.text = text
        self.rating = rating
        self.user = user
        self.place = place

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating
        }
