from flask import abort, make_response, request, current_app, g
from flask_restful import Resource
from lib import authAPI
import jwt, bcrypt, json
from models import User
from middlewares.checkJwtToken import checkJwtTokenMiddleware

salt = bcrypt.gensalt(rounds=10, prefix=b'2a')

def generateJwtToken(payload):
    jwtToken = jwt.encode(
        payload,
        current_app.config["JWT_SECRET_KEY"],
        current_app.config["JWT_ALGORITHM"],
    )
    return jwtToken


class Login(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        
        # Validate username and password parameters
        if not username or not password:
            abort(400)

        user = User.objects(username=username).first()
        if not user:
            abort(401)

        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            abort(401)

        # Generate JWT Token and Set cookies with JWT Token
        del user.password

        jwtToken = generateJwtToken(json.loads(user.to_json()))

        response = make_response(user.to_json())
        response.headers['Content-Type'] = "application/json"
        response.set_cookie(
            key="access-token",
            value=jwtToken,
            max_age=60 * 60 * 24 * 1,
            httponly=True
        )

        return response

class Register(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")

        # Validate username and password parameters
        if not username or not password:
            abort(400)

        user = User.objects(username=username).first()
        if user:
            abort(409)
        try:
            user = User()    
            user.username = username
            user.password = bcrypt.hashpw(password.encode(), salt).decode('utf-8')
            user.save()  
        except:
            abort(500)

        return "Registered Sucessfully", 200

class Logout(Resource):
    def post(self):
        response = make_response('')
        response.status_code = 204
        response.set_cookie(key="access-token", expires=0)
        return response


class Check(Resource):
    @checkJwtTokenMiddleware
    def get(self):
        g.response = g.loginedUser
        return g.response
