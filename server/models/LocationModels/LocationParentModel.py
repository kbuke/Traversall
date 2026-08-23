from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db 

from functions.check_data_type_values import check_data_type_value

from validations.validate_slug import make_slug_default

class LocationParentModel(db.Model, SerializerMixin):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    slug = db.Column(db.String, default = make_slug_default("name"))
    img = db.Column(db.String, nullable = False)
    location_type = db.Column(db.String, nullable = False)

    native_name = db.Column(db.String, nullable = True) # native spelling of location IF it exists eg Japan =　日本
    native_pronounciation = db.Column(db.String, nullable = True) # native pronounciation IF it exists eg Japan = 日本 = Nihon

    @validates("location_type")
    def validate_location_type(self, key, value):
        # Create a set to ensure unique values
        allowed_locations = {
            "Continent",
            "Country",
            # Cities can either be a normal city or a capital 
            "City",
            "Capital City",
            # Set up things like prefectures, states, counties
            "States",
            "Prefecture",
            "Counties"
        }
        return check_data_type_value(allowed_locations, value)
        