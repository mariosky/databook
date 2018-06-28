import pandas as pd
from pandas.plotting import andrews_curves

import matplotlib.pyplot as plt


data = pd.read_csv('../../datos-ejemplo/iris.data', header=None,
 names=['LargoSepalo','AnchoSepalo','LargoPetalo','AnchoPetalo','Nombre'])


plt.figure()


andrews_curves(data, 'Nombre')
plt.show()


from pandas.plotting import parallel_coordinates
parallel_coordinates(data, 'Nombre')
plt.show()

