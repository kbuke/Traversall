from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db

from relational_functions.one_to_many import one_to_many_back_populates, one_to_many_fk

class WishlistModel(db.Model, SerializerMixin):
    __tablename__ = "wishlists"
    id = db.Column(db.Integer, primary_key = True)

    # set it up to a user when I create the user model

    items = one_to_many_back_populates(
        "WishlistItemModel",
        "wishlist",
        delete_orphan=True
    )

    user_id = one_to_many_fk("users")
    user = one_to_many_back_populates(
        "BaseUserModel",
        "wishlist",
        delete_orphan=False
    )

    serialize_rules = (
        "-user.wishlist",
        "-items.wishlist",
    )

