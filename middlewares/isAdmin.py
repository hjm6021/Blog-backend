from functools import wraps
from flask import request, abort, current_app
import jwt
from models import User


def isAdmin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        jwtAccessToken = request.cookies.get("access-token")

        decoded = jwt.decode(
            jwtAccessToken,
            current_app.config["JWT_SECRET_KEY"],
            algorithms=[current_app.config["JWT_ALGORITHM"]],
        )

        if not decoded["isAdmin"]:
            abort(403)

        return func(*args, **kwargs)

    return decorated_function
