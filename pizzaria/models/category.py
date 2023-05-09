from django.db import models


def category_file_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "categories/{0}/%Y%m%d{1}".format(instance, filename)


class Category(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.TextField()
    picture = models.ImageField(upload_to=category_file_path)

    def __str__(self):
        return name
