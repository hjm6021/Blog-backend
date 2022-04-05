from functools import wraps
from flask import request, abort, g, current_app, make_response
import jwt

def checkJwtTokenMiddleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        jwtAccessToken = request.cookies.get("access-token")
    
        if jwtAccessToken is None:
            abort(401)

        try:
            decoded = jwt.decode(
                jwtAccessToken,
                current_app.config["JWT_SECRET_KEY"],
                algorithms=[current_app.config["JWT_ALGORITHM"]],
            )    
            
            g.loginedUser = decoded
            g.response = make_response()
            g.response.set_cookie(
                key="access-token",
                value=jwtAccessToken,
                max_age=60 * 60 * 24 * 1,
                httponly=True
            )

        except:
            abort(500)

        return func(*args, **kwargs)

    return decorated_function
