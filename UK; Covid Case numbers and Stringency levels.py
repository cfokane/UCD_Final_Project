import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')
# set index as Week-Num (column 14)
data = pd.read_csv('RDCDFinal.csv', index_col=14)
print(data.columns)

RD =data.loc[:,['location', 'Weekly_Cases','Stringency_Indexed',]]
print(RD.columns)
RD['UK'] = RD['location'] == 'United Kingdom'
RD=RD.query('UK == True')
print(RD)
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(RD.index, RD['Weekly_Cases'], color='r', label='Weekly Cases')
plt.ylim(0, 40000) #to set the axis ...xlim for x axis
plt.yticks([10000, 20000, 30000, 40000],['10k', '20k', '30k', '40k'])

ax2 = ax.twinx()
ax2.plot(RD.index, RD['Stringency_Indexed'], color='b', label='Stringency Indexed 0-5')
#plt.yscale('log')
ax.set
ax.set_xlabel('Week Number')
ax.set_ylabel("COVID Cases Reported")
ax.set_title("UK; Covid Case numbers and Stringency levels")
ax.annotate('Wave1 Peak at >30k cases for 4 weeks', xy=(14, 30000),  xycoords='data',
                xytext=(0, -55), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.annotate('Infections fall to post peak low of 3784 cases in Wk30', xy=(30, 3784),  xycoords='data',
                xytext=(25, 50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax2.annotate('L4 restrictions lower than Ireland -                                                                                  does this account for sower decline in cases?', xy=(20, 4),  xycoords='data',
                xytext=(-25, -20), textcoords='offset points', wrap=True)
ax.legend()
ax2.legend()
plt.grid(True)
plt.show()
fig.savefig('UK; Covid Case numbers and Stringency levels.png')
plt.close()
