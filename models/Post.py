from mongoengine import *
import datetime
from . import User

class Post(Document):
    title = StringField(max_length=50, required=True)
    body = StringField()
    tags = ListField(StringField())
    user = ReferenceField(User)
    publishedDate = DateTimeField(default=datetime.datetime.utcnow, required=True)

    meta = {"collection": "posts"}

