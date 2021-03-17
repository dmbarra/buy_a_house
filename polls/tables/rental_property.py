from django_tables2 import tables, URLColumn, LinkColumn, A

from polls.models.rental_property import RentalProperty


class RentalPropertyTable(tables.Table):
    url = URLColumn()
    promote = LinkColumn('main:promote', text='Save', args=[A('pk')], attrs={'a': {'class': 'btn'}})
    delete = LinkColumn('main:destroy', text='Delete', args=[A('pk')], attrs={'a': {'class': 'btn'}})
    block = LinkColumn('main:block', text='Move to Block', args=[A('pk')], attrs={'a': {'class': 'btn'}})

    class Meta:
        model = RentalProperty
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "url", "promote", "delete", "block", )