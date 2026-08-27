from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db 

from relational_functions.many_to_many import many_to_many_reltshp
from relational_functions.one_to_many import one_to_many_fk, one_to_many_back_populates

from validations.validate_slug import make_slug_default

class NotableEventModel(db.Model, SerializerMixin):
    __tablename__ = "notable_events"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    slug = db.Column(db.String, default = make_slug_default("name"))
    img = db.Column(db.String, nullable = False)
    start_date = db.Column(db.Date, nullable = False)
    end_date = db.Column(db.Date, nullable = False)
    info = db.Column(db.String, nullable = False)

    # An event can have significance in more than one country such as WW2
    countries_involved = many_to_many_reltshp(
        "CountryModel", "notable_events", "countries_events",
        left_table="countries", right_table="notable_events"
    )

    # Focus on locations that are impacted by an event 
    location_id = one_to_many_fk(
        "other_locations",
        is_null=True
    )

    location = one_to_many_back_populates(
        "OtherLocationModel",
        "events",
        delete_orphan=False
    )

    # An event such as WW2 can have several other significant events such as D-Day which fall under this umbrella
    parent_event_id = one_to_many_fk(
        "notable_events",
        is_null=True
    )

    parent_event = one_to_many_back_populates(
        "NotableEventModel",
        "child_events",
        delete_orphan=False,
        remote_side="NotableEventModel.id"
    )

    child_events = one_to_many_back_populates(
        "NotableEventModel",
        "parent_event",
        delete_orphan=True
    )

    serialize_rules = (
        "-countries_involved.events",
        "-parent_event.child_events",
        "-child_events.parent_event",
    )

    @validates("start_date", "end_date")
    def validate_event_dates(self, key, value):
        if key == "start_date":
            if not value:
                raise ValueError("Event must have a start date")
        if key == "end_date":
            if value and value < self.start_date:
                raise ValueError(f"If the event is over it must have ended on or after {self.start_date}")
        return value
    