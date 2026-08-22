from models.LanguagesModel import LanguagesModel
from resources.BaseResource import BaseResource

from decorators.require_admin_login import require_admin_login

class AllLanguages(BaseResource):
    model = LanguagesModel

    field_map = {
        "name": "name"
    }

    def get(self):
        return self.get_all()

    @require_admin_login
    def post(self):
        return self.post_instance()

class SpecificLanguages(BaseResource):
    model = LanguagesModel

    field_map = {
        "name": "name"
    }

    def get(self, id):
        return self.get_specific(id)

    @require_admin_login
    def patch(self, id):
        return self.patch_instance(id)

    @require_admin_login
    def delete(self, id):
        return self.delete_instance(id)