
from data import dbManager

def generateLifeRule():
    collection_contexts = dbManager.getContexts()
    collection_rule = dbManager.getLifeRule()

    contexts = collection_contexts["contexts"]
    rule = collection_rule["value"]

    dict = {}
    for (context,bit) in zip(contexts, rule):
        dict.update({
            tuple(context) : bit
        })
    return dict
