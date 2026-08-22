from models.LocationModels.LocationParentModel import LocationParentModel

from sqlalchemy.orm import validates

from functions.check_data_type_values import check_data_type_value

from validations.validate_unique_value import validate_unique_value

class ContinentModel(LocationParentModel):
    __tablename__ = "continents"

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

        return validate_unique_value(
            value,
            ContinentModel,
            "Continent"
        )