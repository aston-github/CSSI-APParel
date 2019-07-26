import webapp2
import os
import jinja2
import time
from seed import seed_data
from seed_function import UserProfile, Item, Like
from google.appengine.api import users

from google.appengine.ext import ndb

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Feed(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_dir.get_template("feed.html")

        user = users.get_current_user()
        potential_profiles = UserProfile.query(UserProfile.user_id == user.user_id()).fetch(1)
        if not potential_profiles:
            UserProfile(user_id=user.user_id(), first_name=user.nickname(), last_name=user.nickname(), email=user.email()).put()
            time.sleep(0.1)
        profile = UserProfile.query(UserProfile.user_id == user.user_id()).fetch(1)[0]
        item_display = Item.query().filter(Item.owner != profile.key).fetch()[0]
        # maybe use random integer for random picture (need to update seed if yes)

        my_feed_dict = {
        "image_url": item_display.img_url,
        "item_description": item_display.description,
        "item_id": item_display.key.urlsafe(),
        }
        self.response.write(template.render(my_feed_dict))
        # item gets the item liked
        # liker gets "who is the liker?"
        # Like saves the like info

class LikeHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        item = ndb.Key(urlsafe=self.request.get('item_id')).get()
        liker = UserProfile.query(UserProfile.user_id == user.user_id()).fetch(1)[0]
        item_owner_key = item.owner
        Like(item=item.key, owner=item_owner_key, liker=liker.key).put()
        mutual_likes = Like.query().filter(Like.liker == item_owner_key and Like.owner == liker.key).fetch()
        if mutual_likes:
            self.redirect('/match?matched_user_id=' + item_owner_key.urlsafe())
        else:
            self.redirect('/')

class MatchHandler(webapp2.RequestHandler):
    def get(self):
        matched_user_id = self.request.get('matched_user_id')
        matched_user = ndb.Key(urlsafe=matched_user_id).get()
        user = users.get_current_user()
        liker = UserProfile.query(UserProfile.user_id == user.user_id()).fetch(1)[0]
        self.response.write("You had a match! " + "You matched with " + str(matched_user.email))


class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()

app = webapp2.WSGIApplication([
    ('/', Feed),
    ('/seed-data', LoadDataHandler),
    ('/like', LikeHandler),
    ('/match', MatchHandler)
], debug=True)
