from models.LocationModels.CountriesContinentsModel import CountriesContinentsModel

from resources.BaseResource import BaseResource

from decorators.require_admin_login import require_admin_login

class AllCountriesContinents(BaseResource):
    model = CountriesContinentsModel

    field_map = {
        "continentId": "continent_id",
        "countryId": "country_id"
    }

    def get(self):
        return self.get_all()

    @require_admin_login
    def post(self):
        return self.post_instance()

class SpecificCountriesContinents(BaseResource):
    def get(self, id):
        return self.get_specific(id)

    @require_admin_login
    def delete(self, id):
        return self.delete_instance(id)
  