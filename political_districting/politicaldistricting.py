import extractdata
import helperfunctions
import networkx as nx
from gurobipy import *

def solve(G, k, req_p):
    #pass
    #Initialize Model
    model = Model("Political Districting")
    model.params.LazyConstraints = 1

    x = {}
    #Set Variables:
    for plz in list(G.nodes):
        for district in range(k):
            x[plz, district] = model.addVar(vtype = GRB.BINARY, name="x_%s_%s" % (plz, district))

    model.update()

    #Set Constraints
    #Each postcode must be part of exactly one district
    for plz in list(G.nodes):
            model.addConstr(quicksum(x[plz, district] for district in range(k)) == 1 )

    #Each electoral district must comprise approximately the same number of people
    for district in range(k):
        model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population'] for plz in list(G.nodes())) <= 1.15 * req_p)
        model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population'] for plz in list(G.nodes())) >= 0.85 * req_p)


            # callback: continuity requirement
    def cb_sep_violation(model, where):
        if where == GRB.Callback.MIPSOL:
            rel = model.cbGetSolution(x)
            for d in range(district):
                rel_d = [plz for plz in list(G.nodes) if round(rel[plz, d]) == 1]
                # check whether the current solution yields exactly one component of the graph
                G_d = nx.subgraph(G, rel_d)
                components = list(nx.connected_components(G_d))
                if len(components) > 1:
                    a = list(components[0])[0]
                    b = list(components[1])[0]

                    # calculate subset of minimal ab separators
                    paths = [path[1:-1] for path in nx.node_disjoint_paths(G, a, b)]
                    for sep in itertools.product(*paths):
                        if not any(plz in rel_d for plz in sep):
                            model.cbLazy(x[a, d] + x[b, d] - quicksum(x[plz, d] for plz in sep) <= 1)
                            return None

    #  def cb_sep_violation(model, where):
    #      global sep_count
    #      sep_count = 0
    #      if where == GRB.Callback.MIPSOL:
    #          rel = model.cbGetSolution(x)
    #
    #          #Iterate all districts to check their connectivity
    #          for district in range(k):
    #
    #              assignedNodes = [node for node in list(G.nodes) if round(rel[node, district]) == 1]
    #
    #              for a in assignedNodes:
    #
    #                  A_a = [n for n in G.neighbors(a)]
    #                  for b in assignedNodes:
    #                      if a != b and b not in A_a:
    #
    #                          V = G
    #
    #                          #  A_a = [n for n in V.neighbors(a)]
    #                          A_union = [a] + A_a
    #                          for i in A_union:
    #                              for j in A_union:
    #                                  if i != j and V.has_edge(i,j):
    #                                      V.remove_edge(i,j)
    #
    #                          V.remove_nodes_from(A_a)
    #
    #                          R_b = nx.bfs_edges(V,b)
    #                          R_b = [b] + [v for u, v in R_b]
    #
    #                          intersection = list(set(A_union) & set(R_b))
    #
    #                          model.cbLazy(rel[a, district] + rel[b, district]
    #                                  - quicksum(rel[i, district] for i in
                                        #  intersection)<=1)

    model.write('model.lp')
    model.optimize(cb_sep_violation)

    return model



if __name__ == "__main__":

    shp_file_centeroid = "data/plz-5stellig-centroid.shp"
    shp_file  = "data/plz-5stellig.shp"
    csv_zuordnung  = "data/zuordnung_plz_ort.csv"

    df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    G = helperfunctions.createGraph(df_Border)

    k = 3
    req_p = 340000
    solve(G, k, req_p)

