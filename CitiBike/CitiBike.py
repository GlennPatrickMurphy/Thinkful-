# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:49:03 2016

@author: GlennMurphy
"""

import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite

#request pulling the data off the internet
r= requests.get('http://www.citibikenyc.com/stations/json')

key_list=[]

for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

df=json_normalize(r.json()['stationBeanList'])

# plottoing
df['availableBikes'].hist()
plt.title('Available Bikes')
plt.show() 

df['totalDocks'].hist()
plt.title('Total Docks')
plt.show()

#challenge
test_stations=df['testStation']
TTS= [1 if x==True else 0 for x in test_stations]
print "\n Amount of Test Stations {0}".format(sum(TTS))
Status=df['statusValue']
Status_In=[1 if x=='In Service' else 0 for x in Status]
Status_Not=[1 if x=='Not In Service' else 0 for x in Status]

print "\n Amount of In Service Stations {0} and amount Not In Service {1}".format(sum(Status_In),sum(Status_Not))

print "\n Mean number of Bikes in Station {0}, the median is {1}".format(df['availableBikes'].mean(),df['availableBikes'].median())

#sqlite
con = lite.connect('citi_bike.db')
cur = con.cursor()

with con:
    cur.execute('DROP TABLE IF EXISTS citibike_reference')
    cur.execute('DROP TABLE IF EXISTS available_bikes ')
with con:
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')

#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))
        
#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

#create the table
#in this case, we're concatenating the string and joining all the station ids (now with '_' and 'INT' added)
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

# a package with datetime objects
import time

# a package for parsing a string into a Python datetime object
from dateutil.parser import parse 

import collections


#take the string and parse it into a Python datetime object
exec_time = parse(r.json()['executionTime'])

with con:
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
   
id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

#loop through the stations in the station list
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']

#iterate through the defaultdict to update the values in the database
with con:
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")

print "\n 30 more minutes till code is done"      
        
for x in range(1,30) :
    r = requests.get('http://www.citibikenyc.com/stations/json')
    exec_time=parse(r.json()['executionTime'])
    with con:
         cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
    id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

    #loop through the stations in the station list
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']

    #iterate through the defaultdict to update the values in the database
    with con:
        for k, v in id_bikes.iteritems():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
    con.commit()
    time.sleep(60)
    print "\n {0} more minutes till code is done".format(30-x)

with con:
    cur.execute("SELECT * FROM available_bikes")
    rows=cur.fetchall()
    cols=[desc[0] for desc in cur.description]
    bikes=pd.DataFrame(rows,columns=cols)

