from gurobipy import *
import networkx as nx
import re
import math

def solve(path):

    coordinates = getCityData(path)

    G = nx.Graph()
    G.add_nodes_from([i for i in coordinates])
    vertices = list(G.nodes)
    arcs = []

    for i in coordinates:
        for j in coordinates:
            if i >= j:
               continue

            xd = coordinates[i][0] - coordinates[j][0]
            yd = coordinates[i][1] - coordinates[j][1]
            dij = math.sqrt(xd*xd + yd*yd)

            G.add_edge(i, j, weight=dij)

    arcs = [(a, b, k['weight']) for a, b, k in G.edges.data()]

    model = Model("TSP DFJ")
    model.modelSense = GRB.MINIMIZE

    x = {}
    for arc in arcs:
        x[(arc[0], arc[1])] = model.addVar(name="x_(%s,%s)" % (arc[0], arc[1]),
                vtype='b', obj=round(arc[2]))

    model.update()

    for i in range(1, len(vertices)+1):
        model.addConstr((quicksum(x[i, j] for j in vertices if i < j) +
            quicksum(x[j,i] for j in vertices if j < i))== 2)

    SEC_violated = True
    count = 0
    while(SEC_violated):

        count +=1

        model.optimize()

        Gstar = nx.Graph()

        for i in coordinates:
            for j in coordinates:
                if i >= j:
                   continue
                Gstar.add_edge(i, j, weight=max(0,x[i,j].x))

        cut_val, partition = nx.stoer_wagner(Gstar)

        if cut_val < 1.999999:
            partition_list = []
            for i in partition[0]:
                for j in partition[1]:
                    if i<j:
                        partition_list.append((i,j))
                    else:
                        partition_list.append((j,i))

            model.addConstr(quicksum(x[i,j] for (i,j) in partition_list)>=2)

            SEC_violated = True

        else:
            SEC_violated = False

    print(count)




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
