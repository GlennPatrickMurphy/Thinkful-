# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:40:07 2016

@author: GlennMurphy
"""

from bs4 import BeautifulSoup
import pandas as pd 
import requests 
import sqlite3 as lite
import matplotlib.pyplot as plt
import pylab
from pylab import rcParams
rcParams['figure.figsize'] = 30, 5

#sqlite
con = lite.connect('Countries_Education.db')
cur = con.cursor()

with con:
    cur.execute('DROP TABLE IF EXISTS Education')

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
r=requests.get(url)

soup=BeautifulSoup(r.content,'html.parser')
    
rows=soup.findAll('tr',attrs={'class','tcont'})

with con:
    cur.execute('CREATE TABLE Education (Countries REAL, Year INT, Total INT, Men INT,Women INT);')

for tr in rows:
    cols=tr.findAll('td')
    table=[c.text for c in cols]
    with con:
        cur.execute("INSERT INTO Education(Countries,Year,Total,Men,Women) Values(?,?,?,?,?)",(table[0],table[1],table[4],table[7],table[10]))
    if table[0]=="Zimbabwe":
        break

Education_Table=pd.read_sql_query("SELECT * FROM Education ORDER BY Countries" ,con,index_col='Countries')

Edu_Year_Mean=Education_Table['Year'].mean()
Edu_Men_Mean=Education_Table['Men'].mean()
Edu_Women_Mean=Education_Table['Women'].mean()
Edu_Total_Mean=Education_Table['Total'].mean()

Edu_Year_Med=Education_Table['Year'].median()
Edu_Men_Med=Education_Table['Men'].median()
Edu_Women_Med=Education_Table['Women'].median()
Edu_Total_Med=Education_Table['Total'].median()



Education_Table['Year'].plot(kind='bar').set_title('Year Distribution')
pylab.ylim([1990,2017])
plt.figure(1)
pylab.savefig('Year Distrbution')
Education_Table['Total'].plot(kind='bar').set_title('Total Distribution')
plt.figure(2)
pylab.savefig('Total Distribution')
Education_Table['Men'].plot(kind='bar').set_title('Men Distribution')
plt.figure(3)
pylab.savefig('Men Distribution')
Education_Table['Women'].plot(kind='bar').set_title('Women Distribution')
plt.figure(4)
pylab.savefig('Women Distribution')


