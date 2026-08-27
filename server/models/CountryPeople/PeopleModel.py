# from config import db 

# from sqlalchemy.orm import validates
# from sqlalchemy_serializer import SerializerMixin

# from relational_functions.many_to_many import many_to_many_reltshp 

# class PeopleModel(db.Model, SerializerMixin):
#     __tablename__ = "people"

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String, nullable = False)
#     dob = db.Column(db.Date, nullable = False)
#     date_of_death = db.Column(db.Date, nullable = True)
#     significance = db.Column(db.String, nullable = False)
#     person_type = db.Column(db.String, nullable = False)

#     countries_of_significance = many_to_many_reltshp(
#         "CountryModel", "perople", "country_people",
#         left_table="countries", right_table="people"
#     )

#     __mapper_args__ = {
#         "polymorphic_on": person_type,
#         "polymorphic_identity": "People"
#     }

#     serialize_rules = (
#         "-countries_of_significance.people",
#     )