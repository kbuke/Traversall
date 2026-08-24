from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from config import db

from relational_functions.many_to_many import many_to_many_reltshp

class InterestModel(db.Model, SerializerMixin):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    img = db.Column(db.String, nullable = False)

    sites = many_to_many_reltshp(
        "SiteModel", "interests", "sites_interests",
        left_table="sites", right_table="interests"
    )

    serialize_rules = (
        "-sites.interests",
    )