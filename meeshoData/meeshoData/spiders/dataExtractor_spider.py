import scrapy
from ..items import MeeshodataItem, MeeshoDes
import json
from scrapy.crawler import CrawlerProcess


class MeeshoSpider(scrapy.Spider):
    name = 'meesho'

    def __init__(self, *args, **kwargs):
        super(MeeshoSpider, self).__init__(*args, **kwargs)
        self.start_urls = []
        url = kwargs.get("start_urls") + "?page="
        for i in range(1, 21):
            self.start_urls.append(url + str(i))

    def parse(self, response):

        items = MeeshodataItem()
        product_id = response.css("a.active::text").extract()
        product_name = response.css(".plp-card-title-desktop::text").extract()
        product_price_ = response.css(".actual-cost::text").extract()
        product_image = response.css(".plp-img").xpath("@src").extract()
        product_link = response.css(".plp-card-desktop").xpath("@href").extract()

        product_price = []
        for i in range(1, len(product_price_)):
            if i % 2 != 0:
                product_price.append(product_price_[i])

        items['product_id'] = product_id
        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_image'] = product_image
        items['product_link'] = product_link

        yield items


class DescriptionSpider(scrapy.Spider):
    name = "des"

    def __init__(self, *args, **kwargs):
        super(DescriptionSpider, self).__init__(*args, **kwargs)
        self.start_urls = []
        self.start_urls.append(kwargs.get("start_urls"))

    def parse(self, response):
        items = MeeshoDes()
        product_name = response.css(".pdp-title::text").extract()
        product_dispatch = response.css(".info-product li span::text").extract()
        product_des = response.xpath("//meta[@name='description']").xpath("@content").extract()
        product_stock = response.css(".flash::text").extract()
        product_size = response.css(".chip-button::text").extract()
        product_sold_by = response.css(".sold-by::text").extract()

        items['product_name'] = product_name
        items['product_dispatch'] = product_dispatch
        items['product_size'] = product_size
        items['product_stock'] = product_stock
        items['product_des'] = product_des
        items['product_sold_by'] = product_sold_by


        yield items
# class MeeshoLinkSpider(object):
#     name = 'link'
#     start_urls = ["https://meesho.com/"]
#     temp ={}
#     def parse(self, response):
#         items = MeeshoLinkItem
#
#         main_c = response.css('.nav-head-item::text').extract()
#         cat = response.css('.sub-list-title span::text').extract()
#         sub_cat = response.css('.sub-list-item a::text').extract()
#         link = response.css('.sub-list-item a').xpath('@href').extract()
#
#         for i in range(len(sub_cat)):
#             self.temp[sub_cat[i]] = link[i]
#
#         items['links'] =
