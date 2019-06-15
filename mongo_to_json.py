from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://192.168.99.101:27017')
mydb = client["test"]
mycol = mydb["pay"]
# Issue the serverStatus command and print the results
for x in mycol.find():
  print(x) 