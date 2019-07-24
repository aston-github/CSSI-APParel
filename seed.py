from seed_function import User, Item

def seed_data():
    nancy_key = User(user_id = 001, first_name = 'Nancy', last_name = 'Sarabia', email = 'nanccysarabiaa12@gmail.com').put()
    xoshil_key = User(user_id = 002, first_name = 'Xoshil', last_name = 'Chen-Marquez', email = 'xoshilcm@gmail.com').put()

    nancy_item1 = Item(img_url = 'https://bigboze.com/wp-content/uploads/2017/08/Vintage-90s-Bootleg-Selena-T-Shirt.jpg', description = 'Vintage Selena T-Shirt, Size: Small', owner = nancy_key)
    xoshil_item1 = Item(img_url = 'https://auctions.c.yimg.jp/images.auctions.yahoo.co.jp/image/dr000/auc0407/users/20489ec3f1aed236c91063314c14ec48936aab30/i-img1200x842-1530700458efjyqp6130.jpg', description = 'Converse All Star Black Plaid, Size: US-7', owner = xoshil_key)
    nancy_item1.put()
    xoshil_item1.put()
