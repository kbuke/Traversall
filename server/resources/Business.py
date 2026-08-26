from resources.BaseResource import BaseResource
from models.UserModels.BaseBusinessModel import BaseBusinessModel

from serialize_functions.serialize_business import serialize_business

class AllBusinesses(BaseResource):
    model = BaseBusinessModel

    field_map = {
        "name": "name",
        "locationId": "location_id",
        "countryId": "country_id"
    }

    def get(self):
        records = [
            serialize_business(business)
            for business in self.model.query.all()
        ]
        return records, 200
        # return self.get_all()

    def post(self):
        return self.post_instance()

class SpecificBusiness(BaseResource):
    model = BaseBusinessModel

    field_map = {
        "name": "name"
    }

    def get(self, id):
        business = self.model.query.filter(
            self.model.id == id
        ).first()

        if not business:
            return{
                "error": f"Business {id} not found"
            }, 404
        return serialize_business(business), 200
        # return self.get_specific(id)

    def patch(self, id):
        return self.patch_instance(id)

    def delete(self, id):
        return self.delete_instance(id)