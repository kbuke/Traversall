from config import app, api

from resources.AdminLogin import AdminLogin, AdminCheckSession, AdminLogout
from resources.Continents import AllContinents, SpecificContinent
from resources.Countries import AllCountries, SpecificCountry
from resources.CountriesContinents import AllCountriesContinents, SpecificCountriesContinents
from resources.Language import AllLanguages, SpecificLanguages
from resources.CountriesLanguages import AllCountriesLanguages, SpecificCountryLanguages
from resources.OtherLocations import AllOtherLocations, SpecificOtherLocation

api.add_resource(AdminLogin, "/admin/login")
api.add_resource(AdminLogout, "/admin/logout")
api.add_resource(AdminCheckSession, "/admin/checksession")

api.add_resource(AllContinents, "/continents")
api.add_resource(SpecificContinent, "/continents/<int:id>")

api.add_resource(AllCountries, "/countries")
api.add_resource(SpecificCountry, "/countries/<int:id>")

api.add_resource(AllCountriesContinents, "/countriescontinents")
api.add_resource(SpecificCountriesContinents, "/countriescontinents/<int:id>")

api.add_resource(AllLanguages, "/languages")
api.add_resource(SpecificLanguages, "/languages/<int:id>")

api.add_resource(AllCountriesLanguages, "/countrieslanguages")
api.add_resource(SpecificCountryLanguages, "/countrieslanguages/<int:id>")

api.add_resource(AllOtherLocations, "/otherlocations")
api.add_resource(SpecificOtherLocation, "/otherlocations/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)