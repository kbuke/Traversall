from config import app, api

from resources.AdminLogin import AdminLogin, AdminCheckSession, AdminLogout
from resources.Continents import AllContinents, SpecificContinent

api.add_resource(AdminLogin, "/admin/login")
api.add_resource(AdminLogout, "/admin/logout")
api.add_resource(AdminCheckSession, "/admin/checksession")

api.add_resource(AllContinents, "/continents")
api.add_resource(SpecificContinent, "/continents/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)