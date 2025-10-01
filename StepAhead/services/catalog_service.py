class Product:
    def __init__(self, product_id, name, description, color, sizes, price, stock, category, subcategory,image_url=None):
        self.id = product_id
        self.name = name
        self.description = description
        self.color = color
        self.sizes = sizes
        self.price = price
        self.stock = stock
        self.category = category
        self.subcategory = subcategory
        self.image_url = image_url or "/static/images/default-shoe.png"


    def __repr__(self):
        return f"<Product {self.name} ({self.color}) - {self.price} лв. [{self.category}/{self.subcategory}]>"


products = [
    Product(1, "Nike Air Max", "Спортни маратонки", "черен", [42, 43, 44], 199.99, 10, "мъжки", "спортни","https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/8fe9105d-c364-4ac3-853c-8693e6fc623a/W+AIR+MAX+PLUS.png"),
    Product(2, "Adidas Ultraboost", "Бягащи обувки", "сив", [41, 42, 43, 44], 229.99, 7, "мъжки", "спортни","https://i1.t4s.cz//products/gv8743/adidas-ultraboost-5-0-dna-755405-gv8743-960.webp"),
    Product(3, "Puma RS-X", "Ретро маратонки", "червен", [40, 41, 42, 43], 179.99, 12, "мъжки", "спортни","https://img.eobuwie.cloud/eob_product_512w_512h(d/2/e/8/d2e857140ecffd70dd284c5f97a8e183c48224c5_03_4065454854216_rz.jpg,jpg)/snikrsi-puma-rs-x-efekt-prm-390776-10-frosted-ivory-puma-black-0000302585717.jpg"),

    Product(4, "Clarks Desert Boot", "Класически чизми", "кафяв", [41, 42, 43], 159.99, 6, "мъжки", "официални","https://img.eobuwie.cloud/eob_product_512w_512h(f/9/b/a/f9ba789b5357d35b7e133756d62c3d060212879b_0000197778614_clarks_desert_boot_sand_ws_01,jpg)/turisticheski-obuvki-clarks-desert-boot-261069414-bezhov-0000197778614.jpg"),
    Product(5, "Ecco Soft 7", "Официални обувки", "черен", [42, 43, 44], 189.99, 8, "мъжки", "официални","https://shop-ecco.bg/uploads/product-image/image/original/470824-50104-m.jpg"),
    Product(6, "Geox Nebula", "Дамски официални", "тъмно сив", [39, 40, 41, 42], 169.99, 9, "мъжки", "официални","https://i.sportisimo.com/products/images/1357/1357405/700x700/geox-u-nebula-dblu_5.jpg"),

    Product(7, "Vans Old Skool", "Скетърски обувки", "черно-бяло", [41, 42, 43, 44], 119.99, 15, "мъжки", "ежедневни","https://img.eobuwie.cloud/eob_product_256w_256h(8/7/c/5/87c5cdb0285d4f5fe6b9c464f015493589b99041_0000199854101_02_fp.jpg,jpg)/gumenki-vans-old-skool-platfor-vn0a3b3uy28-black-white.jpg"),
    Product(8, "Converse Chuck Taylor", "Класически кецове", "син", [40, 41, 42, 43], 99.99, 20, "мъжки", "ежедневни","https://www.converse.com/dw/image/v2/BCZC_PRD/on/demandware.static/-/Sites-cnv-master-catalog/default/dw3931bb17/images/a_107/M9160_A_107X1.jpg?sw=964"),
    Product(9, "New Balance 574", "Ежедневни маратонки", "сив", [41, 42, 43, 44], 139.99, 11, "мъжки", "ежедневни","https://img.eobuwie.cloud/eob_product_256w_256h(b/5/b/e/b5bea83f8e4a47c2674268b58bb07b719cc42731_20_0197967950803.jpg,jpg)/snikrsi-new-balance-u574yce-cheren-0000305310132.jpg"),

    Product(10, "Nike Revolution", "Фитнес обувки", "розов", [36, 37, 38, 39], 129.99, 14, "женски", "спортни","https://s.shopsector.com/uploads/productgalleryfile/images/1200x1200/maratonki-nike-revolution-7-fb2207-001-1.jpg"),
    Product(11, "Adidas Superstar", "Класически маратонки", "бял", [36, 37, 38, 39], 149.99, 8, "женски", "спортни","https://img.eobuwie.cloud/eob_product_660w_880h(2/c/a/4/2ca4d2d28b1c6906b34986852351f479fbe76553_0000208408714_01_sw.jpg,jpg)/obuvki-adidas-superstar-w-fy4755-ftwwht-cblack-goldmt.jpg"),
    Product(12, "Reebok Nano", "Кросфит обувки", "лилав", [37, 38, 39, 40], 179.99, 6, "женски", "спортни","https://i1.t4s.cz//products/100074194/reebok-nano-x4-719244-100074197-960.webp"),

    Product(13, "Salvatore Ferragamo", "Елегантни балетки", "черен", [36, 37, 38], 299.99, 4, "женски", "официални","https://images.bloomingdalesassets.com/is/image/BLM/products/7/optimized/14584137_fpx.tif?$2014_BROWSE_FASHION$&qlt=80,0&resMode=sharp2&op_usm=1.75,0.3,2,0&fmt=jpeg&wid=342&hei=428"),
    Product(14, "Michael Kors", "Високи токчета", "бежов", [37, 38, 39], 249.99, 5, "женски", "официални","https://static.glami.bg/img/800x800bt/507215573-michael-kors-sneakers-nova-trainer-43t4nvfs2d-001-black.jpg"),
    Product(15, "Nine West", "Официални обувки", "тъмно синьо", [36, 37, 38, 39], 159.99, 7, "женски", "официални","https://img.modivo.cloud/product(5/f/c/b/5fcb45892f1c702798ef1a822e70ff692ca4aaf0_26_5905588957508.jpg,jpg)/nine-west-obuvki-na-tok-wfa3366-1-cheren-5905588957508.jpg"),

    Product(16, "Birkenstock Arizona", "Сандали", "кафяв", [36, 37, 38, 39], 89.99, 18, "женски", "ежедневни","https://s13emagst.akamaized.net/products/68485/68484429/images/res_466c6386db428af7a4897de89030399b.jpg"),
    Product(17, "Skechers Go Walk", "Удобни разходки", "сребърен", [37, 38, 39, 40], 109.99, 12, "женски", "ежедневни","https://cdn.sportdepot.bg/files/catalog/detail/124975-NVW_01.jpg"),
    Product(18, "Tommy Hilfiger", "Есенни ботуши", "бордо", [36, 37, 38], 199.99, 9, "женски", "ежедневни","https://cdn-images.farfetch-contents.com/22/70/67/98/22706798_53027370_600.jpg"),

    Product(19, "Puma Smash", "Удобни за всеки ден", "син", [28, 29, 30, 31], 79.99, 15, "детски", "спортни","https://i.sportisimo.com/products/images/2001/2001204/700x700/puma-smash-3-0-l_2.jpg"),
    Product(20, "Nike Junior Revolution", "Детски маратонки", "зелен", [27, 28, 29, 30], 89.99, 13, "детски",
            "спортни","https://images.bike24.com/i/mb/10/78/fe/nike-revolution-7-shoes-gs-kids-black-white-hyper-pink-fb7689-002-3-1572682.jpg"),
    Product(21, "Adidas Kids Court", "Тениски", "розов", [26, 27, 28, 29], 69.99, 17, "детски", "спортни","https://cdn.sportdepot.bg/files/catalog/detail/IE1372_01.jpg"),

    Product(22, "Clarks School Shoes", "Училищни обувки", "черен", [28, 29, 30, 31], 59.99, 20, "детски", "официални","https://thegoldenboot.co.uk/image/cache/catalog/Clarks/2024/School%20shoes/26178295_GW_1-800x800.jpg"),
    Product(23, "Geox Kids", "Детски официални", "кафяв", [27, 28, 29, 30], 79.99, 11, "детски", "официални","https://www.beggshoes.com/images/products/large/geox-gisli-bu-blue-kids-boys-toddler-shoes-b551nb-c43761733826504B551NB01422C4376_01.jpg"),
    Product(24, "Ecco Soft Kids", "Удобни официални", "синьо", [26, 27, 28, 29], 89.99, 8, "детски", "официални","https://shop-ecco.bg/uploads/product-image/image/280x280/713812-01363-main3D_rendition_Screen.jpg"),

    Product(25, "Crocs Kids", "Пластмасови обувки", "розов", [25, 26, 27, 28], 39.99, 25, "детски", "ежедневни","https://www.famousfootwear.com/blob/product-images/20000/00/53/4/00534_pair_feed1000.jpg"),
    Product(26, "Skechers Twinkle Toes", "Светещи обувки", "лилав", [26, 27, 28, 29], 69.99, 14, "детски", "ежедневни","https://i.ebayimg.com/images/g/ZQsAAOSwe0tckWXe/s-l400.gif"),
    Product(27, "Converse Kids", "Мини кецове", "червен", [27, 28, 29, 30], 59.99, 16, "детски", "ежедневни","https://www.thestreets.bg/media/catalog/product/cache/2b5c0c30ec592b2d661598663b3592ba/a/0/a04292c1_g4o5h31w42n1ck21.jpg")
]


def get_all_products():
    return products


def get_product_by_id(product_id):
    for p in products:
        if p.id == product_id:
            return p
    return None


def add_product(name, description, color, sizes, price, stock, category, subcategory, image_url=None):
    new_id = max([p.id for p in products], default=0) + 1
    new_product = Product(new_id, name, description, color, sizes, price, stock, category, subcategory, image_url)
    products.append(new_product)
    return new_product


def update_product(product_id, name, description, color, sizes, price, stock, category, subcategory):
    product = get_product_by_id(product_id)
    if product:
        product.name = name
        product.description = description
        product.color = color
        product.sizes = sizes
        product.price = price
        product.stock = stock
        product.category = category
        product.subcategory = subcategory
        return True
    return False


def delete_product(product_id):
    products[:] = [p for p in products if p.id != product_id]


def search_products(query):
    query = query.lower()
    return [p for p in products if query in p.name.lower() or query in p.color.lower()]


def filter_products(min_price=None, max_price=None, size=None, in_stock=None, category=None, subcategory=None):
    filtered = products
    if min_price is not None:
        filtered = [p for p in filtered if p.price >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p.price <= max_price]
    if size is not None:
        filtered = [p for p in filtered if size in p.sizes]
    if in_stock:
        filtered = [p for p in filtered if p.stock > 0]
    if category:
        filtered = [p for p in filtered if p.category.lower() == category.lower()]
    if subcategory:
        filtered = [p for p in filtered if p.subcategory.lower() == subcategory.lower()]
    return filtered


def sort_products(products_list, by="price", descending=False):
    if by == "price":
        return sorted(products_list, key=lambda p: p.price, reverse=descending)
    elif by == "name":
        return sorted(products_list, key=lambda p: p.name.lower(), reverse=descending)
    elif by == "stock":
        return sorted(products_list, key=lambda p: p.stock, reverse=descending)
    else:
        return products_list


