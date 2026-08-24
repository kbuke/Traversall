from resources.BaseResource import BaseResource
from models.InterestModel import InterestModel
from serialize_functions.serialize_interests import serialize_interests

class AllInterests(BaseResource):
    model = InterestModel

    field_map = {
        "name": "name",
        "img": "img",
        "info": "info"
    }

    def get(self):
        records = [
            serialize_interests(interest)
            for interest in self.model.query.all()
        ]
        return records, 200
        # return self.get_all()

    def post(self):
        return self.post_instance()

class SpecificInterest(BaseResource):
    model = InterestModel

    field_map = {
        "name": "name",
        "img": "img",
        "info": "info"
    }

    def get(self, id):
        interest = self.model.query.filter(
            self.model.id == id
        ).first()

        if not interest:
            return{
                "error": f"Interest {id} not found"
            }, 404
        return serialize_interests(interest), 200
        # return self.get_specific(id)

    def patch(self, id):
        return self.patch_instance(id)

    def delete(self, id):
        return self.delete_instance(id)