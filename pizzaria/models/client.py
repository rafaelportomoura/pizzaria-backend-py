from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.CharField(max_length=27)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="ACTIVE")
