# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HamrodoctorItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    address = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()
    phone = scrapy.Field()
    fax = scrapy.Field()
    short_description = scrapy.Field()
    district = scrapy.Field()
    # pass
