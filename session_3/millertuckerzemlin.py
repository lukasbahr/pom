from gurobipy import *
import networkx as nx
import re
import math

def solve(path):

    coordinates = getCityData(path)
    G = nx.DiGraph()
    G.add_nodes_from([i for i in coordinates])
    vertices = list(G.nodes)
    arcs = []

    for i in coordinates:
        for j in coordinates:
            if i == j:
                continue
            else:
                xd = coordinates[i][0] - coordinates[j][0]
                yd = coordinates[i][1] - coordinates[j][1]
                dij = math.sqrt(xd*xd + yd*yd)
                G.add_edge(i, j, weight=dij)
                G.add_edge(j, i, weight=dij)

    arcs = [(a, b, k['weight']) for a, b, k in G.edges.data()]


    model = Model("TSP")
    model.modelSense = GRB.MINIMIZE


    x = {}
    for arc in arcs:
        x[(arc[0], arc[1])] = model.addVar(name="x_(%s,%s)" % (arc[0], arc[1]), vtype=GRB.BINARY, obj=arc[2])

    u = {}
    for i in vertices:
        u[i] = model.addVar(name="x_(%s)" % (i), vtype='c')


    model.update()

    for i in vertices:
        model.addConstr(quicksum(x[i, j] for j in G.successors(i)) == 1)
        model.addConstr(quicksum(x[j, i] for j in G.predecessors(i)) == 1)

    model.addConstr(u[1] == 1)

    for i in vertices:
        for j in vertices:
            if j == 1 or i == j:
                continue
            else:
                model.addConstr(u[i]-u[j]+x[i,j]*len(vertices) <= len(vertices)
                    - 1)

        model.addConstr(u[i] >= 0)

    model.optimize()


def getCityData(path):

    coordinates = {}
    isCoordinate = False

    with open(path, 'r') as df:
        for line in df:
            if line.find("NODE_COORD_SECTION") > -1:
                isCoordinate = True
                continue
            elif line.find("EOF") > -1:
                break

            content = re.split("  | |\t", line)

            if isCoordinate:
                coordinates[int(content[0])] = tuple((float(content[1]),
                    float(content[2].replace("\n", ""))))

    return coordinates



if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    solve(path)
