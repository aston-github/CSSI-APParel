from seed_function import UserProfile, Item, Like

def seed_data():
    nancy = UserProfile(user_id = "nancy", first_name = 'Nancy', last_name = 'Sarabia', email = 'nanccysarabiaa12@gmail.com').put()
    xoshil = UserProfile(user_id = "xoshil", first_name = 'Xoshil', last_name = 'Chen-Marquez', email = 'xoshilcm@gmail.com').put()
    aston = UserProfile(user_id = "aston", first_name = 'Aston', last_name = 'Yong', email = 'astontyong@gmail.com').put()

    nancy_item1 = Item(img_url = 'https://bigboze.com/wp-content/uploads/2017/08/Vintage-90s-Bootleg-Selena-T-Shirt.jpg', description = 'Vintage Selena T-Shirt, Size: Small', owner = nancy)
    xoshil_item1 = Item(img_url = 'https://auctions.c.yimg.jp/images.auctions.yahoo.co.jp/image/dr000/auc0407/users/20489ec3f1aed236c91063314c14ec48936aab30/i-img1200x842-1530700458efjyqp6130.jpg', description = 'Converse All Star Black Plaid, Size: US-7', owner = xoshil)
    item1 = Item(img_url = 'https://di2ponv0v5otw.cloudfront.net/posts/2019/05/01/5cc992fb689ebcecea8359c7/m_5cc9930c7f617f8c7af77091.jpg', description = 'Adidas Track Pants, Size: Medium')
    item2 = Item(img_url = 'http://images.backstreetmerch.com/images/products/bands/clothing/quee/bsi_quee181.jpg', description = 'Queen T-Shirt, Size: Large')
    item3 = Item(img_url = 'https://dtpmhvbsmffsz.cloudfront.net/posts/2017/12/09/5a2c3857f0137d5191019f24/m_5a2c3931291a3528c701af41.jpg', description = 'Silver Necklace')

    nancy_item1.put()
    xoshil_item1.put()
    item1.put()
    item2.put()
    item3.put()

    xoshil_like1 = Like(liker = xoshil, item = nancy_item1.key, owner = nancy).put()
    aston_like1 = Like(liker = aston, item = nancy_item1.key, owner = nancy).put()
