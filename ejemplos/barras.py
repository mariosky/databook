import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", context="talk")
rs = np.random.RandomState(7)

f, ax = plt.subplots()


# Generate some sequential data
x = np.array(list("ABCDE"))
y1 = np.array([23,12,11,22,12])


sns.barplot(x, y1, palette="Set3", ax=ax)
ax.set_title("El Title")

# Center the data to make it diverging
plt.setp(sns)


plt.show()
