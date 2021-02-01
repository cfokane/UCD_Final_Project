import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv', index_col=0)
Econ_cases=(data.pivot_table(values='Weekly_Cases', index='Month', columns='Region', aggfunc='sum', fill_value=0, margins=True))
# correct order of months
new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
EconCases=Econ_cases.reindex(new_order, axis=0)


print(EconCases.columns)
fig, ax = plt.subplots(figsize=(12,10))
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
h1 = EconCases["Jan":"Jun"]
ax.plot(h1.index, h1['ASIA (EX. NEAR EAST)'], label='ASIA (EX. NEAR EAST)')
ax.plot(h1.index, h1['BALTICS'], label='BALTICS')
ax.plot(h1.index, h1['WESTERN EUROPE'], label='WESTERN EUROPE')
ax.plot(h1.index, h1['EASTERN EUROPE'], label='EASTERN EUROPE')
ax.plot(h1.index, h1['NORTHERN AMERICA'], label='NORTHERN AMERICA')
ax.plot(h1.index, h1['OCEANIA'], label='OCEANIA')
ax.plot(h1.index, h1['SUB-SAHARAN AFRICA'], label='SUB-SAHARAN AFRICA')
ax.plot(h1.index, h1['LATIN AMER. & CARIB'], label='LATIN AMER. & CARIB')
#plt.xlim(1, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.yscale('log')
plt.ylim(0, 1500000) #to set the axis ...xlim for x axis
plt.yticks([500000, 1000000, 1500000],['0.5m', '1.0m', '1.5m'])
ax.set_xlabel('Q1-Q2 2020 (Months)')
ax.set_ylabel("COVID Cases Reported (Millions)")
ax.set_title("COVID Cases Wave One Peak by Region")
ax.annotate('Wave1 Peak', xy=(3, 1000000),  xycoords='data',
                xytext=(-75, 0), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.annotate('Following weeks of stability, weekly case rates accelerate again', xy=(4.2, 2000000),  xycoords='data',
                xytext=(-50, 20), textcoords='offset points', wrap=True)
ax.legend()
plt.show()
fig.savefig('Wave One COVID Cases by Month by Region.png')
plt.close()
