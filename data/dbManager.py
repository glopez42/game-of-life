from pymongo import *
import json

def connect() -> MongoClient:
    client = MongoClient("mongodb://root:root@localhost:27017")
    db = client['gameDB']
    return db

def insertLifeRule() -> None:
    db = connect()

    f = open('data/data.json')
    data = json.load(f)
    f.close()

    db["rules"].insert_one({
        "name" : "life_rule",
        "value" : data["life_rule"]
    })

def insertRule(name, rule) -> None:
    db = connect()

    db["rules"].insert_one({
        "name" : name,
        "value" : rule
    })

'''
from algorithm.init import *
def insertBaysRule(Eb, Eh, Fb, Fh):
    name = str(Eb) + str(Eh) + "/" + str(Fb) + str(Fh)
    tuple = (Eb, Eh, Fb, Fh)
    rule = getBaysSpaceRule(tuple).getRuleList()
    insertRule(name, rule)
'''

def insertContexts() -> None:
    db = connect()

    f = open('data/data.json')
    data = json.load(f)
    f.close()

    db["contexts"].insert_one({
        "contexts" : data["contexts"]
    })

def getRuleByName(name) :
    db = connect()
    collection = db["rules"].find_one({"name" : name})
    return collection["value"]

def getLifeRule():
    return getRuleByName("life_rule")

def getContexts():
    db = connect()
    collection = db["contexts"].find_one()
    return collection["contexts"]
