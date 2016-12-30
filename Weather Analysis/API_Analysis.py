# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:29:07 2016

@author: GlennMurphy
"""

import pandas as pd
import sqlite3 as lite
import datetime
import matplotlib.pyplot as plt


con = lite.connect('weather.db')
cur = con.cursor()

df=pd.read_sql_query("SELECT * FROM Weather ORDER BY day_of_reading",con,index_col='day_of_reading')


start_day=df.index[0]

start_day=datetime.datetime.fromtimestamp(start_day).strftime('%Y-%m-%d')

end_day=df.index[len(df.index)-1]

end_day=datetime.datetime.fromtimestamp(end_day).strftime('%Y-%m-%d')

max_temp=df.max(0)

max_temp_city=max_temp[max_temp==max(max_temp)].index[0]

range_temp=df.max(0)-df.min(0)

range_temp_city=range_temp[range_temp==max(range_temp)].index[0]

var_temp=df.var(0)

var_temp_city=var_temp[var_temp==max(var_temp)].index[0]

print "\nThe following temperatures were collected between {0} to {1} through DarkSky.Net".format(start_day,end_day)
print "\nThe max temperature was {0}F seen in {1}".format(max(max_temp),max_temp_city)
print "\nThe largest max temperature range was {0}F seen in {1}".format(max(range_temp),range_temp_city)
print "\nThe largest temperature variance was {0}F seen in {1}\n\n".format(max(var_temp),var_temp_city)

var_temp.plot(kind='bar').set_title('Temperature Variance')