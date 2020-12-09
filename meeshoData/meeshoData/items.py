# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeeshodataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name= scrapy.Field()
    product_price = scrapy.Field()
    product_image = scrapy.Field()
    product_link = scrapy.Field()
    product_id = scrapy.Field()
    pass

class MeeshoDes(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_dispatch = scrapy.Field()
    product_des = scrapy.Field()
    product_size = scrapy.Field()
    product_stock = scrapy.Field()
    product_sold_by = scrapy.Field()
    pass
