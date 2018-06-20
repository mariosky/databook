



from re import sub
from decimal import Decimal
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


file = open('gross.dat')

data = [(title, Decimal( sub(r'[^\d.]', '', budget)),Decimal( sub(r'[^\d.]', '', gross)))
           for title, budget, gross in [line[:-1].split('|') for line in file ]]

data_array = np.array(data)

budget = np.array( data_array[:, 1 ],dtype='float64')
gross = np.array( data_array[:, 2 ] ,dtype='float64')


sns.jointplot(x=gross, y=budget, kind='hex')
plt.show()