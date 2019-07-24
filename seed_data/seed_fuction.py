from google.appengine.ext import ndb

class User(ndb.Model):
    user_id = ndb.IntegerProperty(required = True)
    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)

class Item(ndb.Model):
    img_url = ndb.StringProperty(required = True)
    description = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(User)
