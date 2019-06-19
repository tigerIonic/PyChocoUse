import PyChoco.core.model as m

my_model = m.Model('simple problem')

x = my_model.intVar('X', 0, 4)
y = my_model.intVar('Y', 1, 8)
my_model.arithm(x, '+', y, '<', 5).times(x, y, 4)
my_model.solve()
my_model.printStatistics()

print('X -> ' + str(x.getValue()))
print('Y -> ' + str(y.getValue()))


my_model2 = m.Model('simple problem 2')

x2 = my_model2.intVar('X2', 0, 4)
y2= my_model2.intVar('Y2', 1, 8)
my_model2.arithm(x2, '+', y2, '<', 5).times(x2, y2, 9999)
my_model2.solve()
my_model2.printStatistics()

print('X -> ' + str(x2.getValue()))
print('Y -> ' + str(y2.getValue()))
