import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv', index_col=0)

data=(data.pivot_table(values='total_cases', index='Week_Num', columns='location', aggfunc='count', fill_value=0, margins=True, margins_name='Grand_Total_Cases').iloc[:-1,:])

print(data)
from matplotlib.pyplot import rcParams
fig, ax =plt.subplots()
#rcParams['figure.figsize']=15,2 # to change size of graph
#plt.plot(data.Grand_Total_Cases, color='m', marker='o', linestyle='-', label='Cases Recorded')
plt.plot(data.Grand_Total_Cases, label='No of Countries Recording Infections')
#plt.plot(data.Week_Num)
#plt.grid(True, color='g',linestyle=':')
plt.xlabel('Week Number')
plt.ylim(0, 270) #to set the axis ...xlim for x axis
plt.yticks((50, 100, 150, 200))
plt.ylabel('Number of Countries with Confirmed Cases by Week')
plt.title('Global Pandemic; Rapid & Unprecedented Spread in Cases around the world')
ax.annotate('Wk20: Virus present in all 208 countries', xy=(20, 208), xycoords='data',
            xytext=(-70, 20), textcoords='offset points',
            arrowprops=dict(arrowstyle="->")
            )
ax.annotate('Wk12: 90% countries report infections', xy=(12, 187), xycoords='data',
            xytext=(20, -25), textcoords='offset points',
            arrowprops=dict(arrowstyle="->")
            )
ax.annotate('Wk11: 70%  with infections', xy=(11, 144),  xycoords='data',
                xytext=(20, -25), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('Wk8: 20% countries report infections', xy=(8, 43),  xycoords='data',
                xytext=(30, -15), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
            )

ax.legend()
plt.show() ; # or you could use plt.style.use('ggplot') or plt.style.use('fivethirtyeight')
fig.savefig('Rapid & Unprecedented Spread in Cases around the world.png')
plt.close()


