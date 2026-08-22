from models.CountriesLanguagesModel import CountriesLanguages
from resources.BaseResource import BaseResource

from decorators.require_admin_login import require_admin_login

class AllCountriesLanguages(BaseResource):
    model = CountriesLanguages

    field_map = {
        "countryId": "country_id",
        "languageId": "language_id"
    }

    def get(self):
        return self.get_all()

    @require_admin_login
    def post(self):
        return self.post_instance()

class SpecificCountryLanguages(BaseResource):
    model = CountriesLanguages

    field_map = {
        "countryId": "country_id",
        "languageId": "language_id"
    }

    def get(self, id):
        return self.get_specific(id)

    @require_admin_login
    def delete(self, id):
        return self.delete_instance(id)