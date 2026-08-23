from models.LocationModels.LocationParentModel import LocationParentModel

from config import db

from sqlalchemy.orm import validates

from validations.validate_unique_name import validate_unique_name

from functions.check_data_type_values import check_data_type_value

from relational_functions.many_to_many import many_to_many_reltshp
from relational_functions.one_to_many import one_to_many_back_populates

class CountryModel(LocationParentModel):
    __tablename__ = "countries"

    population = db.Column(db.Integer, nullable = False)
    passport_img = db.Column(db.String, nullable = False) # eventually have this as a upload, and maybe have several options for a stamp
    safety_level = db.Column(db.String, nullable = False)

    # Some countries, like South Africa can have more than one capital city
    # Some countries, like South Africa and China can have more than one language
    # Have a login section for countries so that there is a country admin (this should maybe be a one-to-many relationshp so a country can have many admins)

    continents = many_to_many_reltshp(
        "ContinentModel",
        "countries",
        "countries_continents"
    )

    languages = many_to_many_reltshp(
        "LanguagesModel",
        "countries",
        "countries_languages"
    )

    locations = one_to_many_back_populates(
        "OtherLocationModel",
        "country",
        delete_orphan=True
    )

    serialize_rules = (
        "-continents.countries",
        "-languages.countries",
        "-locations.countries",
    )

    @validates("name", "native_name", "native_pronounciation")
    def validate_country_names(self, key, value):
        # Ensure name of country is unique
        if key == "name":
            validate_unique_name(value, CountryModel, "Country")

        # Ensure if native name exists then it is unique
        if key == "native_name" and value:
            validate_unique_name(value, CountryModel, "Native Country Name")

        # Ensure that if native name exists, and pronounciation doesnt this is flagged
        if self.native_name and key == "native_pronounciation" and not value:
            raise ValueError("Please enter pronounciation of the native name of country")

        # Ensure that if there is a native name, its pronounciation is also unique
        if self.native_name and key == "native_pronounciation" and value:
            validate_unique_name(value, CountryModel, "Country Name Pronounciation")

        return value

    @validates("safety_level")
    def validate_country_safety(self, key, value):
        available_safety_levels = {
            "Very Safe",
            "Safe",
            "Caution",
            "Dangerous",
            "Very Dangerous"
        }
        return check_data_type_value(available_safety_levels, value)