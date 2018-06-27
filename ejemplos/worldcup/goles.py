import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('fifa-world-cup/WorldCupMatches.csv')
goles = map(sum,zip(df['Home Team Goals'], df['Away Team Goals']))



num_bins = 6

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(goles, num_bins)

# add a 'best fit' line
ax.set_xlabel('Goles')
ax.set_ylabel('Frecuencia')
ax.set_title(r'Goles por partido en Copas del Mundo hasta 2014')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()






