import scrapy
from polls.models.basic_crawler import BasicCrawler


class BuyAHouseItem(scrapy.Item):
    django_model = BasicCrawler
    text = scrapy.Field()
    link = scrapy.Field()
