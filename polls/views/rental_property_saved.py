from django_tables2 import SingleTableView

from polls.models.scrapy_improviments import ScrapyImprovement
from polls.tables.rental_property_saved import RentalPropertySavedTable


class RentalPropertySavedListView(SingleTableView):
    model = ScrapyImprovement
    table_class = RentalPropertySavedTable
    template_name = 'rental_property_saved.html'
