from models.LocationModels.LocationParentModel import LocationParentModel

from config import db

from relational_functions.one_to_many import one_to_many_back_populates, one_to_many_fk

from sqlalchemy.orm import validates

class OtherLocationModel(LocationParentModel):
    __tablename__ = "other_locations"

    # This can query what the level of the location is regardless of its name
    # eg a value of 0 can represent states (US), prefectures (Japan), counties (Ireland) etc
    admin_level = db.Column(db.Integer, nullable = False)

    country_id = one_to_many_fk("countries")
    country = one_to_many_back_populates(
        "CountryModel",
        "locations",
        delete_orphan=False
    )

    # Self-referential FK: nullable because top-level locations (eg states) 
    # have no parent location, only a country
    parent_location_id = one_to_many_fk(
        "other_locations",
        is_null=True
    )

    parent_location = one_to_many_back_populates(
        "OtherLocationModel",
        "child_locations",
        delete_orphan=False,
        remote_side="OtherLocationModel.id" # remote_side marks this side as the "one"
    )

    child_locations = one_to_many_back_populates(
        "OtherLocationModel",
        "parent_location",
        delete_orphan=True
    )

    sites = one_to_many_back_populates(
        "SiteModel",
        "location"
    )

    businesses = one_to_many_back_populates(
        "BaseBusinessModel",
        "location"
    )

    wishlist_items = one_to_many_back_populates(
        "WishlistItemModel",
        "location",
        delete_orphan=True
    )

    events = one_to_many_back_populates(
        "NotableEventModel",
        "location",
        delete_orphan=True
    )

    @validates("parent_location", "admin_level")
    def valudate_hierarchy(self, key, value):
        if key == "parent_location" and value is not None:
            if value.country_id != self.country_id:
                raise ValueError(
                    f"Parent's location country must match this location's country"
                )

        if key == "admin_level" and self.parent_location is not None:
            if value <= self.parent_location.admin_level:
                raise ValueError(
                    "admin_evel must be greater than parent's admin_level"
                )
        return value

    serialize_rules = (
        "-country.locations",
        "-country.continents",
        "-country.languages",
        "-child_locations.parent_location",
        "-parent_location.child_locations",
        "-sites.location",
        "-sites.country",
        "-wishlist_items",
        "-businesses.location",
    )