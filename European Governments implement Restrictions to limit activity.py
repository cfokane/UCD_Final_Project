import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
plt.style.use('seaborn-whitegrid')

RD = pd.read_csv('RDCDFinal.csv', index_col=0)
RDEU = RD.query('Econ_Block== "EU"')
print(RDEU)
# Using .loc to create boolean of Stringency at >=4 ad store as new column
RDEU.loc[:, 'Stringency_IndexL4_L5']= RDEU['Stringency_Indexed']>=4
print(RDEU)

#filter stringency levels >=4 by country

RDEU=RDEU.query('Stringency_IndexL4_L5 == True')
RDEU.to_csv('RDEU.csv')
RDEU2 = pd.read_csv('RDEU.csv')

Str45=(RDEU2.pivot_table(values='Stringency_Indexed', index='Week_Num', columns='location', aggfunc='count', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])


fig, ax =plt.subplots()
ax.plot(Str45['Grand_Total'], label='Stringency Index = 4 or 5')
ax.set_xlabel("Week Number")
ax.set_ylabel("Number of Countries at Highest Stringency Level 5")
ax.set_title('European Governments implement Restrictions to limit activity')
ax.annotate('Wk9 = Italy imposes severe restrictions', xy=(9, 1),  xycoords='data',
                xytext=(-10, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('Wk13 = 24 out of 28 Members', xy=(13, 24),  xycoords='data',
                xytext=(0, -35), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.legend(loc=5)
plt.show()
fig.savefig('European Governments implement Restrictions to limit interaction.png')
plt.close()
