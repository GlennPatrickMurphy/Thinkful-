# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:43:01 2017

@author: GlennMurphy
"""
import sqlite3 as lite
import csv
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import rcParams
import scipy.stats as sp


rcParams['figure.figsize'] = 5, 5

con=lite.connect('gdp.db')
cur=con.cursor()

con1=lite.connect('Countries_Education.db')
cur1=con1.cursor()


with con:
    cur.execute('DROP TABLE IF EXISTS gdp')
   
with con:
    cur.execute('CREATE TABLE gdp (country_name TEXT, _1999 REAL, _2000 REAL, _2001 REAL, _2002 REAL, _2003 REAL, _2004 REAL, _2005 REAL, _2006 REAL, _2007 REAL, _2008 REAL, _2009 REAL, _2010 REAL);')


with open('GDP.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
    next(inputFile)
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
       with con:
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[43:-6]) + '");')
            
GDP_Table=pd.read_sql_query("SELECT * FROM gdp",con)

Education_Table=pd.read_sql_query("SELECT * FROM Education",con1)

Comparison=pd.DataFrame()

for index,row in Education_Table.iterrows():
    
    a="_"+str(Education_Table.loc[index,'Year'])
    
    country=Education_Table.loc[index,'Countries']
    
    b=GDP_Table[GDP_Table['country_name']==country].index.tolist()
    
    
    try:
        if b[0]!=50:
            Education_Table.loc[index,'GDP']=np.log(GDP_Table.loc[b[0],a])
    except IndexError:
        pass
    if math.isnan(Education_Table.loc[index,'GDP'])==True:
        Education_Table.loc[index,'GDP']=0

Education_Table=Education_Table[Education_Table.GDP != 0]    
 
plt.plot(Education_Table['Total'],Education_Table['GDP'],"o")   
plt.xlabel("Total Schooling Years")
plt.ylabel("Country's GDP")      

pearval=sp.pearsonr(Education_Table['Total'],Education_Table['GDP'])


print "The pearsons correlation value is {0}.\nSince this is above 0, but below 1, it is somewhat correlated.\nThe Pvalue is {1}.\nThis low value means the Null Hypothesis can be rejected.\nTherefore it can be said that countries that have more schooling \nare more likely to have a higher GDP".format(pearval[0],pearval[1])