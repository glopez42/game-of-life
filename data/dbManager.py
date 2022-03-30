from pymongo import *

client = MongoClient("mongodb://root:root@localhost:27017")
db = client['gameDB']

db['rules'].insert_one({
    "life_rule" : "1111" 
})

print(db['rules'].find_one())