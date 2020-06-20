#!/usr/bin/env python
# coding: utf-8

# WHO COVID 19 data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


# In[10]:


data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")
countries = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/locations.csv")
for country in countries.location:
    plt.suptitle(country)
    plt.xlabel("dates")
    plt.ylabel("total cases")
    total_cases = list(dict(data[data.location.str.contains(country)]["total_cases"]).values())
    dates = list(dict(data[data.location.str.contains(country)]["date"]).values())
    totalCasesByDate = dict(zip(dates, total_cases))
    xAxisPoints = list(totalCasesByDate.keys())[0:len(totalCasesByDate):15]
    fig, ax = plt.subplots() 
    ax.set_xticklabels(xAxisPoints, rotation=45)
    ax.plot(list(totalCasesByDate.values()))