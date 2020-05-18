from gurobipy import *


def solve(a, p, b):
    nitems = len(p)
    items = range(nitems)

    # TODO: Generate vertices and arcs ----------------------------------------
    vertices = []  # Vertices are named (i,j), see lecture
    arcs = []  # List of tuples, i.e. [((i,j), (k,l),w), ((k,l), (u,v),0)]
    # ------------------------------------------------------------------------

    # Model
    model = Model("Flowbased knapsack")
    model.modelSense = GRB.MAXIMIZE

    # Decision variable x_a indicates whether arc a is selected (value 1) or
    # not (value 0)
    x = {}
    for arc in arcs:
        x[(arc[0], arc[1])] = model.addVar(name="x_(%s,%s),(%s,%s)" %
                                           (arc[0][0], arc[0][1], arc[1][0],
                                            arc[1][1]),
                                           vtype=GRB.CONTINUOUS,
                                           obj=arc[2])
    # Update the model to make variables known.
    # From now on, no variables should be added.
    model.update()

    # TODO: Add your constraints ----------------------------------------------

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
