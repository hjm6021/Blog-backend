from mongoengine import *


class User(Document):
    username = StringField(max_length=50, required=True, unique=True)
    password = StringField(required=True)
    isAdmin = BooleanField(default=False, required=True)