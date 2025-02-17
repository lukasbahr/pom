import networkx as nx
from gurobipy import *

def solve(G, k, req_p):
    #pass
    #Initialize Model
    model = Model("Political Districting")
    model.params.LazyConstraints = 1

    x = {}
    #Set Variables:
    for plz in list(G.nodes()):
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

    def min_ab_sep(G, C_i, C_j):
        #copy G for edge deletion
        G_copy = G.copy()
        #find neigbors of C_i
        A_C_i = []
        for node in C_i:
            u = [n for n in G.neighbors(node) if n not in C_i]
            A_C_i = A_C_i + u
        #remove edges from Ci to ACi and between ACi
        for i in C_i:
            for l in A_C_i:
                if G_copy.has_edge(i,l):
                    G_copy.remove_edge(i,l)
                elif G_copy.has_edge(l,i):
                    G_copy.remove_edge(l,i)

        for i in A_C_i:
            for l in A_C_i:
                if G_copy.has_edge(i,l):
                    G_copy.remove_edge(i,l)
        #select node from Cj and find all connected nodes           
        j = C_j[0]
        R_j = nx.node_connected_component(G_copy, j)

        #determine minimal a,b-separator
        intersection = list(set(A_C_i) & set(R_j))

        return intersection

    def cb_sep_violation(model, where):
        if where == GRB.Callback.MIPSOL:
            rel = model.cbGetSolution(x)
            for district in range(k):
                assignedNodes = [node for node in list(G.nodes) if round(rel[node, district]) == 1]

                G_copy = G.copy()
                H = nx.subgraph(G, assignedNodes)
                comp = list(nx.connected_components(H))
                if len(comp) >= 2:
                    C_i = list(comp[0])
                    C_j = list(comp[1])
                    #determine minimal a,b-separator for two connected components of district
                    N = min_ab_sep(G, C_i, C_j)
                    #select two nodes for constraint to be added
                    i = C_i[0]
                    j = C_j[0]
                    #add connectivity constraint
                    model.cbLazy(x[i, district] + x[j, district] - quicksum(x[plz,district] for plz in N) <= 1)

    model.optimize(cb_sep_violation)

    return model
    
# if __name__ == "__main__":

#    shp_file_centeroid = "data/plz-5stellig-centroid.shp"
#    shp_file  = "data/plz-5stellig.shp"
#    csv_zuordnung  = "data/zuordnung_plz_ort.csv"

#    df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
#    G = helperfunctions.createGraph(df_Border)

#    k = 3
#    req_p = 340000
#    model = solve(G, k, req_p)













