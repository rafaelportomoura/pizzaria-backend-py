from polls.models import Product


class ProductsService:
    def __init__(self):
        self.model = Product

    def getAllProducts(self):
        return self.model.objects.all()
