# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd


from re import sub


df = pd.read_csv('fifa-world-cup/WorldCups.csv', converters={'Attendance': lambda attendence: int(sub(r'\.', '', attendence))})


index = range(len(df))
bar_width = .80
opacity = 0.4

fig, ax = plt.subplots(1, 1)


plt.yticks(index, map(lambda d: "{0} {1}".format(d[1], d[0]),  zip(df.Year, df.Country)))


asistencia = ax.barh(  index,  df.Attendance,bar_width,
                    alpha=opacity, color='b')




ax.set_xlabel(u'Asistencia')
ax.set_title(u'Asistencia a las Copas del Mundo de la FIFA')

plt.show()