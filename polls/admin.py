from django.contrib import admin

from polls.models.basic_crawler import BasicCrawler
from polls.models.rental_property import RentalProperty

admin.site.register(RentalProperty)
admin.site.register(BasicCrawler)
