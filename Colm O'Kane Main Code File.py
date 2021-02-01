import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame


#Read source CSV's into project file, Simplify columns to needed columns only, output as dataframes

Trans_Data = pd.read_csv('transformed_data.csv')
#print(Trans_Data.columns)
#CD1 =Trans_Data.loc[:,['CODE', 'COUNTRY', 'DATE', 'HDI']]
#CD1 = pd.DataFrame(CD1)

Raw = pd.read_csv('raw_data.csv')
#print(Raw.columns)
RD =Raw.loc[:,['iso_code', 'location', 'date', 'total_cases', 'total_deaths',
       'stringency_index', 'population', 'gdp_per_capita',
       'human_development_index']]
RD = pd.DataFrame(RD)

States = pd.read_csv('states.csv')
#print(States.columns)
EU =States.loc[:,['Country', 'European Union', 'Area (km²)', 'European Single Market']]
EU = pd.DataFrame(EU)

Countries = pd.read_csv('countries_of_the_world.csv')
#print(Countries.columns)
Countries2=Countries.loc[:,['Country','Region', 'Area (sq. mi.)']]
#print(Countries2)
countries2 = pd.DataFrame(Countries2)

# Merge EU data into CD Data
RD = (RD.merge(countries2, how='left', left_on='location', right_on='Country'))
print(RD)

# Create Key to merge data together
#CD1.sort_values('DATE')
#CD1['KEYCODE&DATE'] = CD1['CODE'] + CD1['DATE']
#RD.sort_values('date')
RD['KEYCODE&DATE'] = RD['iso_code'] + RD['date']
print(RD['KEYCODE&DATE'])
#print(CD1['KEYCODE&DATE'])

#Sort rows before creating new data series
RD['DATE'] = pd.to_datetime(RD['date'], format='%Y/%m/%d')
#CD1['DATE'] = pd.to_datetime(CD1['DATE'], format='%Y/%m/%d')

#print(CD1.columns)
print(RD.columns)
print(EU.columns)

# Merge EU data into RD Data using 'outer' join and forward fill
RD= (pd.merge_ordered(RD, EU, left_on='location', right_on='Country', how='outer', fill_method='ffill'))
print(RD.head)
print(RD.dtypes)
print(RD.isna().any())

#CD.fillna(0)
#RD['European Union']=RD['European Union'].fillna('European Free Trade Agreement')
#RD['European Single Market']= RD['European Single Market'].fillna('Member')
RD.fillna(0)
print(RD.isna().sum())
RD.to_csv('RD.csv')


print(RD)

#Create new fields re Dates
RD['DATE'] = pd.to_datetime(RD['date'], format='%Y/%m/%d')
print(RD['date'])
# Create Key Fields for future reference
RD['Week_Num'] = RD['DATE'].dt.strftime('%U') #number of the week in the year
RD['Month'] = RD['DATE'].dt.strftime('%b') #short name of the month
RD['day'] = RD['DATE'].dt.strftime('%A') #day of the week
RD['dayz'] = RD['DATE'].dt.strftime('%j') #number of the day in the year
RD['Dates'] = RD['DATE'].dt.strftime('%Y%m%d') #dont think this is doing anything useful
RD['Wednesdays'] = RD['day'] == 'Wednesday' #boolean set to confirm Wednesday as True



# add columns with comparable measures
RD['Cases_x_Area'] = (RD['total_cases'] / RD['Area (sq. mi.)']).round(1) #change name to mls2
RD['Cases_x_Pop'] = (RD['total_cases'] / RD['population']).round(1)
RD['Cumulative Deaths_%_Cases']= (RD['total_deaths'] / RD['total_cases']).round(1)
#RDCD['AreaKM2'] =RDCD['Area (km²)'] #new field Change Name to Area(mls².)
RD['PopMi2'] =(RD['population'] / RD['Area (sq. mi.)']).round(1) #new field Change Name to Pop(mls².)
#RDCD['Cases per AreaKM²'] = (RDCD['total_cases'] / RDCD['Area (sq. mi.)']).round(2) #Change Name

#Change Govt'stringency_index' measure to a comparable index (0-5) called Stringency_Indexed
RD['Stringency_Indexed']=(RD['stringency_index'] / 20).round()
#print(RDCD.columns) #work back to exclude unused columns here with new dataframe
#print(RDCD.dtypes)
print(RD)
# park/remove unneeded rows
#del RDCD['Unnamed: 9']
#del RDCD['Unnamed: 10']
#del RDCD['Unnamed: 11']
#del RDCD['Unnamed: 12']
#del RDCD['Unnamed: 13']
#del RDCD['GDP per capita ($, millions)']
#del RDCD['GDP ($, millions)']
#del RDCD['GDP (€, millions)']


# Create groups of counties/Economic Blocks from Dictionary
econ_blocks = {
    'Country': ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia',
                'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania',
                'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain',
                'Sweden', 'United Kingdom', 'Brazil', 'Russia', 'India', 'China', 'South Africa', 'United States'],
    'Econ_Block': ['EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU',
                   'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'BRICS', 'BRICS', 'BRICS', 'BRICS',
                   'BRICS', 'US']}
#convert econ_block to dataframe
Econ_BLocks = pd.DataFrame(econ_blocks)

# Merge Econ_BLocks dataset to enhance RDCD dataset
RDCD = (RD.merge(Econ_BLocks, left_on='location', right_on='Country', how='outer'))

# check for missing data
#print(RDCD)
#print(RDCD.isna().sum())


#Replace Missing Values by filling 'na's with 'No_Affiliation' identifier
RDCD.fillna(0)
RDCD['Econ_Block'] = RDCD['Econ_Block'].fillna('All_Others')


# Create a Weekly Dataset to using Wednesday as the filter to give a weekly reporting day
RDCD=RDCD.query('day == "Wednesday"')

# Calculate Weekly Change in Cases & Deaths from cumulative data within dataset
RDCD['Weekly_Cases']=(RDCD.groupby('iso_code')['total_cases'].diff())
RDCD['Weekly_Deaths']=(RDCD.groupby('iso_code')['total_deaths'].diff())

RDCD['Weekly_Deaths'].fillna(0)

#filter the data set for relevant dates
RDCD=RDCD.query("DATE >= '2020-01-07' and DATE <='2020-09-30'")

#output this to csv
RDCD.to_csv('RDCDbasechecking.csv')

# ***** New csv basefile
RDCD1 = pd.read_csv('RDCDbasechecking.csv')
RDCD1=RDCD1.query("location != 'Hong Kong'")
print(RDCD1.columns)
#(RDCD1.isna().any())
#print(RDCD1.isna().sum())
#print(RDCD1.dtypes)

#opportunity here to read in certain columns
del RDCD1['dayz']
del RDCD1['Country_y']
del RDCD1['human_development_index']
del RDCD1['Country_x']
del RDCD1['Area (km²)']
del RDCD1['gdp_per_capita']
del RDCD1['Unnamed: 0']
del RDCD1['Wednesdays']
del RDCD1['Country']


print(RDCD1.columns)
#(RDCD1.isna().any())
print(RDCD1.isna().sum())
#print(RDCD1.dtypes)
#output this to csv

RDCD1.to_csv('RDCDFinal.csv')