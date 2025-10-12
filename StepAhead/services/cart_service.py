from app import db
from services.catalog_service import Product


class CartItem(db.Model):
    __tablename__ = "cart_items"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)

    @property
    def product(self):
        return Product.query.get(self.product_id)


def get_cart(user_email):
    return CartItem.query.filter_by(user_email=user_email).all()

def add_to_cart(user_email, product_id, quantity=1):
    product = Product.query.get(product_id)
    if not product or product.stock < quantity:
        return False
    cart_item = CartItem.query.filter_by(user_email=user_email, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(
            user_email=user_email,
            product_id=product.id,
            product_name=product.name,
            price=product.price,
            quantity=quantity
        )
        db.session.add(cart_item)
    db.session.commit()
    return True

def remove_from_cart(user_email, product_id):
    item = CartItem.query.filter_by(user_email=user_email, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return True
    return False

def clear_cart(user_email):
    CartItem.query.filter_by(user_email=user_email).delete()
    db.session.commit()
    return True

def get_cart_total(user_email):
    total = db.session.query(db.func.sum(CartItem.price * CartItem.quantity))\
        .filter_by(user_email=user_email).scalar()
    return total or 0
