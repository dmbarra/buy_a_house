from django_tables2 import tables

from polls.models.rental_property import RentalProperty


class RentalPropertyTable(tables.Table):
    class Meta:
        model = RentalProperty
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "url", )