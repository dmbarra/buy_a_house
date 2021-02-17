import scrapy 
from scrapy.linkextractors import LinkExtractor

class firstSpider(scrapy.Spider):
  name = "basic"
  start_urls = [
    "https://www.google.com/search?q=imobiliaria+barbacena"
   ]

  def parse(self, response):
      xlink = LinkExtractor()
      for link in xlink.extract_links(response):
          if len(str(link)) > 200 or 'imoveis' in link.text:
              print(len(str(link)), link.text, link, "\n")