import extractdata
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
from gurobipy import *
import re


def solve(G, k, req_p):
    pass


def createGraph(df):
    G = nx.Graph()
    for index, row in df.iterrows():
        G.add_node(row['plz'], population=row['einwohner'])

    #  print(list(G.nodes(data='population')))


    return G

def findSharedBorders(df):
    df["NEIGHBORS"] = None  # add NEIGHBORS column

    for index, row in df.iterrows():
        # get 'not disjoint' countries

        print(row['geometry_border'].disjoint(row['geometry_border']))
        neighbors = df[~df.geometry_border.disjoint(row.geometry_border)].plz.tolist()
        #  # remove own name from the list
        #  neighbors = [ name for name in neighbors if row.plz != name ]
        #  # add names of neighbors as NEIGHBORS value
        #  df.at[index, "NEIGHBORS"] = ", ".join(neighbors)
#
    print(type(df))

if __name__ == "__main__":

    shp_file_centeroid = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig-centroid.shp"
    shp_file  = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig.shp"
    csv_zuordnung  = "/Users/lukasbahr/POM/political_districting/data/zuordnung_plz_ort.csv"

    df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    #  createGraph(df)
    findSharedBorders(df_Border)
