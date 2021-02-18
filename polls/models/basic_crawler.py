from django.db import models

class BasicCrawler(models.Model):
    text = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
