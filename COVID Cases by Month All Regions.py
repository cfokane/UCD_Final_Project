import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv', index_col=0)
Econ_cases=(data.pivot_table(values='Weekly_Cases', index=['Month'], columns=['Region'], aggfunc='sum', fill_value=0, margins=True))
# correct order of months
new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
EconCases=Econ_cases.reindex(new_order, axis=0)


print(EconCases)
fig, ax = plt.subplots(figsize=(12,5))

Q1_Q3 = EconCases["Jan":"Sep"]
ax.plot(Q1_Q3.index, Q1_Q3['All'], label='All Regions')

plt.ylim(0, 1000000) #to set the axis ...xlim for x axis
plt.yticks([1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '10m'])
ax.set_xlabel('Q1-Q3 2020 (Months)')
ax.set_ylabel("COVID Cases Reported (Millions)")
ax.set_title("COVID Cases by Month - All Regions")
ax.annotate('Wave1 Peak', xy=(3, 2500000),  xycoords='data',
                xytext=(-15, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.annotate('Following weeks of stability, weekly case rates accelerate again', xy=(4.5, 3500000),  xycoords='data',
                xytext=(-50, 20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), ha='center', wrap=True)
ax.annotate('Accelerating to 9.8m cases in Sept', xy=(8, 9800000),  xycoords='data',
                xytext=(-120, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.legend(loc=2)
plt.show()
fig.savefig('COVID Cases by Month All Regions.png')
plt.close()