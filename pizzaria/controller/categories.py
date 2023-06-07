from pizzaria.models import Category


class Categories:
    def __init__(self, model=Category):
        self.model = model

    def all(self):
        return self.model.objects.all()
