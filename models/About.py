from mongoengine import *


class About(Document):
    description = StringField(required=True)

    meta = {"collection": "about"}
