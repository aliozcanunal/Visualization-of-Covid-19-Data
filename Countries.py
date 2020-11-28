# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 03:32:34 2020

@author: aozca
"""

import datetime
import requests

from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure



url="https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json"
alldata= requests.get(url).json()

figure(num=None, figsize=(55,25), dpi=90, facecolor='w', edgecolor='k')
style.use('ggplot')

title = 'Covid-19 World'
plt.title(title)

plt.xlabel('Dates')
plt.ylabel('Cases')


deaths= []
date = []
confirmed = []



i = 0

for country in alldata:
    if country == "US":
        continue
    for day in alldata[country]:
        confirmed.append(day["confirmed"])
        date_time_obj = datetime.datetime.strptime(day['date'], '%Y-%m-%d')
        date.append( date_time_obj.strftime('%m-%d  '))
        
#    if confirmed[-1] < 80000:
#        confirmed=[]
#        date=[]
#        continue
    
    plt.plot(date ,confirmed,label=country)
    confirmed=[]
    date=[]
#    i += 1
#    if i > 1:
#        break
        

plt.legend()
plt.show()
#

