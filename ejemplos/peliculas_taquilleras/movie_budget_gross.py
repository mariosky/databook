# -*- coding: utf-8 -*-
from re import sub
from decimal import Decimal
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker



file = open('gross.dat')

data =  [ (title, Decimal( sub(r'[^\d.]', '', budget)),Decimal( sub(r'[^\d.]', '', gross)) )
           for  title, budget, gross in  [line[:-1].split('|') for line in file ]]

data_array = np.array(data)

budget = np.array( data_array[:, 1 ],dtype='int')
gross = np.array( data_array[:, 2 ] ,dtype='int')


fig, ax = plt.subplots(1, 1)
#ax.set_xscale('log')
#ax.set_yscale('log')
ax.set_xlim(900, 500000000)


def format_fn(tick_val, tick_pos):
    format = matplotlib.ticker.EngFormatter()
    return '$' + format.format_data(tick_val)


ax.set_title(u'Presupuesto de producción vs recaudación en taquilla (sin ajuste a la inflación)')

ax.set_xlabel(u'Presupuesto')
ax.set_ylabel(u'Recaudación')

#ax.set_xlabel(u'Presupuesto en escala logarítmica')
#ax.set_ylabel(u'Recaudación en escala logarítmica')



ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(format_fn))
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(format_fn))



__=ax.plot(budget, gross, '.')




plt.show()


import seaborn as sns

g = sns.jointplot(x=gross, y=budget, xlim=[900, 500000000], ylim=[900,10000000])

ax = g.ax_joint
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(900, 500000000)
plt.show()