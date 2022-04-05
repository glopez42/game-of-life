from data import dbManager

class Rule():

    def __init__(self, rule):
        self.rule = rule
        self.contexts = dbManager.getContexts()
        self.ruleDictionary = self._generateDictionary()
    
    def _generateDictionary(self):
        dict = {}
        for (context, bit) in zip(self.contexts, self.rule):
            dict.update({
                tuple(context) : bit
            })
        return dict
    
    # returns the rule itself, the dictionary
    def getRule(self):
        return self.ruleDictionary
    
    # returns the state list of the rule
    def getRuleList(self):
        return self.rule
    
    # sets a new rule and creates a new dictionary
    def setRule(self, newRule):
        self.rule = newRule
        self.ruleDictionary = self._generateDictionary()