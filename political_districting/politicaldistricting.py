import extractdata
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
from gurobipy import *

def solve(G, k, req_p):
    pass

def plotMap(df_Border, df_Center):
    df_Border = findSharedBorders(df_Border)
    G = createGraph(df_Border)


    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # fix style
    for x, y in G.edges:
        print(x,y)
        for index, row in df_Center.iterrows():
            print(row.geometry)
            if row['plz'] == x:
                point_1 = [row.geometry.centroid.x, row.geometry.centroid.y]
            elif row['plz'] == y:
                point_2 = [row.geometry.centroid.x, row.geometry.centroid.y]
            else:
                continue

        plt.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]],
            color='k', linestyle = '-', linewidth =1.0)

    df_Border.plot(label='Border', ax=ax, color='white', edgecolor='black')
    df_Center.plot(label='Center', ax=ax, marker='o', color='red', markersize=5)

    plt.axis('off')
    plt.show()


def createGraph(df_Border):
    G = nx.Graph()
    for index, row in df_Border.iterrows():
        G.add_node(row['plz'], population=row['einwohner'])
        G.add_edges_from((row['plz'], x) for x in row['neighbours'])

    return G


def findSharedBorders(df_Border):
    df_Border["neighbours"] = None

    for index, row in df_Border.iterrows():
        neighbors = df_Border[~df_Border.geometry.disjoint(row.geometry)].plz.tolist()
        neighbors = [ plz for plz in neighbors if row.plz != plz ]
        df_Border.at[index, "neighbours"] = neighbors

    return df_Border


if __name__ == "__main__":

    shp_file_centeroid = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig-centroid.shp"
    shp_file  = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig.shp"
    csv_zuordnung  = "/Users/lukasbahr/POM/political_districting/data/zuordnung_plz_ort.csv"

    df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    plotMap(df_Border, df_Center)
