from controllers.auth import Login, Logout, Check, Register
from controllers.home import Home


def addResource(api):
    # Authentication Routing
    api.add_resource(Login, "/auth/login")
    api.add_resource(Logout, "/auth/logout")
    api.add_resource(Check, "/auth/check")
    api.add_resource(Register, "/auth/register")

    api.add_resource(Home, "/home")
