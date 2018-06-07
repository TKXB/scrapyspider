# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapyspider.items import ScrapyspiderItem
from scrapyspider.mysqlpipelines.sql import Sql

class ScrapyspiderPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ScrapyspiderItem):
            name = unicode(item['name'])
            chapter = unicode(item['chapter'])
            author = unicode(item['author'])
            recommend = unicode(item['recommend'])
            length = unicode(item['length'])
            time = unicode(item['time'])
            status = unicode(item['status'])
            Sql.insert_book_info(name, chapter, author, recommend, length, time, status)
            print "OK"
            return item

