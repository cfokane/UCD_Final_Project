import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams

#Bubble Chart, cases per Area on YTD Wk39
data = pd.read_csv('RDCDFinal.csv', index_col=0)
data=data.query('Week_Num== 39')
print(data.columns)
PopDen=(data.pivot_table(values=['PopMi2'], index='location', aggfunc='sum', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])
PopDen.to_csv('PopDen.csv')
CaseArea=(data.pivot_table(values=['Cases_x_Area'], index='location', aggfunc='sum', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])
CaseArea.to_csv('CaseArea.csv')
print(CaseArea)


data2= pd.read_csv('PopDen.csv')
data2a=data2.sort_values('location')
print(data2a)
data3 = pd.read_csv('CaseArea.csv')
data3a=data3.sort_values('location')
print(data3a)

fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(data3a['Cases_x_Area'], data2a['PopMi2'], s=data3a['Cases_x_Area']**1.5)



plt.xlabel('Cases per Mi²')
plt.ylabel('Population Density (per Mi²)')
plt.title('5 Most Densely Populated countries have the highest Infecton Rate per Square Mile', wrap=True)
plt.xlim(0, 150)
plt.yscale('log')
plt.subplots_adjust(top=0.95, left=0.15)
plt.yticks([50, 250, 500, 1000, 2500, 5000, 10000, 20000],['50/Mi²','250/Mi²', '500/Mi²', '1000/Mi²', '2500/Mi²', '5000/Mi²', '10000/Mi²', '20000 People/Mi²'])
plt.grid(True)
ax.annotate('Monaco recorded 107 cases per Mi²', xy=(107, 20000),  xycoords='data',
                xytext=(-10, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True, color='red')
ax.annotate('Bahrain 106 cse/Mi²', xy=(106, 2600),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )
ax.annotate('Singapore 83 cse/Mi²', xy=(83, 8400),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )
ax.annotate('Vatican 60 cse/Mi²', xy=(60, 4045),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )
ax.annotate('Gibralter 56 cse/Mi²', xy=(56, 4813),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )

plt.text(3, 80, '} Lower Cases per Mi² where Population Density is lower')
plt.show()
fig.savefig('Correlation between Population Density & Cases Globally.png')
plt.close()