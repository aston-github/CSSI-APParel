import webapp2
import jinja2
import os

class ModelWithUser(ndb.Model):
    user_id = ndb.StringProperty()
    color = ndb.StringProperty()


    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).get()
