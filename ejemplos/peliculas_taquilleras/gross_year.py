# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


from re import sub

converters={ 0: int,
             1:str,
             3: lambda gross: int(sub(r'[^\d.]', '', gross)),
             4: lambda budget: int(sub(r'[^\d.]', '', budget)),
             5: lambda year: int(sub(r'[^\d.]', '', year)),
             }

names=['rank', 'title', 'studio', 'agross', 'gross', 'year' ]
df = pd.read_table('taquilleras.tsv', header=None, converters=converters, names=names)

print (df)
print (df.dtypes)


plt.plot(df.year, df.agross, '.')
plt.xlabel(u'Año')
plt.ylabel(u'Ganancias')
plt.show()
