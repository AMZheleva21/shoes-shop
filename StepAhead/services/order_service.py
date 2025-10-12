from app import db
from services.cart_service import get_cart, get_cart_total, clear_cart, Product

class Order(db.Model):
    __tablename__ = "orders"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class OrderItem(db.Model):
    __tablename__ = "order_items"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)

def create_order(user_email, address, payment_method):
    cart_items = get_cart(user_email)
    if not cart_items:
        return None

    for item in cart_items:
        product = Product.query.get(item.product_id)
        if not product or product.stock < item.quantity:
            return None
        product.stock -= item.quantity

    total = get_cart_total(user_email)
    order = Order(
        user_email=user_email,
        address=address,
        payment_method=payment_method,
        total=total
    )
    db.session.add(order)
    db.session.flush()

    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            product_name=item.product_name,
            price=item.price,
            quantity=item.quantity
        )
        db.session.add(order_item)

    clear_cart(user_email)
    db.session.commit()
    return order

def get_all_orders():
    return Order.query.order_by(Order.created_at.desc()).all()


def get_order_with_items(order_id, user_email):
    order = Order.query.filter_by(id=order_id, user_email=user_email).first()
    if not order:
        return None

    items = OrderItem.query.filter_by(order_id=order.id).all()
    order_data = {
        "id": order.id,
        "user_email": order.user_email,
        "address": order.address,
        "payment": order.payment_method,
        "total": order.total,
        "items": [
            {
                "name": item.product_name,
                "price": item.price,
                "quantity": item.quantity,
                "description": getattr(item, "description", ""),  # ако имате описание
            }
            for item in items
        ]
    }
    return order_data
