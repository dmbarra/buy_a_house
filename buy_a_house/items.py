import scrapy
from scrapy_djangoitem import DjangoItem
from polls.models.basic_crawler import BasicCrawler


class BuyAHouseItem(DjangoItem):
    django_model = BasicCrawler
