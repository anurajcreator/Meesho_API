import json
import scrapy
from scrapy.crawler import CrawlerProcess
from meeshoData.spiders.dataExtractor_spider import MeeshoSpider
from database_link import DataBase
import os

with open("links.json", 'r+') as f:
    Data_F = json.load(f)
f.close()

db = DataBase()



def data_extract():
    for i in Data_F:
        for j in Data_F[i]:
            for k in Data_F[i][j]:
                # print(k)
                # print(Data_F[i][j][k])
                link = Data_F[i][j][k]
                output = "Json_Data/" + k + ".json"
                os.system("scrapy crawl meesho -a start_urls={} -O {}".format(link, output))
                db.dataFormat(output)
                db.createTable(k)
                db.dataInsert(k)






if __name__ == "__main__":
    data_extract()
