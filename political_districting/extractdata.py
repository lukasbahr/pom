import pandas as pd
import geopandas as gpd

def getPolititcalDistrictData(shp_file_centeroid, shp_file, csv_zuordnung,
        state = "Saarland"):
    """
    Return border and center geopanda dataframe containing all plz of
    a specific state. Default state being Saarland.

    """
    # Create drop list of plz not in a state
    df_PLZ_BL = getDF_CSVZuordnung(csv_zuordnung, state)
    drop = list(df_PLZ_BL['plz'])

    # Drop plz in geopanda dataframes
    df_Border = dropPLZ(shp_file, drop)
    df_Center = dropPLZ(shp_file_centeroid, drop)

    # Check if rows of dataframes are matching
    if len(df_Border)  == len(df_Center) == len(df_PLZ_BL):
        # Merge state column to geopanda dataframe
        df_Border = df_Border.merge(df_PLZ_BL[['bundesland', 'plz']], left_on =
                'plz', right_on = 'plz')
        df_Center = df_Center.merge(df_PLZ_BL[['bundesland', 'plz']], left_on =
                'plz', right_on = 'plz')

        return df_Border, df_Center

    else:
        print("Rows of dataframes are not matching.")


def dropPLZ(path, drop_plz):
    """
    Return a geopanda dataframe for only specified plz.

    """
    df = gpd.read_file(path)
    # Drop all not necessary plz
    df.drop(df[~df['plz'].str.contains('|'.join(str(x) for x in
        drop_plz))].index, axis=0, inplace=True)
    df.drop(['note'], axis=1, inplace = True)
    df['plz'] = df['plz'].astype(int)

    return df


def getDF_CSVZuordnung(path, state):
    """
    Return a panda dataframe with plz of a specified state.
    For state = "Germany" return all plz of Germany.

    """
    df = pd.read_csv(path)
    df.drop_duplicates(subset ="plz", keep = 'first', inplace = True)

    if state != "Germany":
        df.drop(df[df['bundesland'] != state].index, axis=0, inplace=True)

    return df
