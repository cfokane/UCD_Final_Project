import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
data = pd.read_csv('RDCDFinal.csv')
#RDCD['Deaths_%_Cases'] = (RDCD['Weekly_Deaths']*100 / RDCD['Weekly_Cases']).round(1)
data=(data.pivot_table(values=['Weekly_Cases', 'total_cases'], index=['Week_Num'], aggfunc='sum', fill_value=0))

# create a cumulative cases % of world population using 7757382765 as the world population
data['Cases_%_ World Population'] = (data['Weekly_Cases']*100 / 7757382765).round(3)
data['Cum_Cases_%_ World Population'] = (data['total_cases']*100 / 7757382765).round(3)

print(data)

fig, ax = plt.subplots(figsize=(12,5))
plt.style.use('seaborn-whitegrid')
ax.plot(data.index, data['Cum_Cases_%_ World Population'], color='b', label='Cumulative Cases % of World Pop')
ax.set_ylabel('Cumulative Cases as % of World Population', color='b')
ax.tick_params('y', colors='blue')
plt.xlim(1, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.ylim(0, 0.55) #to set the axis ...xlim for x axis
plt.yticks([.1, .15, .2, .25, .3, .35, .40, .45,],['.1%', '.15%', '.2%', '.25', '.3%', '.35', '.4%', '.45'])
ax2 = ax.twinx()
ax2.plot(data.index, data['Cases_%_ World Population'], color='red', label='Weekly Cases % of World Pop')
ax2.set_ylabel('Weekly Case Numbers as % Of World Population', color='red')
ax2.tick_params('y', colors='red')
ax.set_title('Global Infection Rates: Cumulatively and Weekly')
ax2.annotate('Weekly Infections as % of World Pop continue to increase', xy=(38.8, .026),  xycoords='data',
                xytext=(-450, -65), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), color='red',wrap=True)

ax.annotate('Global Cases almost 0.5% of World Population', xy=(39, 0.42),  xycoords='data',
                xytext=(-220, -150), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), color='blue', wrap=True)

ax.annotate('Wave 1 Peak 0.025% of World Population infected', xy=(15, 0.025),  xycoords='data',
                xytext=(-100, 50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), color='blue', wrap=True)
plt.grid(True)
ax.legend()
ax2.legend(loc=2)
plt.show()
fig.savefig('Global Infection Rates; Cumulative and Weekly.png')
plt.close()
