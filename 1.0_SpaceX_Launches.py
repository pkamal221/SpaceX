#!/usr/bin/env python
# coding: utf-8



# First need to create a script to call on SpaceX's open source launch APLI 

import sys
import json
import pyodbc
import requests
import numpy as np
import pandas as pd

response = requests.get("https://api.spacexdata.com/v4/launches")
full_list_of_Launches_v4 = response.json()
df_launches = pd.DataFrame()

df_launches_RocketID = []
df_launches_Success = []
df_launches_Ships = []
df_launches_Name = []
df_launches_Launch_ID = []
df_launches_Date_UTC = []
for i in range(len(full_list_of_Launches_v4)):
    #json_rockets = full_list_of_Launces_v4[i]
    df_launches_RocketID.append(full_list_of_Launches_v4[i]['rocket'])
    df_launches_Success.append(full_list_of_Launches_v4[i]['success'])
    df_launches_Ships.append(full_list_of_Launches_v4[i]['ships']) 
    df_launches_Name.append(full_list_of_Launches_v4[i]['name'])
    df_launches_Launch_ID.append(full_list_of_Launches_v4[i]['id'])
    df_launches_Date_UTC.append(full_list_of_Launches_v4[i]['date_utc'])
    
df_launches['RocketID'] = pd.Series(df_launches_RocketID)
df_launches['Success'] = pd.Series(df_launches_Success)
df_launches['Ships'] = pd.Series(df_launches_Ships)
df_launches['Name'] = pd.Series(df_launches_Name)
df_launches['Launch_ID'] =pd.Series(df_launches_Launch_ID) 
df_launches['Date_UTC'] = pd.Series(df_launches_Date_UTC)

df_launches = df_launches.explode('Ships').reset_index(drop=True)
df_launches.replace({np.inf: np.nan, -np.inf: np.nan}, inplace=True)
df_launches = df_launches.fillna(0)

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
create table Launches (
Launches_Index int IDENTITY(1,1) PRIMARY KEY,
RocketID varchar(255),
Success varchar(255),
Ships varchar(255),
Name varchar(255),
Launch_ID varchar(255),
Date_UTC datetime)''')
for index,row in df_launches.iterrows():
    cursor.execute("INSERT INTO Launches (RocketID,Success,Ships,Name,Launch_ID,Date_UTC) VALUES(?,?,?,?,?,?)",
        row.RocketID,
        row.Success,
        row.Ships,
        row.Name,
        row.Launch_ID,
        row.Date_UTC
                  )
cnxn.commit()
cursor.close()

