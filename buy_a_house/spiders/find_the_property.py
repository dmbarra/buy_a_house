import scrapy
from scrapy.linkextractors import LinkExtractor
from polls.models.scrapy_improviments import ScrapyImproviment


def load_url():
    urls = []
    for e in ScrapyImproviment.objects.all():
        urls.append(e.improved.replace("{city}", "Barbacena"))
    return urls


class FindThePropertySpider(scrapy.Spider):
  name = "property_layer"
  start_urls = load_url()

  def parse(self, response):
      print(response.body)
      xlink = LinkExtractor()
      for link in xlink.extract_links(response):
          if len(str(link)) > 200:
              print('----------------------')
              print(link)
              print('******************')
