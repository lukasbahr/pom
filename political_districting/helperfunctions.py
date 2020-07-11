import extractdata
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
from gurobipy import *


def plotMap(df_Border, df_Center):
    df_Border = findSharedBorders(df_Border)
    G = createGraph(df_Border)


    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # fix style
    for x, y in G.edges:
        for index, row in df_Center.iterrows():
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


def createGraph(df_Border):
    df_Border = findSharedBorders(df_Border)
    G = nx.Graph()
    for index, row in df_Border.iterrows():
        G.add_node(row['plz'], population=row['einwohner'], district=0)
        for neighbour in row['neighbours']:
            G.add_edge(row['plz'], neighbour, capacity = 1)

    return G


def findSharedBorders(df_Border):
    df_Border["neighbours"] = None

    for index, row in df_Border.iterrows():
        neighbors = df_Border[~df_Border.geometry.disjoint(row.geometry)].plz.tolist()
        neighbors = [ plz for plz in neighbors if row.plz != plz ]
        df_Border.at[index, "neighbours"] = neighbors

    return df_Border


def plotGraph(G, df_Center):
    #Extract Centroid Coordinates as Dict to support nx.draw
    coords = df_Center.set_index("plz").T.to_dict('list')
    coords = {plz:[coords[plz][2][0].x, coords[plz][2][0].y] for plz in coords}
    #Draw Graph
    nx.draw(G, pos = coords, with_labels = True, node_color = 'r')
    plt.show()


#  if __name__ == "__main__":
    #
    #  shp_file_centeroid = "data/plz-5stellig-centroid.shp"
    #  shp_file  = "data/plz-5stellig.shp"
    #  csv_zuordnung  = "data/zuordnung_plz_ort.csv"
    #
    #  df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    #  plotMap(df_Border, df_Center)

    # Matthias
    #  G = createGraph(df_Border)
    #solve(G, 2, 290000)
    #  plotGraph(G, df_Center)
