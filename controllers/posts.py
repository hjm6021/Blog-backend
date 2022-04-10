from flask_restful import Resource
from models import Post, User
from flask import make_response, request, jsonify, abort, g
from middlewares.checkJwtToken import checkJwtTokenMiddleware
from middlewares.isAdmin import isAdmin

class PostDetail(Resource):
    def get(self, postId):
        try:
            post = Post.objects(id=postId).first()
        except:
            abort(404)

        response = make_response(post.to_json())
        response.headers['Content-Type'] = "application/json"
        return response

    @checkJwtTokenMiddleware    
    @isAdmin
    def patch(self, postId):
        title = request.json.get('title')
        body = request.json.get('body')
        tags = request.json.get('tags')
        try:
            post = Post.objects(id=postId).first()
            post.title = title
            post.body = body
            post.tags = tags
            post.save()
        except:
            abort(500)

        response = make_response("Edited Successfully")
        return response
        
    @checkJwtTokenMiddleware    
    @isAdmin
    def delete(self, postId):
        try:
            post = Post.objects(id=postId).first()
            post.delete()
        except:
            abort(500)

        return "", 204
    
class Posts(Resource):
    def get(self):
        tag = request.args.get('tag')

        if tag:
            posts = Post.objects(tags__contains=tag).order_by('-publishedDate')
        else:
            posts = Post.objects().all().order_by('-publishedDate')

        response = make_response(posts.to_json())
        response.headers['Content-Type'] = "application/json"
        return response

    @checkJwtTokenMiddleware    
    @isAdmin
    def post(self):
        title = request.json.get('title')
        body = request.json.get('body')
        tags = request.json.get('tags')

        try:
            post = Post(title=title, body=body, tags=tags, user=g.loginedUser)
            post.save()
        except:
            abort(500)

        response = make_response("Posted Successfully")
        return response

class Tags(Resource):
    def get(self):
        posts = Post.objects().values_list('tags')
        flat_list = [item for sublist in posts for item in sublist]
        
        tags = list(set(flat_list))

        response = make_response(jsonify(sorted(tags)))
        response.headers['Content-Type'] = "application/json"
        return response