from django.views.generic import ListView
from polls.models.rental_property import RentalProperty


class RentalPropertyListView(ListView):
    model = RentalProperty
    template_name = 'rental_property.html'
