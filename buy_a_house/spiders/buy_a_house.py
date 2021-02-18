import scrapy 
from scrapy.linkextractors import LinkExtractor

from buy_a_house.items import BuyAHouseItem

class firstSpider(scrapy.Spider):
  name = "basic"
  start_urls = [
    "https://www.google.com/search?q=imobiliaria+barbacena"
   ]

  def parse(self, response):
      xlink = LinkExtractor()
      for link in xlink.extract_links(response):
          if len(str(link)) > 200:
              item = BuyAHouseItem()
              item['text'] = link.text
              item['link'] = link
              item['url'] = link.url
              yield item