import datapreparation
import priceprediction
import numpy as np
import pandas as pd
from tqdm.auto import tqdm, trange
from gurobipy import *


def solve(prices,
          Pmax,
          Emax,
          E0,
          print_result=False):
    
    model = Model("Aluminum DSM")
    model.modelSense = GRB.MINIMIZE
    
    # If you test the model for one timestep, you probably want the usual gurobi
    # output, but if you run this model a lot (for every time-step...) this will
    # spam your output window, so i recommend to set print_result=False
    if not print_result:
        model.setParam('OutputFlag', False)
        
    # TODO: Implement model

    T = range(len(prices))

    dP = {}
    dE = {}
    for t in T:
        dP[t] = model.addVar(name = "dP_%s" % (t), lb = -Pmax, ub = Pmax)
        dE[t] = model.addVar(name = "dE_%s" % (t), lb = -Emax, ub = Emax)

    #update the model
    model.update()

    #Energy Balance
    for t in T:
        if t == 0:
            model.addConstr(dP[t] + E0 == dE[t])
        else:
            model.addConstr(dE[t-1]+dP[t] == dE[t])

    #neutral energy balance at the end
    for t in T:
        if t == len(T)-1:
            model.addConstr(dE[t] == 0)

    #set objective function and call optimization
    model.setObjective(quicksum(prices[t]*dP[t] for t in T))
    model.optimize()

    return model, dP, dE


def runScenario(historic_prices,             # Historic electricty prices
                E0, Emax, Pmax,              # Plant parameters
                prediction_method,           # Prediction settings
                t_start, t_end, t_horizon):  # Simulation times

    # You probably have to prepare some stuff here
    T = pd.date_range(t_start, t_end, freq="H")
    results = pd.DataFrame(index = T, columns = {"Power", "Energy", "Earnings"})

    for t in tqdm(T):
        # Prepare price data for model
        predictor = priceprediction.PredictionGenerator(historic_prices, method=prediction_method)
        predicted_prices = predictor.predict(t, t_horizon) # returns a series of "predicted" prices

        # Run model & save results for current timestep
        model, dP, dE = solve(predicted_prices, Pmax, Emax, E0, False)

        #write results
        results.at[t, 'Power'] = dP[0].X
        results.at[t, 'Energy'] = dE[0].X
        results.at[t, 'Earnings'] = dP[0].X*historic_prices[t]

        # "Update world state":
        # - Set E0 based on optimization results for current time step
        E0 = dE[0].X
    
        # Write current results to console
        tqdm.write("%s: P = %s, E = %s, earnings = %s" % (t, results.at[t, 'Power'],  E0, results.at[t, 'Earnings']))
        
    return results # I recommend storing your results in a dataframe as well, for easier plotting


if __name__ == "__main__":

    #Data Preparation
    path = "elspot-prices_2019_hourly_eur.xls"
    df = datapreparation.read_ElspotPrices(path)
    df = datapreparation.removeDaylightSavings(df)

    # Get data
    market_area = "SE1"
    historic_prices = df[market_area]
    prediction_method = "SameHourLastWeek"      # methods = ["Perfect", "SameHourLastWeek"]

    # Plant parameters
    E0 = 0                                      # Energy difference at t = t_start
    Pmax = 100                                  # Maximum power deviation in MW
    Emax = 48 * Pmax                            # Maximum energy deviation in MWh

    # Simulation parameters
    t_start = pd.Timestamp("2019-10-22 00:00:00")   # Times are in UTC+0
    t_end = pd.Timestamp("2019-12-21 23:00:00")     # Simulate two months of operation
    t_horizon = 7*24                                # Time horizon for optimization (in h)

    results = runScenario(historic_prices,            # Historic electricty prices
                E0, Emax, Pmax,             # Plant parameters
                prediction_method,          # Prediction settings
                t_start, t_end, t_horizon)  # Simulation times)
    print(results)



