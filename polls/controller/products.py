from polls.models import Product


class Products:
    def __init__(self):
        self.model = Product

    def all(self):
        return self.model.objects.filter(status=1)

    def perCategory(self, category):
        return self.model.objects.filter(category=category, status=1)

    def getById(self, id):
        return self.model.objects.get(id=id)
