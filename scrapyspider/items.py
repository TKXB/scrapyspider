# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    # 小说的名字
    chapter = scrapy.Field()

    author = scrapy.Field()
    # 作者
    recommend = scrapy.Field()

    length = scrapy.Field()

    time = scrapy.Field()

    status = scrapy.Field()
