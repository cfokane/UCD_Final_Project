import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCDFinal.csv', index_col=0)
print(data.columns)
RD = data.loc[:, ['location', 'Econ_Block', 'Week_Num', 'Weekly_Cases',
                  'Stringency_Indexed', 'population', 'Weekly_Deaths',]]
RDEcon = RD.query('Econ_Block== "EU"')

# Chart showing Case numbers over time, against number of deaths in teh UK
RDUK = RDEcon.query('location == "United Kingdom"')
RDUK = pd.DataFrame(RDUK)
g= sns.relplot(x='Week_Num', y='Weekly_Cases', data=RDUK, height=5, aspect=1.5, size='Weekly_Cases', hue='Weekly_Deaths')
sns.axes_style('darkgrid')
g.fig.suptitle('UK; COVID Cases & Deaths by Week', x=0.5, y=1.0)
g.set_ylabels('Weekly Cases Recorded')
g.set_xlabels('Week Number')
plt.subplots_adjust(top=0.98, bottom=0.13)
#plt.figlegend()
sns.set_palette('RdBu')
plt.grid(True)
#sns.set_context('paper')
plt.setp(g._legend.get_texts(), fontsize=8)
plt.savefig('UK; Cases & Deaths.png')
plt.show()
plt.cla()


