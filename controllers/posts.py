from flask_restful import Resource
from models import Posts
from flask import make_response, request
from middlewares.checkJwtToken import checkJwtTokenMiddleware
from middlewares.isAdmin import isAdmin


class PostList(Resource):
    def get(self):
        posts = Posts.objects
        response = make_response(posts.to_json())
        response.headers['Content-Type'] = "application/json"
        return response

    def post(self):
        pass