import scrapy
from scrapy import Selector
from countrycode.items import CountrycodeItem
import pdb


class CodesSpider(scrapy.Spider):

    name = "codes"

    def start_requests(self):
        urls = [
            'http://www.nationsonline.org/oneworld/country_code_list.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        countries = response.xpath("//table[contains(@id, 'codelist')]//tr[contains(@class,'border1')]").extract()

        for country in countries[1:]:

            tr = Selector(text=country.encode('utf-8'), type="html")
            country_name = tr.xpath("//td[2][contains(@class, 'abs')]/a/text()").extract_first()
            iso_alpha2 = tr.xpath("//td[3]/text()").extract_first().strip()
            iso_alpha3 = tr.xpath("//td[4]/text()").extract_first().strip()

            yield {
                'city': country_name,
                'iso_alpha2': iso_alpha2,
                'iso_alpha3': iso_alpha3,
            }
