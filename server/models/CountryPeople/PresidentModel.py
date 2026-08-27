# from models.CountryPeople.PeopleModel import PeopleModel

# from config import db 

# from sqlalchemy.orm import validates
# from sqlalchemy_serializer import SerializerMixin

# class PresidentModel(PeopleModel):
#     start_year = db.Column(db.Date, nullable = True)
#     still_in_power = db.Column(db.Boolean, nullable = True)
#     end_year = db.Column(db.Date, nullable = True)

#     # set up model for unconsecutive terms like Trump
#     consecutive_terms = db.Column(db.Boolean, nullable = True)
#     next_start = db.Column(db.Date, nullable = True)
#     next_end = db.Column(db.Date, nullable = True)

#     title = db.Column(db.String)

#     __mapper_args__ = {
#         "polymorphic_identity": "Leaders"
#     }

#     def valudate_instance(self):
#         # Ensure a title is given 
#         if not self.title:
#             raise ValueError("A title must be given for the president")
#         # Ensure start year is given
#         if not self.start_year:
#             raise ValueError("Leader must have a start year")
#         # If still in power, end year can not be given 
#         if self.still_in_power and self.end_year:
#             raise ValueError("An end year can not be given if they are still in power")
#         # If end year is given then it must be after start year
#         if self.end_year and self.end_year<self.start_year:
#             raise ValueError("An end year must be after the start year")
#         # Ensure no dates given unless they served a new (unconsecutive) term
#         if not self.consecutive_terms and self.next_start or self.next_end:
#             raise ValueError("No next dates should be given unless the leader took a new term")
#         if self.consecutive_terms and not self.next_start:
#             raise ValueError("If they serve a new term, then a start date must be given")
#         if self.next_end and self.next_end < self.next_start:
#             raise ValueError("The end date can not be before the start date")

#         if self.dob > self.start_year:
#             raise ValueError("A president can not start a term before they are born")
#         if self.dob > self.next_start:
#             raise ValueError("A president can not start a term before they are born")
#         if self.date_of_death > self.end_year or self.date_of_death > self.next_end:
#             if self.name != "Kim Il-sung":
#                 raise ValueError("Only Kim Il-sung (North Korea) is an 'Eternal President'")
        
