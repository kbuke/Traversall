from models.CountryMedia.SongModel import SongModel
from resources.CountryMedia.BaseCountryMedia import BaseCountryMedia

class BaseSong(BaseCountryMedia):
    model = SongModel

    field_map = {
        **BaseCountryMedia.field_map,
        "length": "length",
        "artist": "artist",
        "featuring": "featuring"
    }

class AllSongs(BaseSong):
    def get(self):
        return self.get_all()

    def post(self):
        return self.post_instance()

class SpecificSong(BaseSong):
    def get(self, id):
        return self.get_specific(id)

    def patch(self, id):
        return self.patch_instance(id)

    def delete(self, id):
        return self.delete_instance(id)