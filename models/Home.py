from mongoengine import *


class Home(Document):
    description = StringField(required=True)

    meta = {"collection": "home"}
