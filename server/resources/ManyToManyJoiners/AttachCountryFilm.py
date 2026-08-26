from models.CountryMedia.FilmTvModel import FilmTvModel
from models.LocationModels.CountryModel import CountryModel
from resources.ManyToManyJoiners.BaseJoiners import BaseJoiners

class PostCountryFilm(BaseJoiners):
    def post(self, country_id):
        return self.post_joiners(
            first_id=country_id,
            first_model=CountryModel,
            first_model_type="Country",
            second_id="filmId",
            second_model=FilmTvModel,
            second_model_type="Film/TV",
            relationship="media"
        )

class DeleteCountryFilm(BaseJoiners):
    def delete(self, country_id, film_id):
        return self.delete_joiner(
            first_id=country_id,
            first_model=CountryModel,
            first_model_type="Country",
            second_id=film_id,
            second_model=FilmTvModel,
            second_model_type="Film/TV",
            relationship="media"
        )