from django_tables2 import tables, URLColumn

from polls.models.rental_property import RentalProperty


class RentalPropertyTable(tables.Table):
    url = name = URLColumn()

    class Meta:
        model = RentalProperty
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "url", )