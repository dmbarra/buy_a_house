from django_tables2 import SingleTableView

from polls.models.rental_property import RentalProperty
from polls.tables.rental_property import RentalPropertyTable


class RentalPropertyListView(SingleTableView):
    model = RentalProperty
    table_class = RentalPropertyTable
    template_name = 'rental_property.html'
