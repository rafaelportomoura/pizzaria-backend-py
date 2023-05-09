from django.db import models
from models.category import Category


def product_file_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "products/{0}/%Y%m%d{1}".format(instance, filename)


class Product(models.Model):
    status_choice = [(0, "Lacking"), (1, "Available")]
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    picture = models.ImageField(
        upload_to=product_file_path,
    )
    status = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name="products")

    def __str__(self):
        return self.name
