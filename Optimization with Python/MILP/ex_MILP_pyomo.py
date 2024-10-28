import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

setI = [1,2,3,4]
setJ = [1,2,3,4,5,6,7,8,9,10]
model.z = pyo.Var(setI, setJ, bounds=(0,None))
model.Const_UB_x = pyo.ConstraintList()
for i in setI:
    for j in setJ:
        model.Const_UB_x.add(model.z[i,j] <= 100)
        
        

model.x = pyo.Var(within=Integers, bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr= -x+2*y<=7)
model.C2 = pyo.Constraint(expr= 2*x+y<=14)
model.C3 = pyo.Constraint(expr= 2*x-y<=10)

model.obj = pyo.Objective(expr= x+y, sense=maximize)

opt = SolverFactory('gurobi')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)