import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCDFinal.csv', index_col=0)
print(data.columns)
RD = data.loc[:, ['European Union', 'location',  'Econ_Block', 'Week_Num', 'total_cases',
                  'Stringency_Indexed', 'population', 'total_deaths']]
print(RD)
RD = RD.query('Econ_Block== "EU"')
RD.sort_values('European Union')
RD['European Union Status'] = RD['location'] + ' ' + RD['European Union']

RD['Deaths_%_Cases']= (RD['total_deaths'] / RD['total_cases']).round(1)
RD.fillna(0)
RD1 = pd.DataFrame(RD)
#RDEcon = RD.query('Econ_Block== "EU"')
#RDIre = RDEcon.query('location == "Ireland"')
print(RD)

RD2 = RD1.loc[:, ['European Union Status', 'Week_Num', 'total_cases',
                  'total_deaths', 'Deaths_%_Cases']]
#print(RDDeath)
#RDDeath.to_csv('RDDeathchecking.csv')
sns.set(style='whitegrid')
# Chart showing Case numbers over time, against number of deaths
g=sns.relplot(x='Week_Num', y='European Union Status', data=RD2, kind='scatter', height=6.5, aspect=1.5, size='total_cases', hue='Deaths_%_Cases')
#g= sns.relplot(x='Week_Num', y='Weekly_Cases', data=RDIre, size='Weekly_Deaths', height=5, aspect=1.75, hue='Weekly_Deaths', legend='full')
g.fig.suptitle('Cumulative EU Members; Cases & Deaths by Week', x=0.5, y=1.0)
plt.subplots_adjust(top=0.98)

#leg=g._legend
#leg.set_bbox_to_anchor([0.5, 0.5])
#leg._loc=2
#fig=ax.get_figure()
#fig.savegig('Ireland; Cases & Deaths.png')
plt.savefig('Cumulative EU; Cases & Deaths.png')
plt.show()
plt.clf()