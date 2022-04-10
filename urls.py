from controllers.auth import Login, Logout, Check, Register
from controllers.home import HomePage
from controllers.posts import PostDetail, Posts, Tags
from controllers.image import UploadImage, GetImage

def addResource(api):
    # Authentication Routing
    api.add_resource(Login, "/auth/login")
    api.add_resource(Logout, "/auth/logout")
    api.add_resource(Check, "/auth/check")
    api.add_resource(Register, "/auth/register")

    api.add_resource(HomePage, "/home")

    api.add_resource(Posts, "/posts")
    api.add_resource(Tags, "/tags")

    api.add_resource(PostDetail, "/posts/<string:postId>")

    api.add_resource(UploadImage, "/images")
    api.add_resource(GetImage, "/images/<string:image>")