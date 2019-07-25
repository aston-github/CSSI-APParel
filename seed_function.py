from google.appengine.ext import ndb

class UserProfile(ndb.Model):
    user_id = ndb.StringProperty(required = True)
    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)

class Item(ndb.Model):
    img_url = ndb.StringProperty(required = True)
    description = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(UserProfile)

class Like(ndb.Model):
    item = ndb.KeyProperty(Item)
    owner = ndb.KeyProperty(UserProfile)
    liker = ndb.KeyProperty(UserProfile)
