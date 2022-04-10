from controllers.auth import Login, Logout, Check, Register
from controllers.home import HomePage
from controllers.posts import PostDetail, Posts, Tags
from controllers.image import UploadImage, GetImage
from controllers.about import AboutPage

def addResource(api):
    # Authentication Routing
    api.add_resource(Login, "/api/auth/login")
    api.add_resource(Logout, "/api/auth/logout")
    api.add_resource(Check, "/api/auth/check")
    api.add_resource(Register, "/api/auth/register")

    api.add_resource(HomePage, "/api/home")
    api.add_resource(AboutPage, "/api/about")

    api.add_resource(Posts, "/api/posts")
    api.add_resource(Tags, "/api/tags")

    api.add_resource(PostDetail, "/api/posts/<string:postId>")

    api.add_resource(UploadImage, "/api/images")
    api.add_resource(GetImage, "/api/images/<string:image>")