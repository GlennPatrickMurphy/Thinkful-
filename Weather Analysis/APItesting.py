# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:09:26 2016

@author: GlennMurphy
"""
import calendar
import pandas as pd 
import requests
import sqlite3 as lite
import time


#building and API

cities = { "Atlanta": '33.762909,-84.422675,',
            "Austin": '30.303936,-97.754355,',
            "Boston": '42.331960,-71.020173,',
            "Chicago": '41.837551,-87.681844,',
            "Cleveland": '41.478462,-81.679435,'
        }
   
         
start_day=calendar.timegm(time.gmtime())-calendar.timegm(time.gmtime(2419200))

df=pd.DataFrame(cities.items(),columns=['City','Longitude,Latitude'])
query_day=start_day

df['Time']=start_day

df['Key']='3205dcbf17d32fd9f4dad8ec91245fe8/'

df['API']='https://api.darksky.net/forecast/'

for index, row in df.iterrows(): 
     df.loc[index,'API']='{0}{1}{2}'.format(df.loc[index,'API'],df.loc[index,'Key'],df.loc[index,'Longitude,Latitude'])

#sqlite
con = lite.connect('weather.db')
cur = con.cursor()

with con:
    cur.execute('DROP TABLE IF EXISTS Weather')
   
with con:
    cur.execute('CREATE TABLE Weather (day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL,Chicago REAL,Cleveland REAL);')

with con: 
    while query_day<calendar.timegm(time.gmtime()):
        cur.execute("INSERT INTO Weather(day_of_reading) VALUES (?)",(query_day,))
        query_day+=calendar.timegm(time.gmtime(86164))
  
for index,row in df.iterrows():
    query_day=start_day
    while query_day<calendar.timegm(time.gmtime()):
        url='{0}{1}'.format(df.loc[index,'API'],query_day)
        r=requests.get(url)
        
        with con: 
            cur.execute('UPDATE Weather SET ' + df.loc[index,'City'] + ' = '+ str(r.json()['daily']['data'][0]['temperatureMax'])+' WHERE day_of_reading = '+str(query_day))
    
        query_day+=calendar.timegm(time.gmtime(86164))
    
with con: 
    cur.execute("SELECT * FROM Weather")
    rows=cur.fetchall()
    for row in rows:
        print(rows)
con.close()     