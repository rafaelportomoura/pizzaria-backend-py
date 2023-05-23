from polls.models import Product


class Products:
    def __init__(self):
        self.model = Product

    def getAllProducts(self):
        return self.model.objects.all()
