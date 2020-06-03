from gurobipy import *
import networkx as nx


def solve(m, L, d, l):
    """
    :param m: number of available (raw) rolls (=known upper bound on the optimum)
    :param L: length of (raw) rolls

    Orders: Demand d (how often) length (how much)
    :param d: demands of order i
    :param l: length of order i

    i in n demands
    j in m rolls
    """

    # Graph generator-----------------------------------------------------------
    G = nx.DiGraph()
    G.add_nodes_from(range(L + 2))  # nodes: integer states of a raw roll

    # aggregating the orders
    orders = {}
    for length in set(l):
        orders[length] = sum([x[1] for x in zip(l, d) if x[0] == length])

    print(orders)

    # skip nodes
    for i in range(L + 1):
        G.add_edge(i, i + 1, demand=0, length=1)

    # state connections
    for i in orders:
        for j in range(1, (L + 2) - i):
            G.add_edge(j, j + i, demand=orders[i], length=i)

    nodes = list(G.nodes())
    arcs = [((a, b), d) for a, b, d in G.edges.data()]
    # --------------------------------------------------------------------------

    model = Model("csflowmodel")

    x = model.addVars(G.edges, vtype=GRB.INTEGER, lb=0)  # Edges in Gurobi model

    # flow conservation constraint
    for i in nodes[1:-1]:
        model.addConstr(quicksum(x[j] for j in G.in_edges(i)) - quicksum(x[j] for j in G.out_edges(i)) == 0)

    for i in orders:
        model.addConstr(quicksum(x[j] for j in [x[0] for x in arcs if x[1]["length"] == i]) >= orders[i])

    model.setObjective(x[0, 1], GRB.MINIMIZE)

    model.relax()

    model.optimize()
