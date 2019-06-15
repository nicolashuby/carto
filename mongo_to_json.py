from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from bson.json_util import dumps
import json

data = {}  
data['platforms'] = []  
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://192.168.99.101:27017')
mydb = client["test"]
mycol = mydb["pay"]

platforms =  list(mycol.find())
for plat in platforms:
	plat.pop('_id',None)
	data['platforms'].append(plat)

with open('PAYPlatforms.json', 'w') as outfile:  
    json.dump(data, outfile)