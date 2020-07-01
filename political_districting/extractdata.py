import pandas as pd
import geopandas as gpd

def getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung):

    df_PLZ_BL = getDF_CSVZuordnung(csv_zuordnung)
    drop = list(df_PLZ_BL['plz'])

    df_Border = getDF_SHPFile(shp_file, drop)
    df_Center = getDF_SHPFileCenteroid(shp_file_centeroid, drop)

    if len(df_Border)  == len(df_Center) == len(df_PLZ_BL):
        df_Border = df_Border.merge(df_PLZ_BL[['bundesland', 'plz']], left_on = 'plz', right_on = 'plz')
        df_Center = df_Center.merge(df_PLZ_BL[['bundesland', 'plz']], left_on = 'plz', right_on = 'plz')

        return df_Border, df_Center

    else:
        print("Rows of dataframes are not matching.")


def getDF_SHPFileCenteroid(path, drop):
    df = gpd.read_file(path)
    df.drop(df[~df['plz'].str.contains('|'.join(str(x) for x in drop))].index, axis=0, inplace=True)
    df.drop(['note'], axis=1, inplace = True)
    df['plz'] = df['plz'].astype(int)

    return df

def getDF_SHPFile(path, drop):
    df = gpd.read_file(path)
    df.drop(df[~df['plz'].str.contains('|'.join(str(x) for x in drop))].index, axis=0, inplace=True)
    df.drop(['note'], axis=1, inplace = True)
    df['plz'] = df['plz'].astype(int)

    return df

def getDF_CSVZuordnung(path):
    df = pd.read_csv(path)
    df.drop_duplicates(subset ="plz", keep = 'first', inplace = True)

    # Comment to get all zip codes for germany
    df.drop(df[df['bundesland'] != "Saarland"].index, axis=0, inplace=True)

    return df


if __name__ == '__main__':
    shp_file_centeroid = "/users/lukasbahr/pom/political_districting/data/plz-5stellig-centroid.shp"
    shp_file  = "/users/lukasbahr/pom/political_districting/data/plz-5stellig.shp"
    csv_zuordnung  = "/users/lukasbahr/pom/political_districting/data/zuordnung_plz_ort.csv"

    getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung)
