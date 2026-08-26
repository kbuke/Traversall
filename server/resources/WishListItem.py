from models.WishlistModels.WishlistItemModel import WishlistItemModel
from resources.BaseResource import BaseResource

from flask import request
from sqlalchemy.exc import IntegrityError

from models.WishlistModels.WishlistModel import WishlistModel

from config import db

class AllWishListItems(BaseResource):
    model = WishlistItemModel

    field_map = {
        "wishlistId": "wishlist_id",
        "continentId": "continent_id",
        "countryId": "country_id",
        "locationId": "location_id",
        "siteId": "site_id",
        "businessId": "business_id"
    }

    def get(self):
        return self.get_all()

    def post(self):
        data = request.get_json()

        if not data:
            return {"error": "Missing JSON Data"}, 404 

        mapped_data = {
            self.field_map.get(k, k): v for k, v in data.items()
        }

        wishlist_id = mapped_data.pop("wishlist_id", None)
        wishlist = WishlistModel.query.get(wishlist_id)
        if not wishlist:
            return{
                "error": f"Wishlist {wishlist_id} not found"
            }, 404
        try:
            item = WishlistItemModel.create(wishlist=wishlist, **mapped_data)
            db.session.commit()
            return item.to_dict(), 201
        except (ValueError, IntegrityError) as e:
            db.session.rollback()
            return {"error": [str(e)]}, 400

class SpecificWishlistItem(BaseResource):
    model = WishlistItemModel
    
    field_map = {
        "wishlistId": "wishlist_id",
        "continentId": "continent_id",
        "countryId": "country_id",
        "locationId": "location_id",
        "siteId": "site_id",
        # "businessId": "business_id"
    }

    def get(self, id):
        return self.get_specific(id)

    def patch(self, id):
        return self.patch_instance(id)

    def delete(self, id):
        return self.delete_instance(id)