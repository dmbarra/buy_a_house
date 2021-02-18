import scrapy
from scrapy_djangoitem import DjangoItem
from polls.models.basic_crawler import BasicCrawler
from polls.models.rental_property import RentalProperty


class BuyAHouseItem(DjangoItem):
    django_model = BasicCrawler

class RentAProperty(DjangoItem):
    django_model = RentalProperty