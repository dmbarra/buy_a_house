from django_tables2 import tables, URLColumn

from polls.models.scrapy_improviments import ScrapyImprovement


class RentalPropertySavedTable(tables.Table):
    url = URLColumn()

    class Meta:
        model = ScrapyImprovement
        template_name = "django_tables2/bootstrap.html"
        fields = ("url",)