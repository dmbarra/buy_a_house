import scrapy

from polls.models.basic_crawler import BasicCrawler


def load_url():
    urls = []
    for e in BasicCrawler.objects.all():
        urls.append(e.url)
    return urls



class rentPropertySpider(scrapy.Spider):
  name = "rent_layer"
  start_urls = load_url()

  def parse(self, response):
      print(response)
