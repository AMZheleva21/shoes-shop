from services import order_service, cart_service, catalog_service
from app import db


def test_create_order(app):
    with app.app_context():
        product = catalog_service.Product(name="Nike Air Max", price=120.0, stock=5)
        db.session.add(product)
        db.session.commit()

        cart_service.add_to_cart("order@example.com", product.id, quantity=2)
        order = order_service.create_order(
            user_email="order@example.com",
            address="123 Test Street",
            payment_method="card"
        )

        assert order is not None
        assert order.user_email == "order@example.com"
        assert order.total == 240.0

        updated_product = catalog_service.Product.query.get(product.id)
        assert updated_product.stock == 3





