from app.models.base_model import BaseModel
from app import db
from app.models.association_tables import place_amenity

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'),
                         nullable=False)
    reviews = db.relationship('Review', backref='place', lazy=True)
    amenities = db.relationship('Amenity', secondary=place_amenity,
                                lazy='subquery',
                                backref=db.backref('places', lazy=True))

    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner_id: int, description=""):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Title is required and must be ≤ 100 characters.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180 and 180.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id

    def to_dict(self):
        """Convert the Place object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id
        }
