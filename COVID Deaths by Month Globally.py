import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv', index_col=0)
Econ_cases=(data.pivot_table(values='Weekly_Deaths', index=['Month'], columns=['Region'], aggfunc='sum', fill_value=0, margins=True))
# correct order of months
new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
EconCases=Econ_cases.reindex(new_order, axis=0)


print(EconCases)
fig, ax = plt.subplots(figsize=(12,5))

Q1_Q3 = EconCases["Jan":"Sep"]
ax.plot(Q1_Q3.index, Q1_Q3['All'], label='All Regions')


plt.ylim(0, 250000)
plt.yticks([50000, 100000, 150000, 200000, 250000],['50k', '100k', '150k', '200k', '250k'])
ax.set_xlabel('Q1-Q3 2020 (Months)')
ax.set_ylabel("COVID Deaths Reported (Millions)")
ax.set_title("COVID Deaths by Month Globally")
ax.annotate('Wave 1 Deaths Peak result in higher deaths in Western Europe & North America', xy=(3, 195000),  xycoords='data',
                xytext=(-105, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.annotate('Death again', xy=(6, 1500000),  xycoords='data',
                xytext=(-50, 20), textcoords='offset points',
                 wrap=True)
ax.legend(loc=2)
plt.show()
fig.savefig('COVID Deaths by Month Globally.png')
plt.close()