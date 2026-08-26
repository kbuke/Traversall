from models.CountryMedia.MediaModel import MediaModel

from config import db

from sqlalchemy.orm import validates

from functions.check_data_type_values import check_data_type_value
from functions.check_input_integer import check_input_integer
from functions.check_integer_greater_than_zero import check_integer_greater_than_zero

class FilmTvModel(MediaModel):
    # if it is a film or docu-film
    run_time = db.Column(db.Integer, nullable = True)

    # if it is a tv show or docu-show
    no_of_seasons = db.Column(db.Integer, nullable = True)
    no_of_episodes = db.Column(db.Integer, nullable = True)
    ep_time = db.Column(db.Integer, nullable = True)
    film_category = db.Column(db.String, nullable = True)

    __mapper_args__ = {
        "polymorphic_identity": "FilmTv"
    }

    @validates("film_category")
    def validate_media_type(self, key, value):
        allowed_media = ["Movie", "Documentary-Movie", "Documentary-Series", "TV-Series"]
        check_data_type_value(allowed_media, value)
        return value

    @validates("run_time")
    def validate_film_run_time(self, key, value):
        if self.film_category in {"Movie", "Documentary-Movie"}:
            if not self.run_time:
                raise ValueError("A film must have a run-time")
            check_input_integer(value)
            check_integer_greater_than_zero(value)
        return value

    @validates("no_of_seasons", "no_of_episodes", "ep_time")
    def validate_series_info(self, key, value):
        if self.film_category in {"TV-Series", "Documentary-Series"}:
            if not self.no_of_seasons or not self.no_of_episodes:
                raise ValueError("A TV-Series must have a number of seasons and episodes")
            check_input_integer(value)
            check_integer_greater_than_zero(value)
        return value