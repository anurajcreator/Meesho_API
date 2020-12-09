import MySQLdb
# import mysql.connector as m
#from ..database_link import DataBase
# with open(".. items.json, r+") as f:
#     item = f.read()
# f.close()
# print(item)
import os
# conn = MySQLdb.connect("localhost","root","","meesho")
# curr = conn.cursor()
#
# curr.execute("""SELECT product_link FROM all_sarees""")
# list = curr.fetchall()
# for i in list:
#
#     url = "https://meesho.com" + i[0]
#     os.system("scrapy crawl des -a start_urls={} -o des.json".format(url))
#
url = "https://meesho.com/trendy-stone-work-anklet/p/jgkz"
data = os.system("scrapy crawl des -a start_urls={}".format(url))
print(data)

