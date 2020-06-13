import pandas as pd
import math as math


def getHospitalData(full_path_instance):
    """
    input: path to csv file containing hospitalsital network df
    output: hospitalsitals - name of hospitalsitals
            cities - name of cities
            h_coord - hospitalsital coordinates
            c_coord - city coordinates
            coord - coordinates [[x_y_h_coordinates], [x_y_c_coordinates]]
            c - cost [[costk1], [costk2], [costk3]]
            b - capacity [[capk1], [capk2], [capk3]]
            g - closing income
            citiesSpecial - cities with minimum hospitalsital size 2 [cities]
    """

    df = pd.read_csv(full_path_instance, header = None) 

    idx = []
    for i in df.index:
        if df.iloc[i,0][0] == '#':
            idx.append(i)

    # Get hospitals
    hospitals = df.iloc[idx[0]:idx[1],:]
    hospitals.columns = hospitals.iloc[0]
    hospitals = hospitals.drop(hospitals.index[0])
    hospitals.dropna(axis='columns', inplace = True)
    J = list(hospitals.iloc[:,0])

    # Get closing hospitals
    closingHospitals = df.iloc[idx[1]:idx[2],:]
    closingHospitals.columns = closingHospitals.iloc[0]
    closingHospitals = closingHospitals.drop(closingHospitals.index[0])
    closingHospitals.dropna(axis='columns', inplace = True)
    J_2 = list(closingHospitals.iloc[:,0])

    # Get cities
    cities = df.iloc[idx[2]:idx[3],:]
    cities.columns = cities.iloc[0]
    cities = cities.drop(cities.index[0])
    cities.dropna(axis='columns', inplace = True)
    I = list(cities.iloc[:,0])

    # Get special cities
    specialCities = df.iloc[idx[3]:,:]
    specialCities.columns = specialCities.iloc[0]
    specialCities = specialCities.drop(specialCities.index[0])
    specialCities.dropna(axis='columns', inplace = True)
    I_2 = list(specialCities.iloc[:,0])

    # Set hospital sizes
    K = [1, 2, 3]

    # Transform column names
    hospitals.set_index(hospitals.columns[0], inplace = True)
    hospitals = hospitals.astype('int64')

    cities.set_index(cities.columns[0], inplace = True)
    cities = cities.astype('int64')

    closingHospitals.set_index(closingHospitals.columns[0], inplace = True)
    closingHospitals = closingHospitals.astype('int64')

    # Set cloing income, capacity and cost
    g = {}
    for j in J_2:
        g[j] = closingHospitals.loc[j, ' closing_income']

    c = {}
    b = {}
    for k in K:
        for j in J:
            b[k,j] = hospitals.loc[j, ' capk'+str(k)]
            c[k,j] = hospitals.loc[j, ' costk'+str(k)]

    print(c)

    return hospitals, cities, J, J_2, I, I_2, g, b, c, K

