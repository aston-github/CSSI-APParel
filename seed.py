from seed_function import UserProfile, Item, Like

def seed_data():
    nancy = UserProfile(user_id = "nancy", first_name = 'Nancy', last_name = 'Sarabia', email = 'nanccysarabiaa12@gmail.com').put()
    xoshil = UserProfile(user_id = "xoshil", first_name = 'Xoshil', last_name = 'Chen-Marquez', email = 'xoshilcm@gmail.com').put()
    aston = UserProfile(user_id = "aston", first_name = 'Aston', last_name = 'Yong', email = 'astontyong@gmail.com').put()

    nancy_item1 = Item(img_url = 'https://bigboze.com/wp-content/uploads/2017/08/Vintage-90s-Bootleg-Selena-T-Shirt.jpg', description = 'Vintage Selena T-Shirt, Size: Small', owner = nancy)
    xoshil_item1 = Item(img_url = 'https://auctions.c.yimg.jp/images.auctions.yahoo.co.jp/image/dr000/auc0407/users/20489ec3f1aed236c91063314c14ec48936aab30/i-img1200x842-1530700458efjyqp6130.jpg', description = 'Converse All Star Black Plaid, Size: US-7', owner = xoshil)
    nancy_item1.put()
    xoshil_item1.put()

    xoshil_like1 = Like(liker = xoshil, item = nancy_item1.key, owner = nancy).put()
    aston_like1 = Like(liker = aston, item = nancy_item1.key, owner = nancy).put()
