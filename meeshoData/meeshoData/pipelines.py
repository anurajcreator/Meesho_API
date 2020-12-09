# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import MySQLdb


class MeeshodataPipeline(object):
    def process_item(self, item, spider):
        #self.store_db(item)
        #print("Pipeline : " + item['product_price'][0])
        return item



