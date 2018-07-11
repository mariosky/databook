import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('fifa-world-cup/WorldCupMatches.csv')
goles = map(sum,zip(df['Home Team Goals'], df['Away Team Goals']))


fig, ax = plt.subplots()

# the histogram of the data


ax.boxplot(list(goles),
        vert=True,  # vertical box alignment
        patch_artist=True,  # fill with color
        labels=['Goles'])  # will be used to label x-ticks

ax.set_ylim(-1, 15)


# add a 'best fit' line
ax.set_ylabel('Goles')
ax.set_title(r'Goles por partido en Copas del Mundo hasta 2014')
ax.yaxis.grid(True)

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
