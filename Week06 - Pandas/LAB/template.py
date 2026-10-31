"""
RECORD CHECK  -  my version
===========================

Name  :  Mikael Hisaindee
Lane  :  AI      (delete two)
Date  :  31/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code."""


"""This program creates a dataframe from the contents of a csv file,
 adds percentage and status, then stores it in a new file along with a graph"""
import pandas as pd

# ==================================================================== LOAD


df = pd.read_csv("./LAB/records_AI.csv")   # reads csv file and creates a dataframe from the data.

# ================================================================= PROCESS

df["percent"] = (df.rows_loaded/df.rows_expected) * 100 # adds a column that calculates percentage of rows loaded by rows expected
df["status"] = df["percent"].apply(lambda p : "OVER LIMIT" if p >= 100 else # adds column status which assigns a status to each rows depending on the percentage
                                               "WARNING"   if p >=  90 else
                                               "OK") 
# ================================================================== OUTPUT

print(f"full dataframe:\n {df}") # output of the full dataframe
print("")
print("")
print(f"filtered:\n {df[df["status"]!="OK"]}") # output of dataframe filtered by all status of records that are not ok
print("")
print("")
print(f"grouped count:\n {df.groupby("status").status.count().to_string(dtype=False)}") # output of all counts of each status of records
df.to_csv("./LAB/FullRecords.csv") # storing the full dataframe in a brand new csv file

import matplotlib.pyplot as plt # importing a library to plot graphs

df["status"].value_counts().plot(kind = "bar") # creating a bar chart for all counts of each status of records
plt.title("Number of status") 
plt.savefig("./LAB/NumberOfStatus.png") # saving the bar chart as a png file
# ==========================================================================