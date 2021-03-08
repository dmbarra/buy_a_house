from django.db import models


class BlackList(models.Model):
    url = models.CharField(max_length=100)
