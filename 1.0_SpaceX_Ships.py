#!/usr/bin/env python
# coding: utf-8


# First need to create a script to call on SpaceX's open source launch APLI 
import sys
import json
import pyodbc
import requests
import numpy as np
import pandas as pd
response = requests.get("https://api.spacexdata.com/v4/ships")
full_list_of_Ships_v4 = response.json()
df_Ships = pd.DataFrame()
#df_Ships
df_Ships_Ship_ID = []
df_Ships_Launches = []
df_Ships_Name = []
df_Ships_Home_Port = []

for i in range(len(full_list_of_Ships_v4)):
    #json_rockets = full_list_of_Launces_v4[i]
    df_Ships_Ship_ID.append(full_list_of_Ships_v4[i]['id'])
    df_Ships_Launches.append(full_list_of_Ships_v4[i]['launches'])
    df_Ships_Name.append(full_list_of_Ships_v4[i]['name']) 
    df_Ships_Home_Port.append(full_list_of_Ships_v4[i]['home_port'])
df_Ships['Ship_ID'] = pd.Series(df_Ships_Ship_ID)
df_Ships['Launches'] = pd.Series(df_Ships_Launches)
df_Ships['Name'] = pd.Series(df_Ships_Name)
df_Ships['Home_Port'] = pd.Series(df_Ships_Home_Port)
df_Ships = df_Ships.explode('Launches').reset_index(drop=True)
df_Ships.replace({np.inf: np.nan, -np.inf: np.nan}, inplace=True)
df_Ships = df_Ships.fillna(0)
# DB instance identifier : database-spacex-1
# username - admin
# password = password
# host - database-spacex-1.cxujv5rff92r.us-east-1.rds.amazonaws.com
# Port - 1433
server = 'database-spacex-1.cxujv5rff92r.us-east-1.rds.amazonaws.com,1433' 
database = 'rdsadmin' 
username = 'admin' 
password = 'password' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cnxn.autocommit = True
sql = '''
create database SpaceX
'''
#cursor.execute(sql)
cursor.execute('''use SpaceX''')
cursor.execute('''
create table Ships (
Ships_Index int IDENTITY(1,1) PRIMARY KEY,
Ship_ID varchar(2555),
Launches varchar(2555),
Name varchar(2555),
Home_Port varchar(2555))''')
for index,row in df_Ships.iterrows():
    cursor.execute("INSERT INTO Ships (Ship_ID,Launches,Name,Home_Port) VALUES(?,?,?,?)",
        row.Ship_ID,
        row.Launches,
        row.Name,
        row.Home_Port
                  )
cnxn.commit()
cursor.close()






