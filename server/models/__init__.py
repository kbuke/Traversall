# models/__init__.py
# Import every model so its table registers in db.metadata,
# regardless of whether the model has its own resource/routes.

from models.UserModels.BaseUserModel import BaseUserModel

from models.LocationModels.LocationParentModel import LocationParentModel
from models.LocationModels.ContinentModel import ContinentModel
from models.LocationModels.CountryModel import CountryModel
from models.LocationModels.OtherLocationModel import OtherLocationModel

from models.SiteModel import SiteModel
# from models.BusinessModel import BusinessModel  # once it exists

from models.WishlistModels.WishlistModel import WishlistModel
from models.WishlistModels.WishlistItemModel import WishlistItemModel
from models.WishlistModels.TagModel import TagModel

# add InterestModel, LanguagesModel, etc.