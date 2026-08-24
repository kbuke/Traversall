from config import db 
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from relational_functions.one_to_many import one_to_many_back_populates

class BaseBusinessModel(db.Model, SerializerMixin):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer)

    wishlist_items = one_to_many_back_populates(
        "WishlistItemModel",
        "business",
        delete_orphan=True
    )

    serialize_rules = (
        "-wishlist_items.business",
    )