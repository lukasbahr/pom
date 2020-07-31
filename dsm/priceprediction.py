import pandas as pd
import numpy as np

# You do not have to touch this code
class PredictionGenerator():
    def __init__(self, timeseries, method="perfect"):
        self.setMethod(method)
        self.df = timeseries

    # If you use more elaborate prediction methods, you might have to fit a model to the data
    # Implementing another prediction method will not better your grade, so ignore this if you want.
    def fit(self, end_date):
        pass

    # "Predict" prices for some date range defined by a start date and a number of hours
    def predict(self, start_date, nhours):
        dates = pd.date_range(
            start=start_date,
            periods=nhours,
            freq="H")

        if self.method == "Perfect":
            if dates.max() not in self.df.index: # check if prices known
                raise Exception(("You can not forecast the *future* perfectly "
                                 "out of sample! Some of the dates requested "
                                 "are not in the given dataset."))
            result = self.df.loc[dates]  # the actual observed prices
        elif self.method == "SameHourLastWeek":
            min_date = (dates.min() + pd.DateOffset(hours=-7*24))
            max_date = (dates.max() + pd.DateOffset(hours=-7*24))
            if (min_date not in self.df.index) or (max_date not in self.df.index):
                raise Exception(("For some of the dates you tried to predict, "
                                 "there is no data from the week before available."))
            # Last weeks prices
            result = self.df.loc[dates + pd.DateOffset(hours=-7*24)]
            result.index = dates
            
        return result

    
    # Set method if known, otherwise raise exception
    def setMethod(self, method):
        methods = ["Perfect", "SameHourLastWeek"]
        if method not in methods:
            raise Exception(f"Method passed({method}) is not in ["
                            + ", ".join(methods) + "]")
        self.method = method