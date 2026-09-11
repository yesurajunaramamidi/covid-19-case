

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('case_time_series.csv')
x=df.iloc[60:,0]
y=df.iloc[60:,1]
plt.figure(figsize=(20,8))
ax=plt.axes()
ax.set_facecolor('black')
ax.set_xlabel('Date',size=30,color='Green')
ax.set_ylabel('No of Cases',size=30,color='Green')
plt.xticks(rotation='vertical',size=20)
plt.title('covid 19 analysis')
plt.tick_params(color='white',size=10)
for i,j in zip(x,y):
    ax.annotate(j,xy=(i,j),color='white',size=12)
ax.annotate('Second Lock Down 15 april 2021',
           xy=(15.2,868),
           xytext=(19.2,500),
           color='white',
           size=20,
           arrowprops=dict(color='white',linewidth=0.02)
           )
plt.grid()
plt.plot(x,y,marker='o',ms=12.0,mfc='red',mec='black')
plt.title('Covid 19 analysis',size=40)
plt.savefig('Covid 19 analysis.pdf')
plt.show()
