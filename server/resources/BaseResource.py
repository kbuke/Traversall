from flask import make_response, request
from flask_restful import Resource

from sqlalchemy.exc import IntegrityError

from config import db 

from functions.create_wishlist_for_user import create_wishlist_for_user

class BaseResource(Resource):
    model = None 

    def prepare_data(self, data):
        return data 

    # GET all instances of a model
    def get_all(self):
        records = [
            record.to_dict() for record in self.model.query.all()
        ]
        return records, 200 

    # GET a specific instance of a model
    def get_specific(self, id):
        record = self.model.query.filter(self.model.id == id).first()
        if not record:
            return{"error": f"{self.model.__name__} {id} not found"}, 404
        return make_response(record.to_dict(), 200)

    # POST a new instance to a model
    def post_instance(
            self,
            create_wishlist = False
    ):
        data = request.get_json()

        if not data:
            return{"error": "Missing JSON Data"}, 404 

        mapped_data = {} # check data being passed in-line with model-attributes

        for key, value in data.items():
            mapped_key = self.field_map.get(key, key)
            mapped_data[mapped_key] = value
        try:
            mapped_data = self.prepare_data(mapped_data)

            new_record = self.model(**mapped_data) # same as **kwargs

            if hasattr(new_record, "validate_unique"):
                new_record.validate_unique()

            db.session.add(new_record)
            db.session.commit()

            return new_record.to_dict(), 201
        except(ValueError, IntegrityError) as e:
            db.session.rollback()
            return {"error": [str(e)]}, 400

    # PATCH an existing instance
    def patch_instance(self, id, data = None):
        record = self.model.query.filter(self.model.id == id).first()
        if data is None:
            data = request.get_json()

        if not record:
            return{"error": f"{self.model.__name__} {id} not registeres"}, 404 

        try:
            mapped_data = {}
            for key, value in data.items():
                mapped_key = getattr(self, "field_map", {}).get(key, key)
                mapped_data[mapped_key] = value 

            mapped_data = self.prepare_data(mapped_data)

            for attr, val in mapped_data.items():
                setattr(record, attr, val)

            db.session.commit()
            return make_response(record.to_dict(), 202)

        except(ValueError, IntegrityError) as e:
            db.session.rollback()
            return{"error": [str(e)]}, 400

    # DELETE an existing instance
    def delete_instance(self, id):
        record = self.model.query.filter(self.model.id == id).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            return{"message": f"{self.model.__name__} {id} Deleted"}, 200 
        else:
            return {"error": f"{self.model.__name__} {id} Not Found"}, 404