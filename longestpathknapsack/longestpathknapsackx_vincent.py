
from gurobipy import *
import networkx as nx

def solve(a, p, b):
nitems = len(p)
    items = range(nitems)

    # TODO: Generate vertices and arcs ----------------------------------------
    # we want a graph with x-axis: 0-b (# buckets), and y-axis 0-n (# of items)
    G = nx.DiGraph()
    G.add_nodes_from(nx.grid_graph(dim=[nitems+1, b+1]))
    vertices = list(G.nodes)  # Vertices are named (i,j), see lecture
    arcs = []  # List of tuples, i.e. [((i,j), (k,l),w), ((k,l), (u,v),0)]

    for i in range(1, nitems+1):
        for c in range(b+1-a[i-1]):
            G.add_edge((c, i - 1), (c + a[i - 1], i), weight=p[i - 1])

        for c in range(b + 1):
            G.add_edge((c, i - 1), (c, i), weight=0)

    for i in range(nitems + 1):
        for c in range(b):
            G.add_edge((c, i), (c + 1, i), weight=0)

    arcs = [(a, b, k['weight']) for a, b, k in G.edges.data()]
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
    # flow conservation constraint: input flow = output flow
    # Start node, End node
    s = vertices[0]
    t = vertices[-1]

    model.addConstr(quicksum(x[s, i] for i in G.successors(s)) - quicksum(x[j, s] for j in G.predecessors(s)) == 1)
    model.addConstr(quicksum(x[t, i] for i in G.successors(t)) - quicksum(x[j, t] for j in G.predecessors(t)) == -1)
    for n in vertices[1:-1]:
        model.addConstr(quicksum(x[n, i] for i in G.successors(n)) - quicksum(x[j, n] for j in G.predecessors(n)) == 0)
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
draw(G)
    return model

def generatePos(G):
    pos = {}
    for node in G.nodes:
        pos[node] = node
    return pos

def draw(G):
    nx.draw(G, generatePos(G))

