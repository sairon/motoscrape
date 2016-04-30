# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

from .db import ads_db


class NewAdsPipeline(object):
    def process_item(self, item, spider):
        if item['permalink'] in ads_db:
            raise DropItem()
        return item
