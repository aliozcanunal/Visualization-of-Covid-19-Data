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
#   if dates['confirmed'] >=1:
    confirmed.append(dates["confirmed"])
    recovered.append(dates["recovered"])
    date_time_obj = datetime.datetime.strptime(dates['date'], '%Y-%m-%d')
    date.append( date_time_obj.strftime('%m-%d'))
    
    deaths.append(dates["deaths"])	
    
    
figure(num=None, figsize=(93,16), dpi=90, facecolor='w', edgecolor='k')
style.use('ggplot')    

title = 'Covid-19 Turkey'
plt.xlabel('Dates')

plt.ylabel('Cases')

plt.title(title)

plt.plot(date ,confirmed,'r',label="Number of people infected")
plt.plot(deaths,'b--',label="Number of Death")
plt.plot(recovered,'g--',label="Number of Recovered")
plt.legend()
plt.show()

