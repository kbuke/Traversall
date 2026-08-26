from config import db 
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from validations.validate_instance_exists import validate_instance_exists

from relational_functions.one_to_many import one_to_many_back_populates, one_to_many_fk

from models.LocationModels.OtherLocationModel import OtherLocationModel

class BaseBusinessModel(db.Model, SerializerMixin):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer)

    location_id = one_to_many_fk("other_locations")
    location = one_to_many_back_populates(
        "OtherLocationModel",
        "businesses",
        delete_orphan=False
    )

    country_id = one_to_many_fk("countries")
    country = one_to_many_back_populates(
        "CountryModel",
        "businesses",
        delete_orphan=False
    )

    wishlist_items = one_to_many_back_populates(
        "WishlistItemModel",
        "business",
        delete_orphan=True
    )

    @validates("location_id")
    def validate_business_location(self, key, value):
        validate_instance_exists(
            OtherLocationModel,
            value,
            "Location"
        )
        return value

    serialize_rules = (
        "-wishlist_items.business",
        "-location.businesses",
        "-country.businesses",
        "-country.locations",
        "-country.sites",
        "-country.wishlist_items",
        "-country.continents",
    )