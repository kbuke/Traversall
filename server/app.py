from config import app, api
import models

from resources.AdminLogin import AdminLogin, AdminCheckSession, AdminLogout
from resources.Continents import AllContinents, SpecificContinent
from resources.Countries import AllCountries, SpecificCountry
from resources.Language import AllLanguages, SpecificLanguages
from resources.OtherLocations import AllOtherLocations, SpecificOtherLocation
from resources.Interests import AllInterests, SpecificInterest
from resources.Sites import AllSites, SpecificSite
from resources.User import AllUsers, SpecificUser
from resources.Wishlist import SpecificWishlist
from resources.WishListItem import AllWishListItems, SpecificWishlistItem
from resources.ManyToManyJoiners.AttachCountryContinent import PostCountryContinent, DeleteCountryContinent
from resources.ManyToManyJoiners.AttachCountryLanguage import PostCountryLanguage, DeleteCountryLanguage
from resources.ManyToManyJoiners.AttachSiteInterests import PostSiteInterests, DeleteSiteInterest
from resources.Business import AllBusinesses, SpecificBusiness
from resources.FilmTvShows import AllFilmTv, SpecificFilmTv
from resources.ManyToManyJoiners.AttachCountryFilm import PostCountryFilm, DeleteCountryFilm
from resources.Song import AllSongs, SpecificSong

api.add_resource(AdminLogin, "/admin/login")
api.add_resource(AdminLogout, "/admin/logout")
api.add_resource(AdminCheckSession, "/admin/checksession")

api.add_resource(AllContinents, "/continents")
api.add_resource(SpecificContinent, "/continents/<int:id>")

api.add_resource(AllCountries, "/countries")
api.add_resource(SpecificCountry, "/countries/<int:id>")

api.add_resource(AllLanguages, "/languages")
api.add_resource(SpecificLanguages, "/languages/<int:id>")

api.add_resource(AllOtherLocations, "/otherlocations")
api.add_resource(SpecificOtherLocation, "/otherlocations/<int:id>")

api.add_resource(AllInterests, "/interests")
api.add_resource(SpecificInterest, "/interests/<int:id>")

api.add_resource(AllSites, "/sites")
api.add_resource(SpecificSite, "/sites/<int:id>")

api.add_resource(AllUsers, "/users")
api.add_resource(SpecificUser, "/users/<int:id>")

api.add_resource(SpecificWishlist, "/wishlist/<int:id>")

api.add_resource(AllWishListItems, "/wishlistitems")
api.add_resource(SpecificWishlistItem, "/wishlistitems/<int:id>")

api.add_resource(PostCountryContinent, "/countries/<int:country_id>/continents")
api.add_resource(DeleteCountryContinent, "/countries/<int:country_id>/continents/<int:continent_id>")

api.add_resource(PostCountryLanguage, "/countries/<int:country_id>/languages")
api.add_resource(DeleteCountryLanguage, "/countries/<int:country_id>/languages/<int:languages_id>")

api.add_resource(PostSiteInterests, "/sites/<int:site_id>/interests")
api.add_resource(DeleteSiteInterest, "/sites/<int:site_id>/interests/<int:interest_id>")

api.add_resource(AllBusinesses, "/businesses")
api.add_resource(SpecificBusiness, "/businesses/<int:id>")

api.add_resource(AllFilmTv, "/films")
api.add_resource(SpecificFilmTv, "/films/<int:id>")

api.add_resource(PostCountryFilm, "/countries/<int:country_id>/films")
api.add_resource(DeleteCountryFilm, "/countries/<int:country_id>/films/<int:film_id>")

api.add_resource(AllSongs, "/songs")
api.add_resource(SpecificSong, "/songs/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)