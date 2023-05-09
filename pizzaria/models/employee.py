from django.db import models


class Employee(models.Model):
    status_choice = []

    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=2, default="AC")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
