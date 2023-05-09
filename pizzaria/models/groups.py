from django.db import models
from models.employee import Employee
from models.paths import Paths


class Group(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    is_admin = models.BooleanField(default=False)
    employee = models.ManyToManyField(
        Employee, on_delete=models.RESTRICT, related_name="groups"
    )
    paths = models.ManyToManyField(
        Paths, on_delete=models.RESTRICT, related_name="groups"
    )

    def __str__(self):
        return self.name
