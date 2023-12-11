# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:28:37 2023

@author: baongoc.thai
"""
#%%
import os
import pandas as pd
import math

#%% Working folder
path = r'S:\01_PROJECTS\SG1013 H2i-C2021-009-PUB-Pandan_Rsvr_WQ_Modelling\Working document\GCM data analysis\GCM-hourly-solar-radiation'
os.chdir(path)

df_solar = pd.read_csv("Hourly solar radiation_GCM_BN1.csv",parse_dates = [0],dayfirst=True)
df_solar.index = df_solar.pop('Date')
sunrise_time = 7
day_length = 12
df_temp = []
df_hourly_solar =[]

for k in range(len(df_solar)):
    for i in range(8,20):
        temp = ((math.sin(math.pi*(i-sunrise_time)/day_length))*2)**2*df_solar.iloc[k][0]
        df_temp.append(temp)
    df_hourly_solar.append(df_temp)
    print(df_solar.index[k], k)
    df_temp = []

df_hourly_solar_unpack = pd.DataFrame(sum(df_hourly_solar, []))

time_index = []
for k in range(len(df_solar)):
    for i in range(8,20):
        timestamp = df_solar.index[k] + pd.Timedelta(hours=i)
        time_index.append(timestamp)
        
df_hourly_solar_unpack.index = time_index
df_hourly_solar_unpack.columns = ['DateTime','Solar radiation']
df_hourly_solar_unpack.to_csv('Hourly_Solar_radiation_Pandan.csv')
