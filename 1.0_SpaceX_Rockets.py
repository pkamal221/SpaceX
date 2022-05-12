#!/usr/bin/env python
# coding: utf-8




# First need to create a script to call on SpaceX's open source launch APLI 
import sys
import json
import pyodbc
import requests
import numpy as np
import pandas as pd
response = requests.get("https://api.spacexdata.com/v4/rockets")
full_list_of_Rockets_v4 = response.json()
df_Rockets = pd.DataFrame()
#df_Rockets
df_Rockets_Rocket_Name = []
df_Rockets_Country = []
df_Rockets_Company = []
df_Rockets_RocketID = []
for i in range(len(full_list_of_Rockets_v4)):
    #json_rockets = full_list_of_Launces_v4[i]
    df_Rockets_Rocket_Name.append(full_list_of_Rockets_v4[i]['name'])
    df_Rockets_Country.append(full_list_of_Rockets_v4[i]['country'])
    df_Rockets_Company.append(full_list_of_Rockets_v4[i]['company']) 
    df_Rockets_RocketID.append(full_list_of_Rockets_v4[i]['id'])
df_Rockets['Rocket_Name'] = pd.Series(df_Rockets_Rocket_Name)
df_Rockets['Country'] = pd.Series(df_Rockets_Country)
df_Rockets['Company'] = pd.Series(df_Rockets_Company)
df_Rockets['RocketID'] = pd.Series(df_Rockets_RocketID)

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
create table Rockets (
RocketID varchar(255) PRIMARY KEY,
Rocket_Name varchar(255),
Country varchar(255),
Company varchar(255))''')
for index,row in df_Rockets.iterrows():
    cursor.execute("INSERT INTO Rockets (RocketID,Rocket_Name,Country,Company) VALUES(?,?,?,?)",
        row.RocketID,
        row.Rocket_Name,
        row.Country,
        row.Company
                  )
cnxn.commit()
cursor.close()

