# Plottin the uber pick up points for a perticulat Suunday and Monday
# author: Vishnu Vardhan Kumar Pallati(01468680)
# The required CSV files have to be in the same directory of the python file

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#map for Sunday - 4/6/2014
data = pd.read_csv("uber-raw-data-apr14.csv", parse_dates=['Date/Time'])
data = (data[6966:7787])


my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('Uber Pickup Points - Sunday - 4/6/2014')
plt.show()




#map for Monday - 4/7/2014
data = pd.read_csv("uber-raw-data-apr14.csv", parse_dates=['Date/Time'])
data = (data[7787:9161])

print(data)
my_map =  Basemap(projection='merc', lat_0 = 57, lon_0 = -130,
    resolution = 'h', area_thresh = 1000, llcrnrlon=-77,llcrnrlat=38,urcrnrlon=-70,urcrnrlat=42,)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white')
my_map.drawmapboundary()
 

x, y = my_map(data['Lon'].values, data['Lat'].values)
# draw a red dot at cities coordinates
plt.plot(x, y, 'ro', markersize=1, marker='.')
plt.title('Uber Pickup Points - Monday- 4/7/2014')
plt.show()
