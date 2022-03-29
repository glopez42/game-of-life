import json

def _loadJson():
    f = open('data/data.json')
    data = json.load(f)
    f.close()
    return data

def getActualRule():
    data = _loadJson()
    contexts = data['contexts']
    rule = data['actual_rule']
    ruleDictionary = {}
    for i in range(512):
        ruleDictionary.update({ tuple(contexts[i]) : rule[i]})
    return ruleDictionary

def getLifeRule():
    data = _loadJson()
    contexts = data['contexts']
    ruleGL = data['life_rule']
    ruleDictionary = {}
    for i in range(512):
        ruleDictionary.update({ tuple(contexts[i]) : ruleGL[i]})
    return ruleDictionary
