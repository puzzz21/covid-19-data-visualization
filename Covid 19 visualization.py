#!/usr/bin/env python
# coding: utf-8

# WHO COVID 19 data visualization using matplotlib

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes.Axes as ax
import statsmodels.api as sm
import seaborn as sns

sns.set()

# In[2]:


fullData = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")
fullData.head()

dataGroupedByLocation = dict(fullData.groupby("location").groups)

for location in dataGroupedByLocation:
    # Total Cases
    totalCases = list(dict(fullData[fullData.location.str.contains(location)]["total_cases"]).values())
    dates = list(dict(fullData[fullData.location.str.contains(location)]["date"]).values())
    xAxisData = dates[0:len(dates): int(len(dates) / 7)]

    fig, ax = plt.subplots()
    ax.plot(totalCases)
    plt.suptitle(location)
    ax.set_title("TOTAL CASES")
    plt.xlabel("dates")
    plt.ylabel("population")
    ax.set_xticklabels(xAxisData, rotation=45)

    # New Cases and Death Count
    newCases = list(dict(fullData[fullData.location.str.contains(location)]["new_cases"]).values())
    newDeaths = list(dict(fullData[fullData.location.str.contains(location)]["new_deaths"]).values())

    fig, ax = plt.subplots()
    ax.plot(newCases, label="new cases")
    ax.plot(newDeaths, label="deaths")
    plt.legend()
    plt.suptitle(location)
    ax.set_title("New cases and deaths")
    plt.xlabel("dates")
    plt.ylabel("population")
    ax.set_xticklabels(xAxisData, rotation=45)