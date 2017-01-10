# Plottin the uber pick up points from Apr 2014 to Sept 2014
# author: Vishnu Vardhan Kumar Pallati(01468680)
# The required CSV files have to be in the same directory of the python file

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# http://introtopython.org/visualization_earthquakes.html
#map for apr
data = pd.read_csv("uber-raw-data-apr14.csv", parse_dates=['Date/Time'])
print(data['Lat'])

my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('UBER PICKUPS Apr 2014')
plt.show()





#map for may
data = pd.read_csv("uber-raw-data-may14.csv", parse_dates=['Date/Time'])
print(data['Lat'])

my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('UBER PICKUP POINTS - May 2014')
plt.show()






#map for June
data = pd.read_csv("uber-raw-data-jun14.csv", parse_dates=['Date/Time'])
print(data['Lat'])

my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('UBER PICKUP POINTS - June 2014')
plt.show()




#map for july
data = pd.read_csv("uber-raw-data-jul14.csv", parse_dates=['Date/Time'])
print(data['Lat'])



my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('UBER PICKUP POINTS - July 2014')
plt.show()





#map for aug
data = pd.read_csv("uber-raw-data-aug14.csv", parse_dates=['Date/Time'])
print(data['Lat'])



my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('UBER PICKUP POINTS - Aug 2014')
plt.show()





#map for Sep
data = pd.read_csv("uber-raw-data-sep14.csv", parse_dates=['Date/Time'])
print(data['Lat'])



my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('UBER PICKUP POINTS - Sept 2014')
plt.show()

