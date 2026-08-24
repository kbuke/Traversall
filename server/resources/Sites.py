from models.SiteModel import SiteModel
from resources.BaseResource import BaseResource

from functions.derive_country_id import derive_country_id_on_create, derive_country_id_on_update

from models.LocationModels.OtherLocationModel import OtherLocationModel

from serialize_functions.serialze_site import serialize_site

class AllSites(BaseResource):
    model = SiteModel

    field_map = {
        "name": "name",
        "img": "img",
        "info": "info",
        "locationId": "location_id",
        "countryId": "country_id"
    }

    def prepare_data(self, data):
        return derive_country_id_on_create(
            data,
            parent_field="location_id",
            parent_model=OtherLocationModel,
            parent_required=True
        )

    def get(self):
        records = [
            serialize_site(site)
            for site in self.model.query.all()
        ]
        return records, 200

    def post(self):
        return self.post_instance()

class SpecificSite(BaseResource):
    model = SiteModel

    field_map = {
        "name": "name",
        "img": "img",
        "info": "info",
        "locationId": "location_id",
        "countryId": "country_id"
    }

    def prepare_data(self, data):
        return derive_country_id_on_update(
            data,
            parent_field="location_id",
            parent_model=OtherLocationModel,
            parent_required=False
        )

    def get(self, id):
        site = self.model.query.filter(
            self.model.id == id
        ).first()

        if not site:
            return {
                "error": f"Site {id} not found"
            }, 404
        return serialize_site(site), 200

    def patch(self, id):
        return self.patch_instance(id)

    def delete(self, id):
        return self.delete_instance(id)