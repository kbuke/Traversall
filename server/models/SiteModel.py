from models.NameImgInfoModel import NameImgInfoModel
from models.LocationModels.OtherLocationModel import OtherLocationModel
from models.LocationModels.CountryModel import CountryModel

from relational_functions.one_to_many import one_to_many_back_populates, one_to_many_fk
from relational_functions.many_to_many import many_to_many_reltshp

from validations.validate_instance_exists import validate_instance_exists

from sqlalchemy.orm import validates

class SiteModel(NameImgInfoModel):
    __tablename__ = "sites"

    location_id = one_to_many_fk("other_locations")
    location = one_to_many_back_populates(
        "OtherLocationModel",
        "sites",
        delete_orphan=False
    )

    country_id = one_to_many_fk("countries")
    country = one_to_many_back_populates(
        "CountryModel",
        "sites",
        delete_orphan=False
    )

    interests = many_to_many_reltshp(
        "InterestModel", "sites", "sites_interests",
        left_table="sites", right_table="interests"
    )

    wishlist_items = one_to_many_back_populates(
        "WishlistItemModel",
        "site",
        delete_orphan=True
    )

    serialize_rules = (
        "-country.sites",
        "-country.continents.countries",
        "-country.locations",
        "-country.languages",

        "-interests",

        "-location.sites",

        "-wishlist_items",
    )

    @validates("location_id", "country_id")
    def validate_location_country_instances(self, key, value):
        if key == "location_id":
            validate_instance_exists(
                OtherLocationModel,
                value,
                "Location"
            )
        elif key == "country_id":
            validate_instance_exists(
                CountryModel,
                value,
                "Country"
            )
        return value

    # Set up business model, there may be a business that runs this site, or tour groups etc name like associated_businesses