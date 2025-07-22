from abc import ABC, abstractmethod
from app.extensions import db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository:
    """A simple in-memory repository for testing (not used with SQLAlchemy)."""
    def __init__(self):
        self._data = {}

    def add(self, obj):
        self._data[obj.id] = obj

    def get(self, obj_id):
        return self._data.get(obj_id)

    def get_all(self):
        return list(self._data.values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
        return obj

    def delete(self, obj_id):
        return self._data.pop(obj_id, None)

    def get_by_attribute(self, attr, value):
        for obj in self._data.values():
            if getattr(obj, attr, None) == value:
                return obj
        return None


# SQLAlchemy repositories
class BaseRepository:
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()
        return obj

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
        return obj

    def get_by_attribute(self, attr, value):
        return self.model.query.filter(getattr(self.model, attr) == value).first()


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()


class PlaceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Place)


class ReviewRepository(BaseRepository):
    def __init__(self):
        super().__init__(Review)


class AmenityRepository(BaseRepository):
    def __init__(self):
        super().__init__(Amenity)
