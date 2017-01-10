# Plotting the Uber trips avg per hour for apr 2014 to sep 2014
# author: Vishnu Vardhan Kumar Pallati (01468680)
# The required CSV files should be in the same folder of the pythonm file


import pandas as pd
import matplotlib.pyplot as plt

result = pd .DataFrame()

#april
data = pd.read_csv("uber-raw-data-apr14.csv", parse_dates=['Date/Time'])
grp = data.groupby(by=[data['Date/Time'].map(lambda x : x.hour)], as_index=False).size()
x = pd.DataFrame(grp)
x.columns = ['count']
x['count'] = x['count'] / 30
#print (x)
result['april'] = x['count']

#may
data = pd.read_csv("uber-raw-data-may14.csv", parse_dates=['Date/Time'])
grp = data.groupby(by=[data['Date/Time'].map(lambda x : x.hour)], as_index=False).size()
x = pd.DataFrame(grp)
x.columns = ['count']
x['count'] = x['count'] / 30
#print (x)
result['may'] = x['count']

#june
data = pd.read_csv("uber-raw-data-jun14.csv", parse_dates=['Date/Time'])
grp = data.groupby(by=[data['Date/Time'].map(lambda x : x.hour)], as_index=False).size()
x = pd.DataFrame(grp)
x.columns = ['count']
x['count'] = x['count'] / 30
#print (x)
result['june'] = x['count']

#july
data = pd.read_csv("uber-raw-data-jul14.csv", parse_dates=['Date/Time'])
grp = data.groupby(by=[data['Date/Time'].map(lambda x : x.hour)], as_index=False).size()
x = pd.DataFrame(grp)
x.columns = ['count']
x['count'] = x['count'] / 30
#print (x)
result['july'] = x['count']

#august
data = pd.read_csv("uber-raw-data-aug14.csv", parse_dates=['Date/Time'])
grp = data.groupby(by=[data['Date/Time'].map(lambda x : x.hour)], as_index=False).size()
x = pd.DataFrame(grp)
x.columns = ['count']
x['count'] = x['count'] / 30
#print (x)
result['august'] = x['count']

#september
data = pd.read_csv("uber-raw-data-sep14.csv", parse_dates=['Date/Time'])
grp = data.groupby(by=[data['Date/Time'].map(lambda x : x.hour)], as_index=False).size()
x = pd.DataFrame(grp)
x.columns = ['count']
x['count'] = x['count'] / 30
#print (x)
result['september'] = x['count']
print(result)


plt.plot(result.index, result['april'], label='April')
plt.plot(result.index, result['may'], label='May')
plt.plot(result.index, result['june'], label='June')
plt.plot(result.index, result['july'], label='July')
plt.plot(result.index, result['august'], label='August')
plt.plot(result.index, result['september'], label='September')
plt.xlabel('Hour')
plt.ylabel('avg number of trips')
plt.title('Uber trips avg per hour for apr to sept')
plt.legend()
plt.show()
