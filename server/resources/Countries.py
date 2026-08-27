from resources.BaseResource import BaseResource

from models.LocationModels.CountryModel import CountryModel

from decorators.require_admin_login import require_admin_login

class AllCountries(BaseResource):
    model = CountryModel

    field_map = {
        "name": "name",
        "img": "img",
        "locationType": "location_type",
        "population": "population",
        "passportImg": "passport_img",
        "safetyLevel": "safety_level"
    }

    def get(self):
        return self.get_all(
            "-continents",
            "-languages",
            "-media",
            "-locations",
            "-sites",
            "-businesses",
            "-wishlist_items",
        )

    @require_admin_login
    def post(self):
        return self.post_instance()

class SpecificCountry(BaseResource):
    model = CountryModel

    field_map = {
        "name": "name",
        "img": "img",
        "locationType": "location_type",
        "population": "population",
        "passportImg": "passport_img",
        "safetyLevel": "safety_level"
    }

    def get(self, id):
        return self.get_specific(id)

    def patch(self, id):
        return self.patch_instance(id)

    @require_admin_login
    def delete(self, id):
        return self.delete_instance(id)