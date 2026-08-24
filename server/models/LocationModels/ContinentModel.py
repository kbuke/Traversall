from models.LocationModels.LocationParentModel import LocationParentModel

from sqlalchemy.orm import validates

from functions.check_data_type_values import check_data_type_value

from validations.validate_unique_name import validate_unique_name

from relational_functions.many_to_many import many_to_many_reltshp
from relational_functions.one_to_many import one_to_many_back_populates

class ContinentModel(LocationParentModel):
    __tablename__ = "continents"

    # Some countries like Turkey can be in 2 continents
    countries = many_to_many_reltshp(
        "CountryModel",
        "continents",
        "countries_continents",
        left_table="continents",
        right_table="countries"
    )

    wishlist_items = one_to_many_back_populates(
        "WishlistItemModel",
        "continent",
        delete_orphan=True
    )

    serialize_rules = (
        "-countries.continents",
        "-countries.languages",
        "-countries.locations",
        "-wishlist_items",
    )

    contitent_names = {
        "Antartica", 
        "Australia", 
        "North America",
        "South America",
        "Europe",
        "Asia",
        "Africa"
    }

    @validates("name")
    def validate_continent_name(self, key, value):
        check_data_type_value(
            self.contitent_names,
            value
        )

        return validate_unique_name(
            value,
            ContinentModel,
            "Continent"
        )