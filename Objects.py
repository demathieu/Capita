__author__ = 'demathieu'
class Quadruple:
    def __init__(self,id, op, arg1, arg2, result):
        self.id = id
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return str(self.result) + " = " + str(self.arg1) + " " + str(self.op) + " " + str(self.arg2)+' id:'+str(self.id)+ " \n"
