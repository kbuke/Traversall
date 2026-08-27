from resources.BaseResource import BaseResource
from models.CountryEvents.NotableEventsModel import NotableEventModel

class BaseNotableEvents(BaseResource):
    model = NotableEventModel

    field_map = {
        "name": "name",
        "img": "img",
        "startDate": "start_date",
        "endDate": "end_date",
        "info": "info"
    }

class AllNotableEvents(BaseNotableEvents):

    serialize_fetch_and_post = (
        "-countries_involved",
        "-location",
        "-parent_event",
        "-child_events",
    )

    def get(self):
        return self.get_all(self.serialize_fetch_and_post)

    def post(self):
        return self.post_instance(self.serialize_fetch_and_post)