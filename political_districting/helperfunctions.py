import extractdata
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
from gurobipy import *
import politicaldistricting


def plotMap(df_Border, df_Center):
    df_Border = findSharedBorders(df_Border)
    G = createGraph(df_Border)

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
    df_Border = findSharedBorders(df_Border)
    G = nx.Graph()
    for index, row in df_Border.iterrows():
        G.add_node(row['plz'], population=row['einwohner'])
        for neighbour in row['neighbours']:
            G.add_edge(row['plz'], neighbour)

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

def plotDistricts(model, k, df_Border):
    df_Border = findSharedBorders(df_Border)
    districtedPlz = allocateDistricts(model, k)

    df_Border["district"] = None
    for index, row in df_Border.iterrows():
        for district, plz in districtedPlz.items():
            if row["plz"] in plz:
                d = district
                break
        df_Border.at[index, "district"] = d

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    print(df_Border)
    df_Border.plot(column = "district", legend = True, label='Border', ax=ax)
    plt.axis('off')
    plt.show()

def allocateDistricts(model, k):
    districtedPlz = {d: [] for d in range(k)}
    for item in model.getVars():
        if abs(item.x) == 1:
            districtedPlz[int(item.VarName.split('_')[-1])].append(int(item.VarName.split('_')[1]))
    return districtedPlz

if __name__ == "__main__":

    shp_file_centeroid = "data/plz-5stellig-centroid.shp"
    shp_file  = "data/plz-5stellig.shp"
    csv_zuordnung  = "data/zuordnung_plz_ort.csv"

    df_Border, df_Center = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    #plotMap(df_Border, df_Center)

    # Matthias
    k = 3
    req_p = 340000
    G = createGraph(df_Border)
    model = politicaldistricting.solve(G, k, req_p)
    #plotGraph(G, df_Center)
    plotDistricts(model, k, df_Border)
