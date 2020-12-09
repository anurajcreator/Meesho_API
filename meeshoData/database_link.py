import json
import MySQLdb


class DataBase(object):
    def __init__(self):
        self.createConnection()

    def createConnection(self):
        self.conn = MySQLdb.connect('localhost', 'root', '', 'meesho')
        self.curr = self.conn.cursor()

    def dataFormat(self, json_f):
        with open(json_f, "+r") as f:
            self.item = json.load(f)

        for i in self.item:
            try:
                i['product_id'][0] = int(i['product_id'][0])
            except:
                continue




        self.item = sorted(self.item, key=lambda i: i['product_id'])
        res = {}
        for dict in self.item:
            for list in dict:
                if list in res:
                    res[list] += (dict[list])
                else:
                    res[list] = dict[list]
        del res['product_id']
        self.item = res

        print(self.item)

        # file_name = "formated_" + str(table) + ".json"
        # with open(file_name, "w+") as f:
        #     json.dump(self.item, f)
        # f.close()



    def createTable(self, table):
        self.curr.execute("""DROP TABLE IF EXISTS {}""".format(table))
        self.curr.execute("""CREATE TABLE {} (
                         product_name varchar(255),
                         product_price varchar(5),
                         product_image varchar(255),
                         product_link varchar(255)
                         )""".format(table))

    def dataInsert(self, table):
        item = self.item
        for j in range(len(item['product_name'])):
            self.curr.execute("""INSERT INTO {} VALUES (%s,%s,%s,%s)""".format(table),
                              (item['product_name'][j],
                               item['product_price'][j],
                               item['product_image'][j],
                               item['product_link'][j]))

        self.conn.commit()
