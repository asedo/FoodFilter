# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from plotly.graph_objs import *
init_notebook_mode()


file = "./Playdata.xlsx"
#df = pd.read_excel(file, sheetname = 'Sheet1', header = 0, index_col = 0, convert_float = True)
#dv = pd.read_excel(file, sheetname = 'Sheet3', header = 0, index_col = 0, convert_float = True)
df = pd.read_excel(file, sheetname = 'Sheet1', header = 0, convert_float = True)
dv = pd.read_excel(file, sheetname = 'Sheet3', header = 0, index_col = 0, convert_float = True)

df['protein_percent'] = df['protein']/dv['DV']['Protein'] *100
df['totalcal'] = df['calperserv']/dv['DV']['Caloriesm'] * 100
df['foodtext'] = "\nCalories : " + str(df['calperserv']) + "\nProtein : " + str(df['protein'])

foodgrp_key= list(set(df['foodgroup']))
grp_val = list(map(int,range(len(foodgrp_key))))
grphash = dict(zip(foodgrp_key,grp_val))

for i in df[["foodgroup"]]:
  print(grphash[df["foodgroup"][i]])

    
grphash[]

print(foodgroups)
   
plot({
    'data': [
        Scatter(x=df['calperserv'],
                y=df['score'],
                text=df['foodtext'],
                marker=Marker(size=df['calperserv'], sizemode='area'),   #, sizeref=131868,),
                mode='markers',
                fillcolor=foodgroupcolors) 
    ],
    'layout': Layout(title='Nutrition and Calorie Count',xaxis=XAxis(title='Calories per Serving'), yaxis=YAxis(title='Nutrition 1-10'))
}, show_link=False)


        
#df = pd.read_csv('https://plot.ly/~etpinard/191.csv')

#plot({
#    'data': [
#        Scatter(x=df[continent+', x'],
#                y=df[continent+', y'],
#                text=df[continent+', text'],
#                marker=Marker(size=df[continent+', size'], sizemode='area', sizeref=131868,),
#                mode='markers',
#                name=continent) for continent in ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
#    ],
#    'layout': Layout(xaxis=XAxis(title='Life Expectancy'), yaxis=YAxis(title='GDP per Capita', type='log'))
#}, show_link=False)

#df = pd.read_csv('https://plot.ly/~etpinard/191.csv')
#plt.scatter(x = df['totalcal'], y = df['protein_percent'], s = np.array(df['fullnessfactor']) ** 4, c = "blue" , alpha = 0.8)




#print(foodgroup)

col = ['red',
 'green',
 'blue',
 'blue',
 'yellow',
]
cal_per_serving = [974.58033839999996,
 937.0295259999984,
 223.3674650000003,
 797.2312670000001,
 779.379639999999]
nutrition = [43.828000000000003,
 76.423000000000002,
 72.301000000000002,
 42.731000000000002,
 75.319999999999993 ]

fullness = [31.889923,
 3.6005229999999999,
 33.333216,
 12.420476000000001,
 40.301926999999999]
 
 # Scatter plot
#plt.scatter(x = df['totalcal'], y = df['protein_percent'], s = np.array(df['fullnessfactor']) * 2, c = df['foodgroup'], alpha = 0.8)
plt.scatter(x = df['totalcal'], y = df['protein_percent'], s = np.array(df['fullnessfactor']) ** 4, c = "blue" , alpha = 0.8)

# Previous customizations
#plt.xscale('log') 
plt.xlabel('Calories per serving')
plt.ylabel('Nutrition 1-10 [1 worst - 10 Best]')
plt.title('Nutrition and Calorie count')

#add Text to the graph
#for (X, Y, Z) in zip(df['totalcal'],df['protein_percent'], df['name']):
#    plt.annotate(Z, xy=(X,Y), xytext=(-10, 10), ha='right',
    #                textcoords='offset points')

    
#plt.xticks([0,.5, 1], ['Low Calerie','Mid Calorie','High Calorie'])

#plt.xscale('log') 
#plt.xlabel('Health-O-Meter')
#plt.ylabel('Life Expectancy [in years]')
#plt.title('Bubble Chart for food')
#plt.xticks([Person 1,Person 2,Both], ['1k','10k','100k'])

# Additional customizations
#plt.text(df['totalcal'], 80, 'Kale')
#plt.text(5700, 80, 'China')

plt.grid(True)

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()