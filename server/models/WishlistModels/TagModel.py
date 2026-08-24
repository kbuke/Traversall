from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db
from functions.check_data_type_values import check_data_type_value
from validations.validate_slug import make_slug_default
from relational_functions.many_to_many import many_to_many_reltshp

class TagModel(db.Model, SerializerMixin):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tag_type = db.Column(db.String, nullable=False)  # "business-type" | "interest" | "location"
    slug = db.Column(db.String, default=make_slug_default("name"))

    # Only populated when tag_type == "location", lets the frontend
    # label ("Prefecture: Kyoto Prefecture") and order tags without
    # re-querying the location tree.
    location_type = db.Column(db.String, nullable=True)
    hierarchy_level = db.Column(db.Integer, nullable=True)

    wishlist_items = many_to_many_reltshp(
        "WishlistItemModel", "tags", "wishlist_items_tags",
        left_table="wishlist_items", right_table="tags"
    )

    __table_args__ = (
        db.UniqueConstraint("name", "tag_type", name="uq_tag_name_type"),
    )

    @validates("tag_type")
    def validate_tag_type(self, key, value):
        allowed = {"business-type", "interest", "location"}
        return check_data_type_value(allowed, value)