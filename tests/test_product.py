import pytest; from controllers.product_controller import ProductController

class TestProductController:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.controller = ProductController()

    def test_create_product(self):
        product = self.controller.create_product(1, 'testproduct', 19.99)
        assert product.name == 'testproduct'
        assert product.price == 19.99

    def test_get_products(self):
        self.controller.create_product(1, 'testproduct', 19.99)
        products = self.controller.get_products()
        assert len(products) == 1
        assert products[0].name == 'testproduct'

    def test_multiple_products(self):
        self.controller.create_product(1, 'testproduct1', 19.99)
        self.controller.create_product(2, 'testproduct2', 29.99)
        products = self.controller.get_products()
        assert len(products) == 2
        assert products[0].name == 'testproduct1'
        assert products[1].name == 'testproduct2'