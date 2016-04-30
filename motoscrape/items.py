# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AdvertisementItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    power = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    permalink = scrapy.Field()
    date = scrapy.Field()
