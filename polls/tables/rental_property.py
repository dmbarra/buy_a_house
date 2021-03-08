from django_tables2 import tables, URLColumn, LinkColumn, A

from polls.models.rental_property import RentalProperty


class RentalPropertyTable(tables.Table):
    url = URLColumn()
    delete = LinkColumn('main:destroy', text='Delete', args=[A('pk')], attrs={'a': {'class': 'btn'}})

    class Meta:
        model = RentalProperty
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "url", "delete", )