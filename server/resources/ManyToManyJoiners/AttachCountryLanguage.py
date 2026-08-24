# resources/CountryContinentLinks.py
from models.LocationModels.CountryModel import CountryModel
from models.LanguagesModel import LanguagesModel
from resources.ManyToManyJoiners.BaseJoiners import BaseJoiners

class PostCountryLanguage(BaseJoiners):
    def post(self, country_id):
        return self.post_joiners(
            first_id=country_id,
            first_model=CountryModel,
            first_model_type="Country",
            second_id="languages_id",
            second_model=LanguagesModel,
            second_model_type="Language",
            relationship="languages"
        )

class DeleteCountryLanguage(BaseJoiners):
    def delete(self, country_id, languages_id):
        return self.delete_joiner(
            first_id=country_id,
            first_model=CountryModel,
            first_model_type="Country",
            second_id=languages_id,
            second_model=LanguagesModel,
            second_model_type="Languages",
            relationship="languages"
        )