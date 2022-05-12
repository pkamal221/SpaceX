#!/usr/bin/env python
# coding: utf-8




import sys
import json
import pyodbc
import requests
import numpy as np
import pandas as pd
response = requests.get("https://api.spacexdata.com/v4/payloads")
full_list_of_Payloads_v4 = response.json()
df_Payloads = pd.DataFrame()
df_Payload_PayloadID = []
df_Payload_LaunchID = []
df_Payload_Nationality = []
df_Payload_Name = []


for i in range(len(full_list_of_Payloads_v4)):
    #json_rockets = full_list_of_Launces_v4[i]
    df_Payload_PayloadID.append(full_list_of_Payloads_v4[i]['id'])
    df_Payload_LaunchID.append(full_list_of_Payloads_v4[i]['launch'])
    df_Payload_Nationality.append(full_list_of_Payloads_v4[i]['nationalities']) 
    df_Payload_Name.append(full_list_of_Payloads_v4[i]['name'])
    
df_Payloads['PayloadID'] = pd.Series(df_Payload_PayloadID)
df_Payloads['LaunchID'] = pd.Series(df_Payload_LaunchID)
df_Payloads['Nationality'] = pd.Series(df_Payload_Nationality)
df_Payloads['Name'] = pd.Series(df_Payload_Name)
df_Payloads = df_Payloads.explode('Nationality').reset_index(drop=True)
df_Payloads.replace({np.inf: np.nan, -np.inf: np.nan}, inplace=True)
df_Payloads = df_Payloads.fillna(0)
df_Payloads = df_Payloads[df_Payloads['Nationality']!=0]

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
create table Payloads (
PayloadID varchar(255) PRIMARY KEY,
LaunchID varchar(255),
Nationality varchar(255),
Name varchar(255))''')
for index,row in df_Payloads.iterrows():
    cursor.execute("INSERT INTO Payloads (PayloadID,LaunchID,Nationality,Name) VALUES(?,?,?,?)",
        row.PayloadID,
        row.LaunchID,
        row.Nationality,
        row.Name
                  )
cnxn.commit()
cursor.close()

