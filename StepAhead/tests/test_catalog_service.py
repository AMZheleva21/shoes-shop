from services import catalog_service

def test_add_product(app):
    product = catalog_service.add_product(
        name="Test Shoe",
        description="Test Description",
        color="black",
        sizes=[42],
        price=99.99,
        stock=10,
        category="men",
        subcategory="sport"
    )
    assert product.id is not None
    assert product.name == "Test Shoe"

def test_get_all_products(app):
    products = catalog_service.get_all_products()
    assert isinstance(products, list)
