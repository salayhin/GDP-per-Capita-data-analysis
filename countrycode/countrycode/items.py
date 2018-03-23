# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CountrycodeItem(scrapy.Item):
    # define the fields for your item here like:
    country_name = scrapy.Field()
    iso_alpha2 = scrapy.Field()
    iso_alpha3 = scrapy.Field()
    #pass