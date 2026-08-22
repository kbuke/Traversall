from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db

from validations.validate_unique_name import validate_unique_name

from relational_functions.many_to_many import many_to_many_reltshp

class LanguagesModel(db.Model, SerializerMixin):
    __tablename__ = "languages"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    countries = many_to_many_reltshp(
        "CountryModel",
        "languages",
        "countries_languages"
    )

    serialize_rules = (
        "countries.languages",
        "countries.continents",
    )

    @validates("name")
    def validate_language_name(self, key, value):
        return validate_unique_name(
            value,
            LanguagesModel,
            "language"
        )