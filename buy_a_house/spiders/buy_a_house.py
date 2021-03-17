import scrapy 
from scrapy.linkextractors import LinkExtractor

from buy_a_house.items import BuyAHouseItem

class googleSpider(scrapy.Spider):
  name = "basic"

  def start_requests(self):
      urls = [
          "https://www.google.com/search?q=imobiliaria+barbacena/mg",
          "https://www.google.com/search?q=imoveis+barbacena/mg",
          "https://www.google.com/search?q=lotes+barbacena/mg",
          "https://www.google.com/search?q=terrenos+barbacena/mg",
          "https://www.google.com/search?q=casa+colonia+rodrigo+silva",
      ]
      for url in urls:
          yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
      xlink = LinkExtractor()
      for link in xlink.extract_links(response):
          if len(str(link)) > 200:
              item = BuyAHouseItem()
              item['text'] = link.text
              item['link'] = link
              item['url'] = link.url
              yield item