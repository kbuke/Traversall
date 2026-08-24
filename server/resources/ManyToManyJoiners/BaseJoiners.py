from flask import request
from flask_restful import Resource
from config import db 

from flask import request
from flask_restful import Resource
from config import db


class BaseJoiners(Resource):

    def post_joiners(
        self,
        first_id,
        first_model,
        first_model_type,
        second_id,
        second_model,
        second_model_type,
        relationship
    ):
        data = request.get_json()

        if not data:
            return {"error": "Missing JSON data"}, 400

        second_id = data.get(second_id)

        first = first_model.query.get(first_id)
        second = second_model.query.get(second_id)

        if not first:
            return {
                "error": f"{first_model_type} {first_id} not found"
            }, 404

        if not second:
            return {
                "error": f"{second_model_type} {second_id} not found"
            }, 404

        related_objects = getattr(first, relationship)

        if second in related_objects:
            return {
                "error": f"{first_model_type} and {second_model_type} already linked"
            }, 400

        related_objects.append(second)

        db.session.commit()

        return first.to_dict(), 201

    def delete_joiner(
        self,
        first_id,
        first_model,
        first_model_type,
        second_id,
        second_model,
        second_model_type,
        relationship
    ):

        first = first_model.query.get(first_id)
        second = second_model.query.get(second_id)

        if not first:
            return {
                "error": f"{first_model_type} {first_id} not found"
            }, 404

        if not second:
            return {
                "error": f"{second_model_type} {second_id} not found"
            }, 404

        related_objects = getattr(first, relationship)

        if second not in related_objects:
            return {"error": "Link not found"}, 404

        related_objects.remove(second)

        db.session.commit()

        return {"message": "Unlinked"}, 200