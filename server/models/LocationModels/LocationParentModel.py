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

    # Create a set to ensure unique values
    allowed_locations = {
        "Continent",
        "Country",
        "City",
        # Set up things like prefectures, states, counties
        "States",
        "Prefectures",
        "Counties"
    }

    @validates("location_type")
    def validate_location_type(self, key, value):
        return check_data_type_value(self.allowed_locations, value)
        