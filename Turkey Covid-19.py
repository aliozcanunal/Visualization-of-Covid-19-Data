# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:02:50 2020

@author: aozcanunal
"""

import datetime
import requests

from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

url="https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json"
alldata= requests.get(url).json()

deaths= []
date = []
confirmed = []
Turkey= []
recovered=[]

for dates in alldata['Turkey']:
    if dates['confirmed'] >=1:
    
    
        date_time_obj = datetime.datetime.strptime(dates['date'], '%Y-%m-%d')
    
        date.append( date_time_obj.strftime('%m'))
    
        confirmed.append(dates["confirmed"])
        recovered.append(dates["recovered"])
    
        deaths.append(dates["deaths"])	

death = deaths[-1]
confirme = confirmed[-1]
recovere = recovered[-1]

figure(num=None, figsize=(93,16), dpi=90, facecolor='w', edgecolor='k')
style.use('ggplot')    

title = 'Covid-19 Turkey'
plt.xlabel('Number of days since the first case')
plt.ylabel('Cases')
plt.title(title)

plt.text(75,3000000,recovere, size=10)

plt.text(75,3300000,confirme, size=10)

plt.text(75,3150000,death, size=10)

plt.plot(confirmed,'r',label="Number of people infected")
plt.plot(deaths,'b--',label="Number of Death")
plt.plot(recovered,'g--',label="Number of Recovered")
plt.legend()
plt.show()

