import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from buy_a_house.items import RentAProperty
from buy_a_house.variables.denny_urls import deny_domains_extract
from polls.models.basic_crawler import BasicCrawler
from polls.models.black_list import BlackList
from polls.models.rental_property import RentalProperty

allow_extract = [r'.com/', r'.com.br/', '.br/']
get_just_address = re.compile("(http:\/\/[^\/]*\/)|(https:\/\/[^\/]*\/)")


def load_url():
    urls = []
    for e in BasicCrawler.objects.all():
        urls.append(e.url)
    return urls


class RentAPropertySpider(scrapy.Spider):
  name = "rent_layer"
  start_urls = load_url()

  def parse(self, response):
      xlink = LinkExtractor(allow=allow_extract)
      for link in xlink.extract_links(response):
          if len(str(link)) > 200:
            extracted = get_just_address.findall(link.url)
            for url in extracted:
                # print("URL -> " + ''.join(url))
                yield from self.save_the_item(''.join(url))

  def save_the_item(self, url):
      rent = RentalProperty.objects.filter(url=url).exists()
      blocked = BlackList.objects.filter(url=url).exists()
      if not rent and not blocked:
          item = RentAProperty()
          item['url'] = url
          item['total_of_places'] = 0
          yield item
