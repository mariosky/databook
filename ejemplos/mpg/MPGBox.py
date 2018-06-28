# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


auto_mpg = pd.read_csv('../../datos-ejemplo/auto-mpg.data', sep='\s+',
            header=None,  na_values='?', names=['mpg' ,'cylinders' ,'displacement' ,'horsepower',
                                                'weight' ,'acceleration' ,'model_year' ,'origin' ,'car_name'],
            dtype={'mpg' :'f4' ,'cylinders' :'i4' ,'displacement' :'f4',
                   'horsepower' :'f4' ,'weight' :'f4' ,'acceleration' :'f4',
                   'model_year' :'i4' ,'origin' :'category' ,'car_name' :'category'})

auto_mpg["origin"].cat.categories = ["USA", "Japan", "Germany"]

fig, ax = plt.subplots()

# the histogram of the data

Japan = auto_mpg[[ auto in ['Japan']  for auto in  auto_mpg.origin]].loc[:,['mpg','model_year','origin','car_name']]

USA = auto_mpg[[ auto in ['USA']  for auto in  auto_mpg.origin]].loc[:,['mpg','model_year','origin','car_name']]


Germany = auto_mpg[[ auto in ['Germany']  for auto in  auto_mpg.origin]].loc[:,['mpg','model_year','origin','car_name']]

print Japan

ax.boxplot([Japan['mpg'],USA['mpg'], Germany['mpg']],
        vert=True,  # vertical box alignment
        patch_artist=True,  # fill with color
        labels=['Japan','USA', 'Germany'])  # will be used to label x-ticks


# add a 'best fit' line
ax.set_ylabel('Millas por Galon')
ax.set_title(u'Rendimiento por país')
ax.yaxis.grid(True)

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
