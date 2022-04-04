from flask_restful import Resource
from models import HomePage
from flask import make_response, request
from middlewares.checkJwtToken import checkJwtTokenMiddleware
from middlewares.isAdmin import isAdmin


class Home(Resource):
    @checkJwtTokenMiddleware
    def get(self):
        home = HomePage.objects.get().to_json()
        response = make_response(home)
        return response

    @checkJwtTokenMiddleware
    @isAdmin
    def put(self):
        _id = request.json.get("id")
        editor = request.json.get("editor")

        HomePage.objects(pk=_id["$oid"]).update_one(set__description=editor)

        return "", 204
