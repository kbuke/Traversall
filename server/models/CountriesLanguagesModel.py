from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db 

from models.LocationModels.CountryModel import CountryModel
from models.LanguagesModel import LanguagesModel

from relational_functions.many_to_many import many_to_many_fk

from validations.validate_instance_exists import validate_instance_exists

class CountriesLanguages(db.Model, SerializerMixin):
    __tablename__ = "countries_languages"

    id = db.Column(db.Integer, primary_key = True)
    country_id = many_to_many_fk("countries")
    language_id = many_to_many_fk("languages")

    @validates("country_id", "language_id")
    def validate_country_languages_ids(self, key, value):
        if key == "country_id":
            validate_instance_exists(
                CountryModel,
                value,
                "Country"
            )
        if key == "language_id":
            validate_instance_exists(
                LanguagesModel,
                value,
                "Language"
            )
        return value