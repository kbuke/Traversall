import os 
from flask import request, session
from flask_restful import Resource

from config import bcrypt

class AdminLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        admin_email = os.getenv("ADMIN_EMAIL")
        admin_password = os.getenv("ADMIN_PASSWORD")

        if email != admin_email or not bcrypt.check_password_hash(admin_password, password):
            return {"error": "Invalud email or password"}, 401

        session["is_admin"] = True
        return{
            "email": admin_email,
            "is_admin": True
        }, 200

class AdminLogout(Resource):
    def delete(self):
        session.pop("is_admin", None)
        return {}, 204

class AdminCheckSession(Resource):
    def get(self):
        if not session.get("is_admin"):
            return {"error": "Not logged in"}, 401 
        return{
            "email": os.getenv("ADMIN_EMAIL"), "is_admin": True
        }, 200
