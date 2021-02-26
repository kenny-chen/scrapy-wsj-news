# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    ucode = scrapy.Field()
    nmll = scrapy.Field()
    lot = scrapy.Field()
    stime = scrapy.Field()
    pass
