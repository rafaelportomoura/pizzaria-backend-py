from django.db import models


class Paths(models.Model):
    name = models.CharField(max_length=45)
    method_path = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name
