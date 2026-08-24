# resources/CountryContinentLinks.py
from flask import request
from resources.ManyToManyJoiners.BaseJoiners import BaseJoiners
from config import db
from models.LocationModels.CountryModel import CountryModel
from models.LocationModels.ContinentModel import ContinentModel

class PostCountryContinent(BaseJoiners):
    def post(self, country_id):
        return self.post_joiners(
            first_id=country_id,
            first_model=CountryModel,
            first_model_type="Country",
            second_id="continent_id",
            second_model=ContinentModel,
            second_model_type="Continent",
            relationship="continents"
        )

class DeleteCountryContinent(BaseJoiners):
    def delete(self, country_id, continent_id):
        return self.delete_joiner(
            first_id=country_id,
            first_model=CountryModel,
            first_model_type="Country",
            second_id=continent_id,
            second_model=ContinentModel,
            second_model_type="Continent",
            relationship="continents"
        )