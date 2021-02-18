import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from polls.models.basic_crawler import BasicCrawler

allow_extract = [r'.com/', r'.com.br/']
deny_domains_extract = ['google.com', 'web.whatsapp.com', 'bb.com.br']
get_just_address = re.compile('(.*\.)?(htt.*)\.com.br|(.*\.)?(htt.*)\.com')


def load_url():
    urls = []
    for e in BasicCrawler.objects.all():
        urls.append(e.url)
    return urls


class rentPropertySpider(scrapy.Spider):
  name = "rent_layer"
  start_urls = load_url()

  def parse(self, response):
      xlink = LinkExtractor(allow=allow_extract, deny_domains=deny_domains_extract)
      for link in xlink.extract_links(response):
          if len(str(link)) > 200:
            matchResult = get_just_address.search(link.url)
            if matchResult:
                print("REFINED: "+matchResult.group(0))
