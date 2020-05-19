from gurobipy import *


def solve(a, p, b):
    nitems = len(p)
    items = range(nitems)

    # TODO: Generate vertices and arcs ----------------------------------------
    vertices = [(i, j) for i in range(b) for j in items]  # Vertices are named (i,j), see lecture

    arcs = []  # List of tuples, i.e. [((i,j), (k,l),w), ((k,l), (u,v),0)]

    # skip arcs
    for j in range(1, nitems):
        for i in range(b):
            arcs.append((i,j-1,i,j,0))

    # waste arcs
    for j in items:
        for i in range(b-1):
            arcs.append((i,j,i+1,j,1))

    # items arcs
    for j in range(1, nitems):
        for i in range(b-a[j]):
            arcs.append((i, j-1, i+a[j],j, a[j]))

   #  # skip arcs
    #  for j in range(1, nitems):
    #      for i in range(b):
    #          arcs.append(((i,j-1),(i,j),0))
    #
    #  # waste arcs
    #  for j in items:
    #      for i in range(b-1):
    #          arcs.append(((i,j),(i+1,j),1))
    #
    #  # items arcs
    #  for j in range(1, nitems):
    #      for i in range(b-a[j]):
    #          arcs.append(((i, j-1), (i+a[j],j), a[j]))
#
    # ------------------------------------------------------------------------
    arcs = tuplelist(arcs)

    print(arcs)
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
    s = (0,0)
    t = (b,nitems)

    for arc in arcs:
            print(arcs.select('*', arc[0,2]))
            # right hand side
            rhs = 0
            if arc[0:2] == s:
                rhs = 1
            if arc[0:2] == t:
                rhs = -1
            # now the flow balance
            model.addConstr(
                # outgoing edges
                quicksum(x[(arc[0:2],j)] for j in list(t[1] for t in
                    arcs.select(arc[0:2],'*'))) -
                # incoming edges
                quicksum(x[(j,arc[0:2])] for j in list(t[0] for t in
                    arcs.select('*',arc[0,2])))
                == rhs, name="flow_"+str(i)
                )

    # -------------------------------------------------------------------------

    model.update()
    # For debugging: print your model
    # model.write('model.lp')
    model.optimize()

    # Printing solution and objective value
    def printSolution():
        if model.status == GRB.OPTIMAL:
            print('\n objective: %g\n' % model.ObjVal)
            print("Selected following arcs:")
            for arc in arcs:
                if x[(arc[0], arc[1])].x == 1:
                    print(arc)
        else:
            raise Exception("No solution!")

    printSolution()
    # Please do not delete the following line
    return model
