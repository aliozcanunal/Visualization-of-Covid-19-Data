# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:02:50 2020
 
@author: aozca
"""
 
import datetime
import numpy as np

import requests
import matplotlib as mpl

from cycler import cycler
from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

url="https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json"
alldata= requests.get(url).json()

deaths= []
date = []
confirmed = []
Turkey= []




for day in alldata:
    
   confirmed.append(day["confirmed"])
    
   date_time_obj = datetime.datetime.strptime(day['date'], '%Y-%m-%d')
   date.append( date_time_obj.strftime('%m-%d--'))
   deaths.append(day["deaths"])	
    
        
    
    
figure(num=None, figsize=(60,16), dpi=20, facecolor='w', edgecolor='k')
style.use('ggplot')

plt.plot(date,confirmed,'r',deaths,'r')




