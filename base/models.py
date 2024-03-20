import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}{" "}{self.last_name}'

    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Item(models.Model):
    owner_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner_name}{" "}{self.product}'

