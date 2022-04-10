from flask_restful import Resource
from flask import send_file, current_app, request, make_response, abort
import os
from datetime import datetime
from middlewares.checkJwtToken import checkJwtTokenMiddleware
from middlewares.isAdmin import isAdmin

class UploadImage(Resource):
    @checkJwtTokenMiddleware
    @isAdmin
    def post(self):
        if not request.files['file']:
            abort(400)

        image = request.files['file']
        filename = datetime.today().strftime('%Y%m%d') + "-" + image.filename
        path = os.path.join(current_app.config["UPLOADED_IMAGE_FOLDER"], filename)
        if os.path.exists(path):
            abort(409)

        image.save(path)
        return make_response(current_app.config["URL"]+"images/"+filename)

class GetImage(Resource):
    def get(self, image):
        imageFile = os.path.join(current_app.config["UPLOADED_IMAGE_FOLDER"], image)
        if not os.path.exists(imageFile):
            abort(404)

        return send_file(imageFile)



