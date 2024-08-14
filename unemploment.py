# -*- coding: utf-8 -*-
"""Unemploment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l7FFqJQ3pNWTDL3sOb_CsuTL-KSQdFZq

TASK 2:UNEMPLOYENT ANALYSIS WITH PYTHON
"""

# IMPORTING REQUIRED LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("/content/Unemployment in India (1).csv")
print(data.head())

print(data.isnull().sum())

data.columns= ["States","Date","Frequency",
               "Estimated unployement Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region"]

#CORRELATION
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
sns.heatmap(data.corr())
plt.show()

#DATA VISUALISATION
data.columns= ["States","Date","Frequency",
               "Estimated unployement Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region",data=data)
plt.show()

plt.figure(figsize=(12,10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated unployement Rate", hue="Region",data=data)
plt.show()

unemploment = data[["States","Region","Estimated unployement Rate"]]
figure = px.sunburst(unemploment, path=["Region","States"],
                    values="Estimated unployement Rate",
                    width=700, height=700,
                    color_continuous_scale="RdY1Gn",
                    title="Unemployment Rate in india")
figure.show()