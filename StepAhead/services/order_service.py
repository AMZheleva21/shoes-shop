from services.cart_service import get_cart, clear_cart

orders = []

def create_order(user_email, address, payment_method):
    cart = get_cart(user_email)
    if not cart:
        return None

    for item in cart:
        item["product"].stock -= item["quantity"]

    order = {
        "user": user_email,
        "items": cart.copy(),
        "address": address,
        "payment": payment_method,
    }
    orders.append(order)

    clear_cart(user_email)
    return order

def get_all_orders():
    return orders
