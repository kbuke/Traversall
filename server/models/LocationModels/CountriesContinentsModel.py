from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db

from models.LocationModels.ContinentModel import ContinentModel
from models.LocationModels.CountryModel import CountryModel

from relational_functions.many_to_many import many_to_many_fk

from validations.validate_instance_exists import validate_instance_exists

class CountriesContinentsModel(db.Model, SerializerMixin):
    __tablename__ = "countries_continents"

    id = db.Column(db.Integer, primary_key = True)
    continent_id = many_to_many_fk("continents")
    country_id = many_to_many_fk("countries")

    @validates("continent_id", "country_id")
    def validate_location_ids(self, key, value):
        if key == "continent_id":
            validate_instance_exists(
                ContinentModel,
                value,
                "Continent"
            )
        if key == "country_id":
            validate_instance_exists(
                CountryModel,
                value,
                "Country"
            )
        return value