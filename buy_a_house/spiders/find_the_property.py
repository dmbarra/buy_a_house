import time

import scrapy
from selenium.webdriver.chrome import webdriver

from polls.models.rental_property import RentalProperty


def load_url():
    urls = []
    for e in RentalProperty.objects.all():
        urls.append('https://www.google.com.br/search?q=site:'+e.url+'+venda+barbacena/mg')
    return urls


class FindThePropertySpider(scrapy.Spider):
  name = "property_layer"
  start_urls = load_url()
  handle_httpstatus_list = [302,303,429]

  def __init__(self):
      self.driver = webdriver.WebDriver()
      self.driver.maximize_window()

  def parse(self, response):
      for url in self.start_urls:
          self.driver.get(url)
          if(self.driver.find_element_by_id("recaptcha")):
              self.driver.find_element_by_css_selector(".recaptcha-checkbox-border").click()
          print(self.driver.title)
          time.sleep(40)

