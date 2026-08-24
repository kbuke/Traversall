from models.UserModels.BaseUserModel import BaseUserModel
from resources.BaseResource import BaseResource
from functions.create_wishlist_for_user import create_wishlist_for_user

class AllUsers(BaseResource):
    model = BaseUserModel

    field_map = {
        "name": "name"
    }

    def get(self):
        return self.get_all()

    def post(self):
        return self.post_instance()