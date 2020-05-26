from gurobipy import *

def solve(a, p, b):
    model = Model("knapsack")

    x = {}

    for i in range(len(a)):
        x[i] = model.addVar(vtype='b', obj=p[i])

    model.addConstr(quicksum(a[i] * x[i] for i in range(len(a))) <= b)

    model.ModelSense = GRB.MAXIMIZE
    model.optimize()

