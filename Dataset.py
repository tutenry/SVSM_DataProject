import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset1 = pd.read_csv("Dataset1.csv")
dataset2019 = pd.read_csv("Dataset2019.csv")
dataset2018 = pd.read_csv("Dataset2018.csv")
dataset2017 = pd.read_csv("Dataset2017.csv")
dataset2016 = pd.read_csv("Dataset2016-Large.csv").dropna()
dataset2015 = pd.read_csv("Dataset2015-Large.csv").dropna()
dataset2014 = pd.read_csv("Dataset2014-Large.csv").dropna()
dataset2013 = pd.read_csv("Dataset2013.csv").dropna()
dataset2012 = pd.read_csv("Dataset2012.csv").dropna()


dataCompare = pd.concat([dataset2019, dataset2018, dataset2017, dataset2016, dataset2015, dataset2014, dataset2013, dataset2012], axis=0)

datasetTech1 = pd.merge(dataset1, dataCompare, on=["Breakdowns", "Year"])
data = datasetTech1[datasetTech1["State Name"]=="United States"]
data2 = data[data["Breakdowns"]=="Retail Trade"][["Topic", "Percentage", "Year", "Employment", "Firms", "Establishments", "Enterprise Size", "Annual Payroll ($1,000)"]]


print("Created dataset")
data2.to_csv("data2.csv")