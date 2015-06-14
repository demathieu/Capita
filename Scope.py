__author__ = 'demathieu'


class Entry():
    def __init__(self, name,type):
        self.name = name
        self.type = type

    def __eq__(self, other):
       if self.name == other.name:
             return True
       return False


    def __repr__(self):
        return str(self.name) + " " + str(self.type) +" \n"

class SymbolTable():
    def __init__(self):
        #contains all the vars
        self.table = []
        # contains all the formal params
        self.formalParams = []
        # contains the functions defined
        self.functionList = []
        # size of the vars
        self.sizeVar = 0
        self.sizeParam = 0

    def giveSizeVar(self):
        result = 0
        for element in self.table:
            if element.type == 'int':
                result += 4
            elif element.type == 'char':
                result += 1
        return result

    def giveSizeParam(self):
        result = 0
        for element in self.formalParams:
            if element.type == 'int':
                result += 4
            elif element.type == 'char':
                result += 1
        return result

    def removeVariable(self,entry):
        self.table[entry.name]

    def __str__(self):
        returnString = ''
        for entry in self.table:
            returnString += ' var: '+ str(entry)
        for entry in self.formalParams:
            returnString += ' formal: '+ str(entry)
        for entry in self.functionList:
            returnString += ' func: ' + str(entry)
        return returnString;


class Scope():
    def __init__(self, parent = None, creator = None):
        self.parent = parent
        self.subScopes = []
        self.symbolTable = SymbolTable()
        self.creator = creator

    def addVarToSymbolTable(self,entry):
        self.symbolTable.table.append(entry)

    def addFormalParamToSymbolTable(self,entry):
        self.symbolTable.formalParams.append(entry)

    def addFunctionToSymbolTable(self,entry):
        self.symbolTable.functionList.append(entry)

    def removeVarToSymbolTable(self,scopeName,name,type):
        self.findScopeOfFunction(scopeName).symbolTable.table.remove(Entry(name,None))
        return self

    def findScopeOfFunction(self,name):
        for subScope in self.subScopes:
            if name == subScope.creator.name:
                return subScope
    def createSubScope(self):
        newScope = Scope(self)
        self.subScopes.append(newScope)
        return newScope

    def goBackToParentScope(self):
        return self.parent

    def setCreator(self,entry):
        self.creator = entry

    def giveBackSizeForFunction(self,name):
        for subscope in self.subScopes:
            if subscope.creator.name == name:
                return subscope.symbolTable.giveSizeVar()

    def giveBackSizeForFormalParam(self,name):
        for subscope in self.subScopes:
            if subscope.creator.name == name:
                return subscope.symbolTable.giveSizeParam()


    def __str__(self):
        temp = str(self.symbolTable)
        temp += 'creator: '+ str(self.creator) + '\n'
        for subScope in self.subScopes:
            temp += 'start sub  \n' +  str(subScope) + 'end sub \n'
        return temp
