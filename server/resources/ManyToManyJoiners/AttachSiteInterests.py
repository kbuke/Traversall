from models.SiteModel import SiteModel
from models.InterestModel import InterestModel
from resources.ManyToManyJoiners.BaseJoiners import BaseJoiners

class PostSiteInterests(BaseJoiners):
    def post(self, site_id):
        return self.post_joiners(
            first_id=site_id,
            first_model=SiteModel,
            first_model_type="Sites",
            second_id="interest_id",
            second_model=InterestModel,
            second_model_type="Interests",
            relationship="interests"
        )

class DeleteSiteInterest(BaseJoiners):
    def delete(self, site_id, interest_id):
        return self.delete_joiner(
            first_id=site_id,
            first_model=SiteModel,
            first_model_type="Site",
            second_id=interest_id,
            second_model=InterestModel,
            second_model_type="Interests",
            relationship="interests"
        )