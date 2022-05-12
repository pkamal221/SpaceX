#!/usr/bin/env python
# coding: utf-8



import sys
import json
import pyodbc
import requests
import numpy as np
import pandas as pd
df_GDP = pd.read_csv('GDP_Countries.csv')

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
create table GDP (
Country varchar(255),
Region varchar(255),
GDP_In_Million_USD varchar(255))''')
for index,row in df_GDP.iterrows():
    cursor.execute("INSERT INTO GDP (Country,Region,GDP_In_Million_USD) VALUES(?,?,?)",
        row.Country,
        row.Region,
        row.GDP_In_Million_USD
                  )
cnxn.commit()
cursor.close()






