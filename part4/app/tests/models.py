from app.models.review import Review
from app.models.place import Place
from app.models.user import User
from app.models.amenity import Amenity
"""
This module tests Objects and their relations
"""


def main():
    """
    This Function calls all possibilities
    to check models and their relations
    """
    # Creation of users
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False
    print("{} created !!!\n".format(user))

    owner = User(first_name="Jane", last_name="Poe", email="jane.poe@example.com")
    print("{} created !!!\n".format(owner))

    # Creation of places by owner
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100.00, latitude=37.7749, longitude=-122.4194, owner=owner)
    print("Place created: {}".format(place))
    print("At: {}€ by night\n".format(place.created_at))

    place2 = Place(title="Family's home", description="A nice place for family", price=200.00, latitude=35.7749, longitude=-54.4194, owner=owner)
    print("Place created: {}".format(place2))
    print("At: {}€ by night\n".format(place2.created_at))

    # Creations of amenities
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")
    print("Amenity: {}".format(amenity.name))
    print("At: {}\n".format(amenity.created_at))

    amenity2 = Amenity(name="Swimming pool")
    assert amenity2.name == "Swimming pool"
    print("Amenity creation test passed!")
    print("Amenity: {}".format(amenity2.name))
    print("At: {}\n".format(amenity2.created_at))

    # Creation of reviews
    review = Review(text="Great stay!", rating=5, place=place, user=user)
    assert review.text == "Great stay!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == user
    print("review creation test passed!")
    print("review: {}".format(review))
    print("At: {}".format(review.created_at))
    print("writer of this review: {}".format(review.user))
    print("commenting {}".format(review.place))
    print("rating: {} stars".format(review.rating))
    print("comment: {}".format(review.text))

    review2 = Review(text="Perfect for family !", rating=4, place=place2, user=user)
    assert review2.text == "Perfect for family !"
    assert review2.rating == 4
    assert review2.place == place2
    assert review2.user == user
    print("review creation test passed!")
    print("review: {}".format(review2))
    print("At: {}".format(review2.created_at))
    print("writer of this review: {}".format(review2.user))
    print("commenting {}".format(review2.place))
    print("rating: {} stars".format(review2.rating))
    print("comment: {}".format(review2.text))

    # Check relation user/place, user/review

    owner.add_place(place)
    print("{} has:\n{}".format(owner, owner.places[0]))

    owner.add_place(place2)
    print("{} has:\n{}".format(owner, owner.places[1]))

    print("So, {} has:".format(owner))
    for plc in owner.places:
        print(plc)

    user.add_review(review)
    print("{} wrote:\n{}".format(user, user.reviews[0]))

    user.add_review(review2)
    print("{} wrote:\n{}".format(user, user.reviews[1]))

    print("So, {} has posted:".format(user))
    for rev in user.reviews:
        print(rev)

    # Check relation place/review, place/amenities

    place.add_review(review)
    print("{} has received:\n{}".format(place, place.reviews[0]))

    place.add_review(review2)
    print("{} has received:\n{}".format(owner, place.reviews[1]))

    print("So, {} has received:".format(owner))
    for rev in place.reviews:
        print(rev)

    place.add_amenity(amenity)
    print("{} offers:\n{}".format(place, place.amenities[0]))

    place.add_amenity(amenity2)
    print("{} offers:\n{}".format(place, place.amenities[1]))

    print("So, {} offers:".format(place))
    for ame in place.amenities:
        print(ame)


main()
