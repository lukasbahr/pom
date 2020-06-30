import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
from gurobipy import *
import re

# Enable high resolution plots
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

def getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung):

    df_PLZ_BL = getDF_CSVZuordnung(csv_zuordnung)
    drop = list(df_PLZ_BL['plz'])

    df_Border = getDF_SHPFile(shp_file, drop)
    df_Center = getDF_SHPFileCenteroid(shp_file_centeroid, drop)

    df = pd.concat([df_Border, df_Center], axis = 1)
    df = df.loc[:,~df.columns.duplicated()]
    df = df.set_index('plz')

    return df

def getDF_SHPFileCenteroid(path, drop):
    df = gpd.read_file(path)
    df.drop(df[~df['plz'].str.contains('|'.join(str(x) for x in drop))].index, axis=0, inplace=True)
    df.rename(columns={'geometry':'geometry_center'}, inplace = True)

    return df

def getDF_SHPFile(path, drop):
    df = gpd.read_file(path)
    #  print(df.size)
    df.drop(df[~df['plz'].str.contains('|'.join(str(x) for x in drop))].index, axis=0, inplace=True)
    df.rename(columns={'geometry':'geometry_border'}, inplace = True)

    return df

def getDF_CSVZuordnung(path):
    df = pd.read_csv(path)
    df.drop_duplicates(subset ="plz", keep = 'first', inplace = True)
    df.drop(df[df['bundesland'] != "Saarland"].index, axis=0, inplace=True)

    return df




if __name__ == '__main__':
    import sys

    shp_file_centeroid = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig-centroid.shp"
    shp_file  = "/Users/lukasbahr/POM/political_districting/data/plz-5stellig.shp"
    csv_zuordnung  = "/Users/lukasbahr/POM/political_districting/data/zuordnung_plz_ort.csv"

    getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)

