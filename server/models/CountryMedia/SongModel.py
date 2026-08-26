from models.CountryMedia.MediaModel import MediaModel

from config import db 

from sqlalchemy.orm import validates

from functions.check_integer_greater_than_zero import check_integer_greater_than_zero
from functions.check_input_integer import check_input_integer

class SongModel(MediaModel):

    length = db.Column(db.Float, nullable=True)
    artist = db.Column(db.String, nullable=True)
    featuring = db.Column(db.String, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "Music"
    }

    @validates("length")
    def validate_length(self, key, value):

        if value is not None:
            if value <= 0:
                raise ValueError(
                    "Song length must be greater than 0"
                )

        return value

    @validates("artist")
    def validate_artist(self, key, value):

        if value is not None and not isinstance(value, str):
            raise ValueError(
                "Artist must be a string"
            )

        return value

    def validate_song(self):

        if self.length is None:
            raise ValueError(
                "Music must have a length"
            )

        if self.artist is None:
            raise ValueError(
                "Music must have an artist"
            )
