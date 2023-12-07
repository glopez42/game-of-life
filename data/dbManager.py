import json


def insertRule(name, rule) -> None:
    f = open('data/data.json')
    data = json.load(f)
    f.close()

    data[name] = rule
    with open('json_data.json', 'w') as outfile:
        json.dump(data, outfile)

def getRuleByName(name) :
    f = open('data/data.json')
    data = json.load(f)
    f.close()
    return data[name]

def getLifeRule():
    return getRuleByName("life_rule")

def getContexts():
    f = open('data/data.json')
    data = json.load(f)
    f.close()
    return data["contexts"]
