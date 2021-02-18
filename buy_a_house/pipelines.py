from django.core.exceptions import ObjectDoesNotExist
from polls.models.rental_property import RentalProperty


class BuyAHousePipeline:
    def process_item(self, item, spider):
        item.save()
        return item

class RentAPropertyPipeline:
    def process_item(self, item, spider):
        item.save()
        return item
