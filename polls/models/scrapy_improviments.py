from django.db import models


class ScrapyImprovement(models.Model):
    url = models.CharField(max_length=1000)
    improved = models.CharField(max_length=1000)
