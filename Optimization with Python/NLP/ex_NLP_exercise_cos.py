import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(initialize=0, bounds=(-5,5))
model.y = pyo.Var(initialize=0, bounds=(-5,5))
x = model.x
y = model.y

model.obj = pyo.Objective(expr = cos(x+1) + cos(x)*cos(y), sense=maximize)

opt = SolverFactory('ipopt')
opt.options['tol']=1e-6
opt.solve(model)

model.pprint()
print('x=',pyo.value(x))
print('y=',pyo.value(y))
print('objFun=',pyo.value(model.obj))