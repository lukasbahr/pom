import extractdata
import helperfunctions
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
import math
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
        model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population'] for plz in list(G.nodes())) - req_p <= 0.15*req_p)
        model.addConstr(quicksum(x[plz, district]*G.nodes[plz]['population'] for plz in list(G.nodes())) - req_p >= -0.15*req_p)
    '''
    def cb_sep_violation(model, where):
        global sep_count
        sep_count = 0
        if where == GRB.Callback.MIPSOL:
            rel = model.cbGetSolution(x)
            #Iterate all districts to check their connectivity
            for district in range(k):
                #create a subgraph of all nodes assigned to this district
                for a in district.nodes
                    for b in district.nodes
                        if a~=b
                            #delete E[a and A(a)] from G
                            #check reachable nodes from b
                            #N is set of reachable neighbors from b
                            #N is minimum seperator for a,b
                        #if any of i in N is in district
                            #enforce Inequality


            assignedNodes = [node for node in list(G.nodes) if round(rel[node, district]) == 1]
            G_sub = G.subgraph(assignedNodes)
            #check connectivity of all nodes on this subgraph
        

    model.setObjective(1, GRB.MINIMIZE)
    model.write('model.lp')
    model.optimize(cb_sep_violation)

    return model
    '''

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

