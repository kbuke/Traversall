from models.CountryMedia.FilmTvModel import FilmTvModel
from resources.CountryMedia.BaseCountryMedia import BaseCountryMedia

class BaseFilmTv(BaseCountryMedia):
    model = FilmTvModel

    field_map = {
        **BaseCountryMedia.field_map,
        "runTime": "run_time",
        "seasons": "no_of_seasons",
        "episodes": "no_of_episodes",
        "epTime": "ep_time",
        "filmCat": "film_category"
    }

class AllFilmTv(BaseFilmTv):
    def get(self):
        return self.get_all(
            "-countries",
        )

    def post(self):
        return self.post_instance()

class SpecificFilmTv(BaseFilmTv):
    def get(self, id):
        return self.get_specific(id)

    def patch(self, id):
        return self.patch_instance(id)

    def delete(self, id):
        return self.delete_instance(id)