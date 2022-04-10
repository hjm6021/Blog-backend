from flask_restful import Resource
from models import About
from flask import make_response, request
from middlewares.checkJwtToken import checkJwtTokenMiddleware
from middlewares.isAdmin import isAdmin


class AboutPage(Resource):
    def get(self):
        about = About.objects.get().to_json()
        response = make_response(about)
        return response

    @checkJwtTokenMiddleware
    @isAdmin
    def put(self):
        _id = request.json.get("id")
        editor = request.json.get("editor")

        About.objects(pk=_id["$oid"]).update_one(set__description=editor)

        return "", 204
