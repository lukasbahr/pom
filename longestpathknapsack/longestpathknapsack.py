from gurobipy import *


def solve(a, p, b):
    nitems = len(p)
    items = range(nitems)

    # TODO: Generate vertices and arcs ----------------------------------------
    vertices = [(i, j) for i in range(b) for j in items]  # Vertices are named (i,j), see lecture

    arcs = []  # List of tuples, i.e. [((i,j), (k,l),w), ((k,l), (u,v),0)]

    for i in range(1, nitems+1):
    # skip arcs
        for c in range(b+1):
            arcs.append((c, i-1, c, i, 0))

    # items arcs
        for c in range(b+1-a[i-1]):
            arcs.append((c, i-1, c+a[i-1], i, p[i-1]))

    # waste arcs
    for i in range(nitems+1):
        for c in range(b):
            arcs.append((c, i, c+1, i, 0))

    # ------------------------------------------------------------------------
    arcs = tuplelist(arcs)

    # Model
    model = Model("Flowbased knapsack")
    model.modelSense = GRB.MAXIMIZE

    # Decision variable x_a indicates whether arc a is selected (value 1) or
    # not (value 0)
    x = {}
    for arc in arcs:
        x[(arc[0:2], arc[2:4])] = model.addVar(name="x_(%s,%s),(%s,%s)" %
                                           (arc[0], arc[1], arc[2],
                                            arc[3]),
                                           vtype=GRB.CONTINUOUS,
                                           obj=arc[4])
    # Update the model to make variables known.
    # From now on, no variables should be added.

    model.update()

    # TODO: Add your constraints ----------------------------------------------
    # flow conversation

    idx = 0

    s = (0,0)
    t = (b,nitems)

    for arc in arcs:
            rhs = 0
            if arc[0:2] == s:
                rhs = 1
            if arc[0:2] == t:
                rhs = -1

            model.addConstr(

                quicksum(x[(arc[0:2], j)] for j in list(t[2:4] for t in
                    arcs.select(arc[0], arc[1],'*', '*'))) -

                quicksum(x[(j, arc[0:2])] for j in list(t[0:2] for t in
                    arcs.select('*', '*', arc[0], arc[1])))
                == rhs, name="flow_"+str(idx)
                )

            idx+=1

    # -------------------------------------------------------------------------

    model.update()
    # For debugging: print your model
    model.write('model.lp')
    model.optimize()

    # Printing solution and objective value
    def printSolution():
        if model.status == GRB.OPTIMAL:
            print('\n objective: %g\n' % model.ObjVal)
            print("Selected following arcs:")
            for arc in arcs:
                if x[(arc[0:2], arc[2:4])].x == 1:
                    print(arc)
        else:
            raise Exception("No solution!")

    printSolution()
    # Please do not delete the following line
    return model
