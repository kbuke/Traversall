from config import db 

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from relational_functions.one_to_many import one_to_many_back_populates

class BaseUserModel(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    wishlist = one_to_many_back_populates(
        "WishlistModel",
        "user",
        delete_orphan=True
    )

    serialize_rules = (
        "-wishlist.user",
        "-wishlist."
    )