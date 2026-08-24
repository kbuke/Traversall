# from resources.BaseResource import BaseResource
# from models.SitesInterestsModel import SitesInterestModel

# class AllSitesInterests(BaseResource):
#     model = SitesInterestModel

#     field_map = {
#         "interestId": "interest_id",
#         "siteId": "site_id"
#     }

#     def get(self):
#         return self.get_all()

#     def post(self):
#         return self.post_instance()

# class SpecificSiteInterest(BaseResource):
#     model = SitesInterestModel

#     field_map = {
#         "interestId": "interest_id",
#         "siteId": "site_id"
#     }

#     def get(self, id):
#         return self.get_specific(id)

#     def patch(self, id):
#         return self.patch_instance(id)

#     def delete(self, id):
#         return self.delete_instance(id)