

import math
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../../datos-ejemplo/iris.data', header=None)
num_bins = 8
print(df)
fig, ax = plt.subplots()
#print (df.mpg)
# the histogram of the data
n, bins, patches = ax.hist( df[0], num_bins)
n, bins, patches = ax.hist( df[1], num_bins)
# add a 'best fit' line
ax.set_xlabel('Goles')
ax.set_ylabel('Frecuencia')
ax.set_title(r'Goles por partido en Copas del Mundo hasta 2014')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()