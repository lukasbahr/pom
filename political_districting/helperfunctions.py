import extractdata
import politicaldistricting
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
from gurobipy import *

def plotMap(df_Border, df_Center):
    """
    Plot the map of a state containing,
    * the borders of each postcode
    * the centroids of each postcode
    * the lines connecting the centroids of neighboring postcodes

    """
    df_Border = findSharedBorders(df_Border)
    G = createGraph(df_Border)

    # Create subplots
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Plot the connecting lines of all edges
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

    # Plot the border
    df_Border.plot(label='Border', ax=ax, color='blue', edgecolor='black')
    # Plot the centroids
    df_Center.plot(label='Center', ax=ax, color='red', marker = 'o',
            markersize=10)

    plt.axis('off')
    plt.show()


def createGraph(df_Border):
    """
    Return a graph from geopanda dataframe fullfilling the contiguity
    requirement.

    """
    # Find all borders for every plz in border dataframe
    df_Border = findSharedBorders(df_Border)
    # Create graph
    G = nx.Graph()
    for index, row in df_Border.iterrows():
        # Add population to node
        G.add_node(row['plz'], population=row['einwohner'])
        # Connect all neigbouring nodes
        for neighbour in row['neighbours']:
            G.add_edge(row['plz'], neighbour)

    return G


def findSharedBorders(df_Border):
    """
    Return geopanda dataframe with column of neighbouring plz.

    """
    df_Border["neighbours"] = None
    # Iterate over dataframe
    for index, row in df_Border.iterrows():
        # Make list of connecting borders
        neighbors = df_Border[~df_Border.geometry.disjoint(row.geometry)].plz.tolist()
        neighbors = [ plz for plz in neighbors if row.plz != plz ]
        # Add neighbouring plz to each plz
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
    """
    Plot the map of a state with the solution of the gurobi model.

    """
    df_Border = findSharedBorders(df_Border)
    # Find the PLZs for the districts
    df_Border = allocateDistricts(model, k, df_Border)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    df_Border.plot(column = "district", legend = True, label='Border', ax=ax)

    plt.axis('off')
    plt.show()


def allocateDistricts(model, k, df_Border):
    """
    Return hash map with keys of districts and plz as values based on the
    model.

    """
    districtedPlz = {d: [] for d in range(k)}
    for item in model.getVars():
        if abs(item.x) == 1:
            districtedPlz[int(item.VarName.split('_')[-1])].append(int(item.VarName.split('_')[1]))

    df_Border["district"] = None
    for index, row in df_Border.iterrows():
        for district, plz in districtedPlz.items():
            if row["plz"] in plz:
                d = district
                break
        df_Border.at[index, "district"] = d

    return df_Border

def printDistricts(model, k, df_Border):

    print(df_Border)
    districts = {k: dict(Population = 0, Towns = [], ) for k in range(k)}
    for index, row in df_Border.iterrows():
        districts[row["district"]]["Population"] += row["einwohner"]
        districts[row["district"]]["Towns"].append(row["note"])
    for k in districts:
        print("")
        print("District %s" % (k+1))
        print("Population: %s" % (districts[k]['Population']))
        print("Towns and Villages:")
        print(*districts[k]['Towns'], sep = ", ")
        print("")


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
    #plotMap(df_Center, df_Border)
    #  plotGraph(G, df_Center)
    plotDistricts(model, k, df_Border)
    printDistricts(model, k, df_Border)
