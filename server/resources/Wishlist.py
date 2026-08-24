from models.WishlistModels.WishlistModel import WishlistModel
from resources.BaseResource import BaseResource

class SpecificWishlist(BaseResource):
    model = WishlistModel
    
    def get(self, id):
        return self.get_specific(id)

    