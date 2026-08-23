from models.LocationModels.OtherLocationModel import OtherLocationModel
from resources.BaseResource import BaseResource

from decorators.require_admin_login import require_admin_login

from flask import request

class AllOtherLocations(BaseResource):
    model = OtherLocationModel

    field_map = {
        "name": "name",
        "img": "img",
        "locationType": "location_type",
        "adminLevel": "admin_level",
        "countryId": "country_id",
        "parentLocationId": "parent_location_id"
    }

    def prepare_data(self, data):
        parent_id = data.get("parent_location_id")

        if parent_id is not None:
            parent = self.model.query.get(parent_id)
            if not parent:
                raise ValueError(f"Parent location {parent_id} not found.")
            # ignore what client sent for country_id, derive it
            data["country_id"] = parent.country_id
        else:
            # for top-level location (eg states) MUST specify a country directly
            if not data.get("country_id"):
                raise ValueError("A location with no parent must specify it's country id")
        return data

    def get(self):
        return self.get_all()

    @require_admin_login
    def post(self):
        return self.post_instance()

class SpecificOtherLocation(BaseResource):
    model = OtherLocationModel

    field_map = {
        "name": "name",
        "img": "img",
        "locationType": "location_type",
        "adminLevel": "admin_level",
        "countryId": "country_id",
        "parentLocationId": "parent_location_id"
    }

    def prepare_data(self, data):
        if "parent_location_id" in data:
            parent_id = data["parent_location_id"]
            if parent_id is not None:
                parent = self.model.query.get(parent_id)
                if not parent:
                    raise ValueError(f"Parent location {parent_id} not found.")
                data["country_id"] = parent.country_id
            else:
                if not data.get("country_id"):
                    raise ValueError("Removing a parent requires specifying country_id")
        else: 
            data.pop("country_id", None)
        return data

    def get(self, id):
        return self.get_specific(id)

    @require_admin_login
    def patch(self, id):
        return self.patch_instance(
            id, 
            data=self.prepare_data(request.get_json())
        )

    @require_admin_login
    def delete(self, id):
        return self.delete_instance(id)