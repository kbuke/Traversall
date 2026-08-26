from models.UserModels.BaseUserModel import BaseUserModel
from resources.BaseResource import BaseResource

from functions.create_wishlist_for_user import create_wishlist_for_user
from serialize_functions.serialize_wishlist import serialize_user


class AllUsers(BaseResource):
    model = BaseUserModel

    field_map = {
        "name": "name"
    }

    def get(self):
        records = [
            serialize_user(user)
            for user in self.model.query.all()
        ]

        return records, 200

    def post(self):
        return self.post_instance()


class SpecificUser(BaseResource):
    model = BaseUserModel

    def get(self, id):
        user = self.model.query.filter(self.model.id == id).first()

        if not user:
            return {
                "error": f"User {id} not found"
            }, 404

        return serialize_user(user), 200