from models.CountryMedia.MediaModel import MediaModel
from resources.BaseResource import BaseResource

class BaseCountryMedia(BaseResource):
    field_map = {
        "name": "name",
        "img": "img",
        "year": "year",
        "info": "info"
    }