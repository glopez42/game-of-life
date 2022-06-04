
import sys
import json
from data import dbManager

db = dbManager.connect()
dbManager.insertContexts()
dbManager.insertLifeRule()


f = open('data/data.json')
data = json.load(f)
f.close()

# insert some results of the algorithm
for i in range(5):
    name = "result" + str(i+1)
    db["rules"].insert_one({
        "name" : name,
        "value" : data[name]
    })

