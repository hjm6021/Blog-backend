from controllers.auth import Login, Logout, Check, Register
from controllers.home import Home
from controllers.posts import PostList

def addResource(api):
    # Authentication Routing
    api.add_resource(Login, "/auth/login")
    api.add_resource(Logout, "/auth/logout")
    api.add_resource(Check, "/auth/check")
    api.add_resource(Register, "/auth/register")

    api.add_resource(Home, "/home")

    api.add_resource(PostList, "/posts")
