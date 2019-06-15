require 'mongo'

client = Mongo::Client.new([ '192.168.99.101:27017' ], :database => 'test')

db = client.database

collection = client[:pay]
collection.delete_many()
doc = [{name: 'Steve', hobbies: [ 'hiking', 'tennis', 'fly fishing' ]},
       {name: 'Stev00', hobbies: [ 'hik', 'tennis', 'fly fishing' ]}]

result = collection.insert_many(doc)
