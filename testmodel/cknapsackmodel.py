from gurobipy import *

def solve(a, p, b, C):
    model = Model("knapsack")

    x = {}

    for i in range(len(a)):
        x[i] = model.addVar(vtype='b', obj=p[i])

    model.addConstr(quicksum(a[i] * x[i] for i in range(len(a))) <= b)
    for item in C:
        i, j = item
        model.addConstr((x[i] + x[j] ) <= 1)

    model.ModelSense = GRB.MAXIMIZE
    model.optimize()

