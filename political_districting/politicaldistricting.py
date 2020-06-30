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
    print(df)


if __name__ == "__main__":

    shp_file_centeroid = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig-centroid.shp"
    shp_file  = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig.shp"
    csv_zuordnung  = "/Users/lukasbahr/POM/political_districting/data/zuordnung_plz_ort.csv"

    df = extractdata.getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
    createGraph(df)
