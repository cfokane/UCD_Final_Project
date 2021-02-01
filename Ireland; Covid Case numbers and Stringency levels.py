import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')

data = pd.read_csv('RDCDFinal.csv', index_col=14)
print(data.columns)

RD =data.loc[:,['location', 'Weekly_Cases','Stringency_Indexed',]]
print(RD.columns)
RD['Ireland'] = RD['location'] == 'Ireland'
RD=RD.query('Ireland == True')
print(RD)


fig, ax = plt.subplots(figsize=(10,5))
ax.plot(RD.index, RD['Weekly_Cases'], color='r', label='Weekly Cases (000s)')
plt.ylim(0, 6000) #to set the axis ...xlim for x axis
plt.yticks([2000, 4000, 6000],['2k', '4k', '6k'])

ax2 = ax.twinx()
ax2.plot(RD.index, RD['Stringency_Indexed'], color='b', label='Stringency Indexed 0-5')
#plt.yscale('log')
ax.set
ax.set_xlabel('Week Number')
ax.set_ylabel("COVID Cases Reported")
ax.set_title("Ireland; Covid Case numbers and Stringency levels")
ax.annotate('Wave1 Peak at 5770 cases', xy=(15, 5700),  xycoords='data',
                xytext=(-125, -55), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.annotate('Infections fall to just 57 cases', xy=(25, 57),  xycoords='data',
                xytext=(25, 50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax2.annotate('L5 restrictions reduce interations with                                                                    consequent reduction in Cases', xy=(20, 4),  xycoords='data',
                xytext=(-25, -20), textcoords='offset points', wrap=True)
ax.legend()
ax2.legend(loc=2)
plt.grid(True)
plt.show()
fig.savefig('Ireland; Covid Case numbers and Stringency levels.png')
plt.close()
