import json
 
# Opening JSON file
f = open('data/data.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

CONTEXTS = data['contexts']

def getActualRule():
    rule = data['actual_rule']
    ruleDictionary = {}
    for i in range(512):
        ruleDictionary.update({ tuple(CONTEXTS[i]) : rule[i]})
    return ruleDictionary

def getLifeRule():
    ruleGL = data['life_rule']
    ruleDictionary = {}
    for i in range(512):
        ruleDictionary.update({ tuple(CONTEXTS[i]) : ruleGL[i]})
    return ruleDictionary


# Closing file
f.close()