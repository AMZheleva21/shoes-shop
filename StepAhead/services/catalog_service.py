class Product:
    def __init__(self, product_id, name, description, color, sizes, price, stock):
        self.id = product_id
        self.name = name
        self.description = description
        self.color = color
        self.sizes = sizes
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"<Product {self.name} ({self.color}) - {self.price} лв.>"


products = [
    Product(1, "Nike Air Max", "Спортни маратонки", "черен", [42, 43, 44], 199.99, 10),
    Product(2, "Adidas Superstar", "Класически маратонки", "бял", [40, 41, 42], 149.99, 8),
    Product(3, "Puma Smash", "Удобни за всеки ден", "син", [39, 40, 41, 42], 129.99, 5),
]


def get_all_products():
    return products


def get_product_by_id(product_id):
    for p in products:
        if p.id == product_id:
            return p
    return None


def add_product(name, description, color, sizes, price, stock):
    new_id = max([p.id for p in products], default=0) + 1
    new_product = Product(new_id, name, description, color, sizes, price, stock)
    products.append(new_product)
    return new_product


def update_product(product_id, name, description, color, sizes, price, stock):
    product = get_product_by_id(product_id)
    if product:
        product.name = name
        product.description = description
        product.color = color
        product.sizes = sizes
        product.price = price
        product.stock = stock
        return True
    return False


def delete_product(product_id):
    products[:] = [p for p in products if p.id != product_id]


def search_products(query):
    query = query.lower()
    return [p for p in products if query in p.name.lower() or query in p.color.lower()]

def filter_products(min_price=None, max_price=None, size=None, in_stock=None):
    filtered = products
    if min_price is not None:
        filtered = [p for p in filtered if p.price >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p.price <= max_price]
    if size is not None:
        filtered = [p for p in filtered if size in p.sizes]
    if in_stock:
        filtered = [p for p in filtered if p.stock > 0]
    return filtered