import extractdata
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
from gurobipy import *
import re


def solve(G, k, req_p):
    #pass
    #Initialize Model
    model = Model("Political Districting")
    model.params.LazyConstraints = 1
    
    #Set Variables: 
    for plz in list(G.nodes):
        for district in range(k):
            model.AddVar(vtype = GRB.BINARY, name="x_%s_%s" % (plz, district))


    #Set Constraints
    #Each postcode must be part of exactly one district
    for plz in list(G.nodes):
            model.addConstr(quicksum(x[plz][district] for district in range(k)) == 1 )

    #Each electoral district must comprise approximately the same number of people
    for district in range(k):
        model.addConstr(abs(quicksum(x[plz][district] for plz in list(G.nodes())) - req_p) <= 0.15*req_p )

    return model

def cb_sep_violation(model, where):
    global sep_count
    sep_count = 0
    if where == GRB.Callback.MIPSOL:
        rel = model.cbGetSolution(x)
        #Iterate all districts to check their connectivity
        for district in range(k):
            #create a subgraph of all nodes assigned to this district
            assignedNodes = [node for node in list(G.nodes) if round(rel[node, district]) == 1]
            G_sub = G.subgraph(assignedNodes)
            #check connectivity of all nodes on this subgraph

def createGraph(df_Border):
    df_Border = findSharedBorders(df_Border)
    G = nx.Graph()
    for index, row in df_Border.iterrows():
        G.add_node(row['plz'], population=row['einwohner'])
        for neighbor in row['NEIGHBORS']:
            G.add_edge(row['plz'], neighbor, capacity = 1)

    #print(list(G.nodes(data='population')))
    #print(list(G.edges()))
    
    return G


def findSharedBorders(df):

    df["NEIGHBORS"] = None

    for index, row in df.iterrows():
        neighbors = df[~df.geometry.disjoint(row.geometry)].plz.tolist()
        neighbors = [ plz for plz in neighbors if row.plz != plz ]
        df.at[index, "NEIGHBORS"] = neighbors

    return df

def plotGraph(G, df_Center):
    #Extract Centroid Coordinates as Dict to support nx.draw
    coords = df_Center.set_index("plz").T.to_dict('list')
    coords = {plz:[coords[plz][2][0].x, coords[plz][2][0].y] for plz in coords}
    #Draw Graph
    nx.draw(G, pos = coords, with_labels = True, node_color = 'r')
    plt.show()


if __name__ == "__main__":

    shp_file_centeroid = "/Users/matthias/dev/pom/political_districting/data/plz-5stellig-centroid.shp"
    shp_file  = "/Users/matthias/dev/pom/political_districting/data/plz-5stellig.shp"
    csv_zuordnung  = "/Users/matthias/dev/pom/political_districting/data/zuordnung_plz_ort.csv"

    df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    G = createGraph(df_Border)
    #solve(G, 2, 290000)
    plotGraph(G, df_Center)