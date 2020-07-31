import numpy as np
import pandas as pd
from gurobipy import *

def read_ElspotPrices(filename):
    # TODO
    df = pd.concat(pd.read_html(filename, header = 2, decimal = ',')) #liest Daten und macht Spalten [0,1] zu individuellen Datenindizes
    df.rename(columns={'Unnamed: 0':'Day'}, inplace = True)
    df['Dateindex'] = None
    space = " "
    for index, row in df.iterrows():
        df.at[index,'Dateindex'] = pd.to_datetime(space.join([str(df['Day'][index]), str(df['Hours'][index]).split()[0]]), format = "%d-%m-%Y %H")
    df.set_index('Dateindex', inplace = True)
    df.drop(columns=['Day', 'Hours'], inplace = True)
    return df # Returning a pandas dataframe

def removeDaylightSavings(df):
    #find index of first shift: from normal- to summertime (row with no timediff to previous row)
    index1 = df.index.get_loc(df[df.isnull().all(axis = 1)].index.item())
    #find index of second shift: from summer- bach to normaltime
    timediffs = pd.Series(df.index).diff() # Calculate time difference between indices
    index2 = timediffs[timediffs == pd.Timedelta(0)].idxmax() #  Find row with no time-difference
    #shift Data from [index1+1:index2] 1 hour into the past and delete the row with the double index
    df[index1:index2+1] = df[index1:index2+1].shift(periods = -1)
    df.dropna(how = 'all', inplace = True)
    #shift time-index to UTC+0 
    df = df.shift(periods = -1, freq = 'h')
    return df