from django.db import models

class ScrapyImproviment(models.Model):
    original = models.CharField(max_length=1000)
    improved = models.CharField(max_length=1000)
