from services import cart_service, catalog_service
from app import db

def test_add_to_cart(app):
    with app.app_context():
        product = catalog_service.Product(name="Nike Air", price=100.0, stock=10)
        db.session.add(product)
        db.session.commit()

        result = cart_service.add_to_cart("test@example.com", product.id, quantity=2)
        assert result is True

        cart = cart_service.get_cart("test@example.com")
        assert len(cart) == 1
        assert cart[0].product_name == "Nike Air"
        assert cart[0].quantity == 2

