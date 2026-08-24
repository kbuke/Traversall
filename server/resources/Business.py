from resources.BaseResource import BaseResource
from models.UserModels.BaseBusinessModel import BaseBusinessModel

class AllBusinesses(BaseResource):
    model = BaseBusinessModel

    field_map = {
        "name": "name"
    }

    def get(self):
        return self.get_all()

    def post(self):
        return self.post_instance()

class SpecificBusiness(BaseResource):
    model = BaseBusinessModel

    field_map = {
        "name": "name"
    }

    def get(self, id):
        return self.get_specific(id)

    def patch(self, id):
        return self.patch_instance(id)

    def delete(self, id):
        return self.delete_instance(id)