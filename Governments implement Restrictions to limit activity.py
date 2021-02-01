import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
plt.style.use('seaborn-whitegrid')

RDCD2 = pd.read_csv('RDCDFinal.csv', index_col=0)
print(RDCD2)
# Using .loc to create boolean of Stringency at >=4 ad store as new column
RDCD2.loc[:, 'Stringency_Index_L4_L5']= RDCD2['Stringency_Indexed']>=4
print(RDCD2.dtypes)

#filter stringency levels >=4 by country
RDCD2=RDCD2.query('Stringency_Index_L4_L5 == True')
RDCD2.to_csv('RDCD2.csv')
RDCD3 = pd.read_csv('RDCD2.csv')

Str45=(RDCD3.pivot_table(values='Stringency_Indexed', index='Week_Num', columns='location', aggfunc='count', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])


fig, ax =plt.subplots()
ax.plot(Str45['Grand_Total'], label='Stringency_Index L4 or L5')
ax.set_xlabel("Week Number")
ax.set_ylabel("Number of Countries at Highest Stringency Levels")
ax.set_title('Governments implement Restrictions to limit interaction')
ax.annotate('Wk10 = 3 Countries', xy=(10, 2.5),  xycoords='data',
                xytext=(10, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('Wk15 = 150 Countries', xy=(15, 148),  xycoords='data',
                xytext=(10, -20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )

ax.legend(loc=5)
plt.show()
fig.savefig('Governments implement Restrictions to limit interaction.png')
plt.close()
