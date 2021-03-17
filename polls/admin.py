from django.contrib import admin

from polls.models.basic_crawler import BasicCrawler
from polls.models.black_list import BlackList
from polls.models.property_to_buy import PropertyToBuy
from polls.models.rental_property import RentalProperty
from polls.models.scrapy_improviments import ScrapyImprovement

admin.site.register(RentalProperty)
admin.site.register(BasicCrawler)
admin.site.register(ScrapyImprovement)
admin.site.register(PropertyToBuy)
admin.site.register(BlackList)
