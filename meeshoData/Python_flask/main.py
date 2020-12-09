from flask import Flask
from flask_restful import Api, Resource
import os
import json

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, link, link1, link2):
        url = "https://meesho.com/" + link +"/"+link1+"/"+link2
        os.system("scrapy crawl des -a start_urls={} -O des.json".format(url))
        with open("des.json", "r+") as f:
            data = json.load(f)

        return data


api.add_resource(HelloWorld, "/api/<string:link>/<string:link1>/<string:link2>")

if __name__ == "__main__":
    app.run(debug=True)
