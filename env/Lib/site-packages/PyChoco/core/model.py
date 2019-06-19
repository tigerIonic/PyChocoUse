from jnius import autoclass

# from . import intvar

class Model(object):


    def getName(self):
        return self.model.getName()

    def intVar(self, name, lb, ub):
        return self.model.intVar(name, lb, ub)

    def boolVar(self, name, val):
        if val==True:
            return self.model.intVar(name,1,1)
        elif val==False:
            return self.model.intVar(name,0,0)
        else:
            raise SyntaxError ("boolean expected")

    def arithm(self, var1, op1, var2, op2, cste):
        self.model.arithm(var1, op1, var2, op2, cste).post()
        return self

    def times(self, var1, var2, equ):
        self.model.times(var1, var2, equ).post()
        return self

    def solve(self):
        self.model.getSolver().solve()

    def printStatistics(self):
        self.model.getSolver().printStatistics()

    def __init__(self, name):
        Mod = autoclass('org.chocosolver.solver.Model')
        self.model = Mod(name)
