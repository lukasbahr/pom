import extractdata
import helperfunctions
import networkx as nx
from gurobipy import *

#  def solve(G, k, req_p):
#      #pass
#      #Initialize Model
#      model = Model("Political Districting")
#      model.params.LazyConstraints = 1
#
#      x = {}
#      #Set Variables:
#      for plz in list(G.nodes):
#          for district in range(k):
#              x[plz, district] = model.addVar(vtype = GRB.BINARY, name="x_%s_%s" % (plz, district))
#
#      model.update()
#
#      #Set Constraints
#      #Each postcode must be part of exactly one district
#      for plz in list(G.nodes):
#              model.addConstr(quicksum(x[plz, district] for district in range(k)) == 1 )
#
#      #Each electoral district must comprise approximately the same number of people
#      for district in range(k):
#          model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population'] for plz in list(G.nodes())) <= 1.15 * req_p)
#          model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population'] for plz in list(G.nodes())) >= 0.85 * req_p)
#
#      def cb_sep_violation(model, where):
#          global sep_count
#          sep_count = 0
#          if where == GRB.Callback.MIPSOL:
#              rel = model.cbGetSolution(x)
#              print("tes")
#
#              #Iterate all districts to check their connectivity
#              for district in range(k):
#
#                  assignedNodes = [node for node in list(G.nodes) if round(rel[node, district]) == 1]
#
#                  for a in assignedNodes:
#                      for b in assignedNodes:
#                          if a != b:
#
#                              A_union = [n for n in G.neighbors(a)]
#                              # change
#                              for node in A_union:
#                                  G.remove_edge(a, node)
#
#                              R_b = nx.bfs_edges(G,b)
#                              R_b = [b] + [v for u, v in R_b]
#
#                              intersection = list(set(A_union) & set(R_b))
#
#                              model.addConstr(rel[a, district] + rel[b, district]
#                                      - quicksum(rel[i, district] for i in
#                                          intersection)<=1)
#
#      #  model.setObjective(1, GRB.MINIMIZE)
#      model.write('model.lp')
#      model.optimize(cb_sep_violation)
#
#      return model
#

def solve(G, k, req_p):
    D = range(1, k + 1)  # Districts
    V = list(G.nodes)  # Postcodes
    p = {}  # population of each postcode
    for a, k in G.nodes.data():
        p[a] = k['population']

    model = Model("political_districting")
    model.params.LazyConstraints = 1

    x = {}
    for plz in V:
        for d in D:
            x[plz, d] = model.addVar(vtype=GRB.BINARY, name="x_{}_{}".format(plz, d))

    # every plz has to be assigned to exactly one district
    for plz in V:
        model.addConstr(quicksum(x[plz, d] for d in D) == 1)

    # the total population of each district d may not deviate from the required population per district by more than 15%
    for d in D:
        model.addConstr(quicksum(p[plz] * x[plz, d] for plz in V) >= (1 - 0.15) * req_p)
        model.addConstr(quicksum(p[plz] * x[plz, d] for plz in V) <= (1 + 0.15) * req_p)

    # callback: continuity requirement
    def callback(model, where):
        if where == GRB.Callback.MIPSOL:
            print("test")
            rel = model.cbGetSolution(x)
            for d in D:
                rel_d = [plz for plz in V if round(rel[plz, d]) == 1]
                # check whether the current solution yields exactly one component of the graph
                G_d = nx.subgraph(G, rel_d)
                components = list(nx.connected_components(G_d))
                if len(components) > 1:
                    a = list(components[0])[0]
                    b = list(components[1])[0]

                    # calculate subset of minimal ab separators
                    paths = [path[1:-1] for path in nx.node_disjoint_paths(G, a, b)]
                    for sep in product(*paths):
                        if not any(plz in rel_d for plz in sep):
                            model.cbLazy(x[a, d] + x[b, d] - quicksum(x[plz, d] for plz in sep) <= 1)
                            return None

    model.write('model_v.lp')
    model.optimize(callback)


    return model


if __name__ == "__main__":

    shp_file_centeroid = "data/plz-5stellig-centroid.shp"
    shp_file  = "data/plz-5stellig.shp"
    csv_zuordnung  = "data/zuordnung_plz_ort.csv"

    df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    G = helperfunctions.createGraph(df_Border)

    k = 3
    req_p = 3400000
    solve(G, k, req_p)

    #print(list(G.nodes))

