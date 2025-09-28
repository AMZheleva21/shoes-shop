from services.catalog_service import get_product_by_id

carts = {}

def get_cart(user_email):
    return carts.get(user_email, [])

def add_to_cart(user_email, product_id, quantity):
    if user_email not in carts:
        carts[user_email] = []

    product = get_product_by_id(product_id)
    if product and product.stock >= quantity:
        for item in carts[user_email]:
            if item["product"].id == product_id:
                item["quantity"] += quantity
                return True

        carts[user_email].append({"product": product, "quantity": quantity})
        return True
    return False

def remove_from_cart(user_email, product_id):
    if user_email in carts:
        carts[user_email] = [item for item in carts[user_email] if item["product"].id != product_id]

def clear_cart(user_email):
    if user_email in carts:
        carts[user_email] = []

def get_cart_total(user_email):
    return sum(item["product"].price * item["quantity"] for item in get_cart(user_email))