from resources.BaseResource import BaseResource

from decorators.require_admin_login import require_admin_login

from models.LocationModels.ContinentModel import ContinentModel

class AllContinents(BaseResource):
    model = ContinentModel

    field_map = {
        "name": "name",
        "img": "img",
        "locationType": "location_type"
    }

    def get(self):
        return self.get_all(
            "-countries",
        )

    @require_admin_login
    def post(self):
        return self.post_instance()

class SpecificContinent(BaseResource):
    model = ContinentModel

    field_map = {
        "name": "name",
        "img": "img",
        "locationType": "location_type"
    }

    def get(self, id):
        return self.get_specific(id)

    @require_admin_login
    def patch(self, id):
        return self.patch_instance(id)

    @require_admin_login
    def delete(self, id):
        return self.delete_instance(id)