import extractdata
import helperfunctions
import networkx as nx
import itertools
from gurobipy import *

def solve(G, k, req_p):
    """
    Solve the political district problem given a graph G,
    the number of districts and a requirement of people.

    """
    #Initialize Model
    model = Model("Political Districting")
    model.params.LazyConstraints = 1

    x = {}
    #Set Variables:
    for plz in list(G.nodes):
        for district in range(k):
            x[plz, district] = model.addVar(vtype = GRB.BINARY, name="x_%s_%s"
                    % (plz, district))

    model.update()

    #Set Constraints
    #Each postcode must be part of exactly one district
    for plz in list(G.nodes):
            model.addConstr(quicksum(x[plz, district] for district in range(k)) == 1 )

    #Each electoral district must comprise approximately the same number of people
    for district in range(k):
        model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population']
            for plz in list(G.nodes())) <= 1.15 * req_p)
        model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population']
            for plz in list(G.nodes())) >= 0.85 * req_p)

    # callback: continuity requirement
    def callback(model, where):
        if where == GRB.Callback.MIPSOL:
            #Import current values for x
            rel = model.cbGetSolution(x)

            for district in range(k):
                # Extract nodes assigned to a district
                assignedNodes = [plz for plz in list(G.nodes()) if
                        round(rel[plz, district]) == 1]
                # Check whether the current solution yields exactly one
                # component of the graph
                H = nx.subgraph(G, assignedNodes)
                components = list(nx.connected_components(H))
                if len(components) >= 2:
                    a = list(components[0])[0]
                    b = list(components[1])[0]

                    # Calculate subset of minimal ab separators
                    paths = [path[1:-1] for path in nx.node_disjoint_paths(G, a, b)]
                    for seperator in itertools.product(*paths):
                        if not any(plz in assignedNodes for plz in seperator):
                            model.cbLazy(x[a, district] + x[b, district] -
                                    quicksum(x[plz, district] for plz in
                                        seperator) <= 1)
                            return None

    model.optimize(callback)

    return model
