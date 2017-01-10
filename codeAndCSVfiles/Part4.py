# Comparing Uber pick ups with other cab services
# author: Vishnu Vardhan Kumar Pallati(01468680)
# The required CSV files have to be in the same directory of the python file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#uber jul to sep
df = pd.read_csv("uber-raw-data-jul14.csv", parse_dates=['Date/Time'])
df['Date/Time'] = df['Date/Time'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date/Time'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
df1=df
df = pd.read_csv("uber-raw-data-aug14.csv", parse_dates=['Date/Time'])
df['Date/Time'] = df['Date/Time'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date/Time'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
df2=df
df = pd.read_csv("uber-raw-data-sep14.csv", parse_dates=['Date/Time'])
df['Date/Time'] = df['Date/Time'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date/Time'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
df3=df
df = [df1, df2, df3]
result = pd.concat(df)
print(result)
plt.plot_date(result['Date'], result['num of trips'], fmt='b-', color="blue", label='Uber')

#aMERICAN CAB
df = pd.read_csv("American_B01362.csv", parse_dates=['DATE'])
df['DATE'] = df['DATE'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['DATE'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'],color="green", fmt='b-', label='American')

#Carmel CAB
df = pd.read_csv("Carmel_B00256.csv", encoding='latin-1')
df['Date'] = pd.to_datetime(df["Date"])
df['Date'] = df['Date'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'],color="red", fmt='b-', label='Carmel')

#Dial7 CAB
df = pd.read_csv("Dial7_B00887.csv", parse_dates=['Date'])
df['Date'] = df['Date'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'], fmt='b-', color="cyan", label='Dial7')

#Diplo CAB
df = pd.read_csv("Diplo_B01196.csv", encoding='latin-1')
df['Date'] = pd.to_datetime(df["Date"])
df['Date'] = df['Date'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'],color="magenta", fmt='b-', label='Diplo')


#federal
df = pd.read_csv("Federal_02216.csv", parse_dates=['Date'])
df['Date'] = df['Date'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'], fmt='b-', color="yellow", label='Federal')


#Firstclass CAB
df = pd.read_csv("Firstclass_B01536.csv",encoding='latin-1' , parse_dates=['DATE'])
df['DATE'] = df['DATE'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['DATE'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'],color="black", fmt='b-', label='Firstclass')



#Highclass CAB
df = pd.read_csv("Highclass_B01717.csv", encoding='latin-1', parse_dates=['DATE'])
df['DATE'] = df['DATE'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['DATE'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'],color='magenta', fmt='b-', label='Highclass')


#LYFT CAB
df = pd.read_csv("Lyft_B02510.csv", parse_dates=['time_of_trip'])
df['time_of_trip'] = df['time_of_trip'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['time_of_trip'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'],color='olive', fmt='b-', label='LYFT')



#PrestigeCAB
df = pd.read_csv("Prestige_B01338.csv",encoding='latin-1', parse_dates=['DATE'])
df['DATE'] = df['DATE'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['DATE'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'],color='pink', fmt='b-', label='Prestige')



#skyline
df = pd.read_csv("Skyline_B00111.csv", parse_dates=['Date'])
df['Date'] = df['Date'].apply(lambda x: x.strftime('%m-%d-%y'))
counts = df['Date'].value_counts()
df = pd.DataFrame(counts)
df.columns = ['num of trips']
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)
df = df.sort('Date')
plt.plot_date(df['Date'], df['num of trips'], fmt='b-', color='tan', label='Skyline')


plt.xlabel('TimeSpan')
plt.ylabel('number of trips')
plt.title('Uber trips avs other cab service trips')
plt.legend()
plt.show()

