import matplotlib.pyplot as plt
import numpy as np

cars=['bmw','audi','jaguar','alto']
data=[34,22,40,12]
fig=plt.figure(figsize=(10,7))
plt.pie(data,labels=cars)
plt.show()
