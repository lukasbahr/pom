# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:40:35 2020

@author: flori
"""


from gurobipy import *
import math as math
import pandas as pd

def solve(full_path_instance):
    """
    Parameters
    ----------
    path: full path instance

    Returns
    -------
    model
    """
    ############# Preprocessing ##############
    data = pd.read_csv(full_path_instance, header = None) # import data

    ind = [] # get indices from data file
    for i in data.index:
        # get first element of string
        if data.iloc[i,0][0] == '#':
            ind.append(i)

    hosp = data.iloc[ind[0]:ind[1],:]
    hosp.columns = hosp.iloc[0]
    hosp = hosp.drop(hosp.index[0])
    hosp.dropna(axis='columns', inplace = True)

    old_hosp = data.iloc[ind[1]:ind[2],:]
    old_hosp.columns = old_hosp.iloc[0]
    old_hosp = old_hosp.drop(old_hosp.index[0])
    old_hosp.dropna(axis='columns', inplace = True)

    cities = data.iloc[ind[2]:ind[3],:]
    cities.columns = cities.iloc[0]
    cities = cities.drop(cities.index[0])
    cities.dropna(axis='columns', inplace = True)

    old_cities = data.iloc[ind[3]:,:]
    old_cities.columns = old_cities.iloc[0]
    old_cities = old_cities.drop(old_cities.index[0])
    old_cities.dropna(axis='columns', inplace = True)

    # make relevant Sets (I, I_2, J, J_2, K)
    # list of all cities
    I = list(cities.iloc[:,0])
    # list of cities with old population
    I_2 = list(old_cities.iloc[:,0])
    # list of all possible hospitals
    J = list(hosp.iloc[:,0])
    # list of preexisting hospitals
    J_2 = list(old_hosp.iloc[:,0])
    # list of possible hospital sizes
    K = [1, 2, 3]

    # set first columns of "hosp", "cities" and "old_hosp" as row indices and change type to integer
    hosp.set_index(hosp.columns[0], inplace = True)
    hosp = hosp.astype('int64')
    cities.set_index(cities.columns[0], inplace = True)
    cities = cities.astype('int64')
    old_hosp.set_index(old_hosp.columns[0], inplace = True)
    old_hosp = old_hosp.astype('int64')

    # make distance dict d_j_i
    d = {}
    for j in J:
        for i in I:
            d[j,i] = math.sqrt( (hosp.loc[j, ' x_coord'] - cities.loc[i, ' x_coord'])**2 + (hosp.loc[j, ' y_coord'] - cities.loc[i, ' y_coord'])**2 )

    # make closing_income dict g_j
    g = {}
    for j in J_2:
        g[j] = old_hosp.loc[j, ' closing_income']

    # make hospital-capacity dict b_k_j and building_costs dict c_k_j
    b = {}
    c = {}
    for k in K:
        for j in J:
            b[k,j] = hosp.loc[j, ' capk'+str(k)]
            c[k,j] = hosp.loc[j, ' costk'+str(k)]

    print(b)
    print(c)
    print(g)


    ############# Model ##################
    model = Model("Hospital NetwORk Model")
    model.modelSense = GRB.MINIMIZE

    # make relevant x_j_i variables, describing wether hospital j serves city i (x_j_i = 1) or not (x_j_i = 0)
    x = {}
    for j in J:
        for i in I:
            if d[j,i] <= 30:
                x[j,i] = model.addVar(name="x_%s_%s" % (j,i), vtype="b")

    # make y_k_j variables, describing wether hospital j exists in size k (y_k_j = 1) or not (y_k_j = 0)
    y = {}
    for k in K:
        for j in J:
            y[k,j] = model.addVar(name="y_%s_%s" % (str(k),j), vtype="b")

    # update the model
    model.update()

    ############# Constraints ###############
    # every hospital exists in max. one size-configuration
    for j in J:
        model.addConstr( quicksum(y[k,j] for k in K) <= 1 )


    # hospital capacities are not exceeded
    for j in J:
        model.addConstr( quicksum(x[j,i] for i in I if d[j,i] <= 30) <= quicksum(y[k,j]*b[k,j] for k in K) )

    # every city gets exactly one hospital assigned to it
    for i in I:
        model.addConstr( quicksum(x[j,i] for j in J if d[j,i] <= 30) == 1 )

    # max. distances of hospital-city-pairings are not exceeded
    for j in J:
        for i in I:
            if d[j,i] <= 30:
                model.addConstr( x[j,i]*d[j,i] <= 20*y[1,j]+20*y[2,j]+30*y[3,j] )

    # old-people-cities get adequately large hospitals assigned to them
    for j in J:
        for i in I_2:
            if d[j,i] <= 30:
                model.addConstr( y[2,j]+y[3,j] >= x[j,i] )

    ############ Solve ################
    model.setObjective( quicksum(y[k,j]*c[k,j] for k in K for j in J) - quicksum(g[j]*(1 - quicksum(y[k,j] for k in K)) for j in J_2) ,GRB.MINIMIZE)
    model.optimize()
    
    model.write('model.lp')
    
    return model


