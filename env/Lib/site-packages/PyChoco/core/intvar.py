from jnius import autoclass
class IntVar:

    def __init__(self, name, lb, ub): # pas de constructeur coté java c'est une interface différent de model
        self = autoclass('org.chocosolver.solver.variables.IntVar')
       

    def getValue(self):
        return self

"""     
        
        self.lb = IV(lb)
        self.ub = IV(ub)
"""