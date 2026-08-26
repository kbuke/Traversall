from config import db 

from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from relational_functions.many_to_many import many_to_many_reltshp

class MediaModel(db.Model, SerializerMixin):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    img = db.Column(db.String, nullable = False)
    year = db.Column(db.String, nullable = False)
    info = db.Column(db.String, nullable = False)
    media_type = db.Column(db.String, nullable = False)

    # Set up a many-to-many relationship with countries, as one film or book can have cultural significance to more than one country
    countries = many_to_many_reltshp(
        "CountryModel", "media", "country_media",
        left_table="countries", right_table="media"
    )

    __mapper_args__ = {
        "polymorphic_on": media_type,
        "polymorphic_identity": "Media"
    }

    serialize_rules = (
        "-countries.media",
        "-countries.languages",
        "-countries.continents",
        "-countries.locations",
        "-countries.sites",
        "-countries.businesses",
        "-countries.wishlist_items",
    )