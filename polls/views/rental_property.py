from django.shortcuts import redirect
from django_tables2 import SingleTableView

from polls.models.black_list import BlackList
from polls.models.rental_property import RentalProperty
from polls.models.scrapy_improviments import ScrapyImprovement
from polls.tables.rental_property import RentalPropertyTable


class RentalPropertyListView(SingleTableView):
    model = RentalProperty
    table_class = RentalPropertyTable
    template_name = 'rental_property.html'

    @staticmethod
    def destroy(request, *args, **kwargs):
        RentalProperty.objects.filter(pk=kwargs['pk']).delete()
        return redirect('/')

    @staticmethod
    def black_list(request, *args, **kwargs):
        rental = RentalProperty.objects.get(pk=kwargs['pk'])
        RentalProperty.objects.filter(pk=kwargs['pk']).delete()
        BlackList.objects.create(url=rental.url).save()
        return redirect('/')

    @staticmethod
    def promote(request, *args, **kwargs):
        rental = RentalProperty.objects.get(pk=kwargs['pk'])
        RentalProperty.objects.filter(pk=kwargs['pk']).delete()
        ScrapyImprovement.objects.create(url=rental.url).save()
        return redirect('/')