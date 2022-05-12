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
df_Core_Landing_Result = pd.DataFrame()

df_Core_Landing_Result_Cores = []
df_Core_Landing_Result_CoreID = []
df_Core_Landing_Result_Launch_ID = []
df_Core_Landing_Result_LandingResult = []
for i in range(len(full_list_of_Launches_v4)):
    for k in range(len(full_list_of_Launches_v4[i]['cores'])):
        df_Core_Landing_Result_Launch_ID.append(full_list_of_Launches_v4[i]['id'])
        df_Core_Landing_Result_CoreID.append(full_list_of_Launches_v4[i]['cores'][k]['core'])
        df_Core_Landing_Result_LandingResult.append(full_list_of_Launches_v4[i]['cores'][k]['landing_success'])
        
df_Core_Landing_Result['LaunchID'] = pd.Series(df_Core_Landing_Result_Launch_ID)
df_Core_Landing_Result['CoreID'] = pd.Series(df_Core_Landing_Result_CoreID)
df_Core_Landing_Result['LandingResult'] = pd.Series(df_Core_Landing_Result_LandingResult)

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
create table Cores_Landing_Result (
Cores_Landing_Index int IDENTITY(1,1) PRIMARY KEY,
LaunchID varchar(255),
CoreID varchar(255),
LandingResult varchar(255))''')
for index,row in df_Core_Landing_Result.iterrows():
    cursor.execute("INSERT INTO Cores_Landing_Result (LaunchID,CoreID,LandingResult) VALUES(?,?,?)",
        row.LaunchID,
        row.CoreID,
        row.LandingResult
                  )
cnxn.commit()
cursor.close()

