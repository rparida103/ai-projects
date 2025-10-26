from models.product import Product

class ProductController:
    def __init__(self):
        self.products = []

    def create_product(self, product_id, name, price):
        product = Product(product_id, name, price)
        self.products.append(product)
        return product

    def get_products(self):
        return self.products