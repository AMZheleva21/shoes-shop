class Product:
    def __init__(self, product_id, name, description, color, sizes, price, stock, category, subcategory):
        self.id = product_id
        self.name = name
        self.description = description
        self.color = color
        self.sizes = sizes
        self.price = price
        self.stock = stock
        self.category = category
        self.subcategory = subcategory

    def __repr__(self):
        return f"<Product {self.name} ({self.color}) - {self.price} лв. [{self.category}/{self.subcategory}]>"


products = [
    Product(1, "Nike Air Max", "Спортни маратонки", "черен", [42, 43, 44], 199.99, 10, "мъжки", "спортни"),
    Product(2, "Adidas Ultraboost", "Бягащи обувки", "сив", [41, 42, 43, 44], 229.99, 7, "мъжки", "спортни"),
    Product(3, "Puma RS-X", "Ретро маратонки", "червен", [40, 41, 42, 43], 179.99, 12, "мъжки", "спортни"),

    Product(4, "Clarks Desert Boot", "Класически чизми", "кафяв", [41, 42, 43], 159.99, 6, "мъжки", "официални"),
    Product(5, "Ecco Soft 7", "Официални обувки", "черен", [42, 43, 44], 189.99, 8, "мъжки", "официални"),
    Product(6, "Geox Nebula", "Дамски официални", "тъмно сив", [39, 40, 41, 42], 169.99, 9, "мъжки", "официални"),

    Product(7, "Vans Old Skool", "Скетърски обувки", "черно-бяло", [41, 42, 43, 44], 119.99, 15, "мъжки", "ежедневни"),
    Product(8, "Converse Chuck Taylor", "Класически кецове", "син", [40, 41, 42, 43], 99.99, 20, "мъжки", "ежедневни"),
    Product(9, "New Balance 574", "Ежедневни маратонки", "сив", [41, 42, 43, 44], 139.99, 11, "мъжки", "ежедневни"),

    Product(10, "Nike Revolution", "Фитнес обувки", "розов", [36, 37, 38, 39], 129.99, 14, "женски", "спортни"),
    Product(11, "Adidas Superstar", "Класически маратонки", "бял", [36, 37, 38, 39], 149.99, 8, "женски", "спортни"),
    Product(12, "Reebok Nano", "Кросфит обувки", "лилав", [37, 38, 39, 40], 179.99, 6, "женски", "спортни"),

    Product(13, "Salvatore Ferragamo", "Елегантни балетки", "черен", [36, 37, 38], 299.99, 4, "женски", "официални"),
    Product(14, "Michael Kors", "Високи токчета", "бежов", [37, 38, 39], 249.99, 5, "женски", "официални"),
    Product(15, "Nine West", "Официални обувки", "тъмно синьо", [36, 37, 38, 39], 159.99, 7, "женски", "официални"),

    Product(16, "Birkenstock Arizona", "Сандали", "кафяв", [36, 37, 38, 39], 89.99, 18, "женски", "ежедневни"),
    Product(17, "Skechers Go Walk", "Удобни разходки", "сребърен", [37, 38, 39, 40], 109.99, 12, "женски", "ежедневни"),
    Product(18, "Tommy Hilfiger", "Есенни ботуши", "бордо", [36, 37, 38], 199.99, 9, "женски", "ежедневни"),

    Product(19, "Puma Smash", "Удобни за всеки ден", "син", [28, 29, 30, 31], 79.99, 15, "детски", "спортни"),
    Product(20, "Nike Junior Revolution", "Детски маратонки", "зелен", [27, 28, 29, 30], 89.99, 13, "детски",
            "спортни"),
    Product(21, "Adidas Kids Court", "Тениски", "розов", [26, 27, 28, 29], 69.99, 17, "детски", "спортни"),

    Product(22, "Clarks School Shoes", "Училищни обувки", "черен", [28, 29, 30, 31], 59.99, 20, "детски", "официални"),
    Product(23, "Geox Kids", "Детски официални", "кафяв", [27, 28, 29, 30], 79.99, 11, "детски", "официални"),
    Product(24, "Ecco Soft Kids", "Удобни официални", "синьо", [26, 27, 28, 29], 89.99, 8, "детски", "официални"),

    Product(25, "Crocs Kids", "Пластмасови обувки", "розов", [25, 26, 27, 28], 39.99, 25, "детски", "ежедневни"),
    Product(26, "Skechers Twinkle Toes", "Светещи обувки", "лилав", [26, 27, 28, 29], 69.99, 14, "детски", "ежедневни"),
    Product(27, "Converse Kids", "Мини кецове", "червен", [27, 28, 29, 30], 59.99, 16, "детски", "ежедневни")
]


def get_all_products():
    return products


def get_product_by_id(product_id):
    for p in products:
        if p.id == product_id:
            return p
    return None


def add_product(name, description, color, sizes, price, stock, category, subcategory):
    new_id = max([p.id for p in products], default=0) + 1
    new_product = Product(new_id, name, description, color, sizes, price, stock, category, subcategory)
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


