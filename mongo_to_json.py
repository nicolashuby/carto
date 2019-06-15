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
# Issue the serverStatus command and print the results
platforms =  mycol.find()
l = list(platforms)

for plat in l:
	print(type(plat))
	plat.pop('_id',None)
	print(plat)
	data['platforms'].append(plat)

with open('PAYPlatforms.json', 'w') as outfile:  
    json.dump(data, outfile)