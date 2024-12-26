from matplotlib import pyplot as plt
import numpy as np
a=np.array([32,51,72,9,21,12,8])

fig,ax=plt.subplots(figsize=(10,7))
ax.hist(a,bins=[0,25,50,75])

plt.show()
