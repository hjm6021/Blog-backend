from mongoengine import *
import datetime
from . import User

class Posts(Document):
    title = StringField(max_length=50, required=True, unique=True)
    body = StringField()
    tags = ListField(StringField())
    user = ReferenceField(User)
    publishedDate = DateTimeField(default=datetime.datetime.utcnow)

