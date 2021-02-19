from django.db import models


class PropertyToBuy(models.Model):
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    place = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)